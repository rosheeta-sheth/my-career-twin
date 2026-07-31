from __future__ import annotations

import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from content import ABOUT_HTML, PROJECTS_HTML, RESUME_HTML
from context import TWIN_SYSTEM_PROMPT
from styles import CSS, EXAMPLES, HEADER_HTML, JS
from tools import handle_tool_calls, tools
from knowledge import KnowledgeBase
import tempfile

load_dotenv(override=True)

# Initialize KB
kb = KnowledgeBase()
kb.initialize(base_dir=os.path.dirname(__file__))

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

openai = OpenAI(timeout=60.0, max_retries=2)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

WELCOME_MESSAGE = (
    "Hi — I'm **Rosheeta's career assistant**. Ask about her AI/ML projects, "
    "analytics experience, technical skills, education, or how to get in touch.\n\n"
    "You can also browse the **About**, **Resume**, and **Projects** tabs above."
)


def initial_history() -> list[dict[str, str]]:
    return [{"role": "assistant", "content": WELCOME_MESSAGE}]


def status_html(state: str = "ready", message: str | None = None) -> str:
    labels = {
        "ready": "Ready",
        "thinking": "Thinking…",
        "error": "Unavailable",
    }
    label = message or labels.get(state, labels["ready"])
    return (
        f'<div class="chat-status" data-state="{state}">'
        '<span class="status-dot"></span>'
        f"<span>{label}</span>"
        "</div>"
    )


def _message_parts(message):
    if isinstance(message, dict):
        return message.get("role"), message.get("content")
    return getattr(message, "role", None), getattr(message, "content", None)


def respond(message, history):
    history = history or initial_history()
    message = (message or "").strip()

    if not message:
        yield history, "", status_html("ready"), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)
        return

    clean_history = []
    for item in history:
        role, content = _message_parts(item)
        if role in {"user", "assistant"} and isinstance(content, str) and content:
            clean_history.append({"role": role, "content": content})

    messages = system + clean_history + [{"role": "user", "content": message}]
    updated_history = history + [{"role": "user", "content": message}, {"role": "assistant", "content": ""}]
    
    yield updated_history, "", status_html("thinking"), None, gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

    thoughts = []

    try:
        while True:
            response_stream = openai.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                tools=tools,
                stream=True,
            )
            
            tool_calls_accumulator = {}
            reply = ""
            
            for chunk in response_stream:
                delta = chunk.choices[0].delta
                
                if delta.content:
                    reply += delta.content
                    display_reply = reply.split("---FOLLOW_UPS---")[0].strip()
                    
                    updated_history[-1]["content"] = display_reply
                    yield updated_history, "", status_html("thinking"), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)
                    
                if delta.tool_calls:
                    for tc in delta.tool_calls:
                        if tc.index not in tool_calls_accumulator:
                            tool_calls_accumulator[tc.index] = {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": ""}}
                        if tc.function.arguments:
                            tool_calls_accumulator[tc.index]["function"]["arguments"] += tc.function.arguments
                            
            if not tool_calls_accumulator:
                break
                
            assembled_tool_calls = [tool_calls_accumulator[k] for k in sorted(tool_calls_accumulator.keys())]
            messages.append({"role": "assistant", "tool_calls": assembled_tool_calls})
            
            # Update thoughts UI before executing tools
            import json
            for tc in assembled_tool_calls:
                t_name = tc["function"]["name"]
                t_args = tc["function"]["arguments"]
                if t_name == "search_knowledge_base":
                    try:
                        q = json.loads(t_args).get("query", "")
                    except:
                        q = "documents"
                    thoughts.append(f"🔍 Searching knowledge base for: `{q}`...")
                elif t_name == "record_user_details":
                    thoughts.append(f"📝 Securely saving contact details...")
            
            thoughts_html = "<details><summary>Agent Thinking...</summary>\n\n" + "\n".join([f"- {t}" for t in thoughts]) + "\n</details>\n\n"
            updated_history[-1]["content"] = thoughts_html + "..."
            yield updated_history, "", status_html("thinking"), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

            class DummyFunction:
                def __init__(self, name, args):
                    self.name = name
                    self.arguments = args
            class DummyToolCall:
                def __init__(self, id, name, args):
                    self.id = id
                    self.function = DummyFunction(name, args)
                    
            dummy_calls = [DummyToolCall(tc["id"], tc["function"]["name"], tc["function"]["arguments"]) for tc in assembled_tool_calls]
            results = handle_tool_calls(dummy_calls)
            messages.extend(results)

        follow_ups = []
        display_reply = reply
        if "---FOLLOW_UPS---" in reply:
            parts = reply.split("---FOLLOW_UPS---")
            display_reply = parts[0].strip()
            follow_ups = [line.strip().lstrip('-').strip() for line in parts[1].strip().split('\n') if line.strip().startswith('-')]
            
        updated_history[-1]["content"] = display_reply

        final_status = status_html("ready")
                
        fu1 = gr.update(value=follow_ups[0], visible=True) if len(follow_ups) > 0 else gr.update(visible=False)
        fu2 = gr.update(value=follow_ups[1], visible=True) if len(follow_ups) > 1 else gr.update(visible=False)
        fu3 = gr.update(value=follow_ups[2], visible=True) if len(follow_ups) > 2 else gr.update(visible=False)
        
        yield updated_history, "", final_status, fu1, fu2, fu3

    except Exception as error:
        print(f"Chat request failed: {type(error).__name__}: {error}", flush=True)
        reply = "Sorry — I couldn't complete that response right now. Please try again in a moment."
        updated_history[-1]["content"] = reply
        yield updated_history, "", status_html("error"), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)


