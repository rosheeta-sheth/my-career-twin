import gradio as gr
import os

gr.set_static_paths(paths=[os.path.abspath(os.path.dirname(__file__))])

with gr.Blocks() as demo:
    gr.HTML("<a href='/file=" + os.path.abspath(os.path.join(os.path.dirname(__file__), "summary.txt")) + "'>Link</a>")

demo.launch(server_port=7861)
