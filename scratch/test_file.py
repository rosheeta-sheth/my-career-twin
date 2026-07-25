import gradio as gr
import urllib.request
import time
import json

with gr.Blocks() as demo:
    f = gr.File(value="summary.txt")

demo.launch(server_port=7862, prevent_thread_lock=True)

# Wait for server to start
time.sleep(2)

# Make a request to the API to get the component props
req = urllib.request.Request("http://127.0.0.1:7862/config")
try:
    with urllib.request.urlopen(req) as response:
        config = json.loads(response.read().decode())
        # Find the File component and print its value
        for comp in config['components']:
            if comp['type'] == 'file':
                print(comp['props']['value'])
except Exception as e:
    print(e)
