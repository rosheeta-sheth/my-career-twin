import sys
import os

# Add path so imports work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import respond, initial_history

print("--- Testing RAG Retrieval & Multi-Source Query ---")
history = initial_history()
message = "Compare the tech stack of the AI Equity Traders project to the Personal Career Agent project."
print(f"User: {message}")

generator = respond(message, history)
final_state = None
for state in generator:
    final_state = state

# final_state format: updated_history, "", final_status, audio_path, fu1, fu2, fu3
updated_history = final_state[0]
reply = updated_history[-1]["content"]
print(f"\nAssistant: {reply}\n")

print("--- Testing Function Calling (Contact Capture) ---")
message2 = "My email is test_qa@example.com, please reach out."
print(f"User: {message2}")

generator2 = respond(message2, updated_history)
final_state2 = None
for state in generator2:
    final_state2 = state

updated_history2 = final_state2[0]
reply2 = updated_history2[-1]["content"]
print(f"\nAssistant: {reply2}\n")

print("Backend QA tests completed successfully.")