def reset_chat():
    return initial_history(), "", status_html("ready"), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)


def wire_chat(trigger):
    return (
        trigger(
            lambda: status_html("thinking"),
            None,
            status_box,
            queue=False,
        )
        .then(
            respond,
            [msg, chatbot],
            [chatbot, msg, status_box, fu1, fu2, fu3],
            show_progress="hidden"
        )
    )


with gr.Blocks(title="Rosheeta Sheth — Career Twin", fill_width=True) as demo:
    gr.HTML(HEADER_HTML)

    with gr.Tabs(elem_classes=["main-tabs"]):
        with gr.Tab("Chat"):
            with gr.Column(elem_id="chat-shell"):
                with gr.Row(elem_id="chat-toolbar"):
                    status_box = gr.HTML(status_html("ready"), elem_id="status-wrap")
                    new_chat = gr.Button("New chat", elem_id="new-chat", scale=0)

                chatbot = gr.Chatbot(
                    value=initial_history(),
                    show_label=False,
                    elem_id="twin-chat",
                    layout="bubble",
                    avatar_images=(None, "profile.png"),
                    height=520,
                    min_height=320,
                    render_markdown=True,
                    buttons=[],
                    feedback_options=None,
                    group_consecutive_messages=False,
                    placeholder="Ask about experience, projects, or skills.",
                )

                with gr.Row(elem_id="composer"):
                    msg = gr.Textbox(
                        placeholder="Ask a question...",
                        show_label=False,
                        container=False,
                        lines=1,
                        max_lines=5,
                        scale=1,
                        elem_id="msg-box",
                    )
                    send = gr.Button(
                        "Send",
                        variant="primary",
                        scale=0,
                        min_width=88,
                        elem_id="send-btn",
                    )
                


                with gr.Column(elem_id="prompts-section"):
                    gr.HTML('<div class="prompts-label">Suggested questions</div>')
                    with gr.Row(elem_id="prompt-grid"):
                        example_buttons = [
                            gr.Button(text, elem_classes=["prompt-card"])
                            for text in EXAMPLES
                        ]
                    with gr.Row(elem_id="follow-up-grid"):
                        fu1 = gr.Button("", visible=False, elem_classes=["prompt-card"])
                        fu2 = gr.Button("", visible=False, elem_classes=["prompt-card"])
                        fu3 = gr.Button("", visible=False, elem_classes=["prompt-card"])
                        follow_up_buttons = [fu1, fu2, fu3]

        with gr.Tab("About"):
            gr.HTML(ABOUT_HTML)

        with gr.Tab("Resume"):
            gr.HTML(RESUME_HTML)

        with gr.Tab("Projects"):
            gr.HTML(PROJECTS_HTML)

    wire_chat(msg.submit)
    wire_chat(send.click)
    

    for button in example_buttons + follow_up_buttons:
        (
            button.click(
                lambda text: text,
                inputs=[button],
                outputs=[msg],
                queue=False,
            )
            .then(
                lambda: status_html("thinking"),
                None,
                status_box,
                queue=False,
            )
            .then(
                respond,
                [msg, chatbot],
                [chatbot, msg, status_box, fu1, fu2, fu3],
                show_progress="hidden"
            )
        )

    new_chat.click(
        reset_chat,
        None,
        [chatbot, msg, status_box, fu1, fu2, fu3],
        queue=False,
    )

if __name__ == "__main__":
    import os
    demo.launch(css=CSS, js=JS, theme=gr.themes.Soft(), allowed_paths=[os.path.abspath(os.path.dirname(__file__))])
