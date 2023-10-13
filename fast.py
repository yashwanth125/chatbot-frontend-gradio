from fastapi import FastAPI
import random
import time
import requests
app = FastAPI()

@app.get('/')
async def balabala():
    import gradio as gr

    with gr.Blocks() as demo:
        gr.Markdown("""<h1><center>Musle Blaze PDF Chatbot</center></h1>""")
        chatbot = gr.Chatbot()
        state = gr.State()
        message = gr.Textbox()
        submit = gr.Button("SEND")

        def chatgpt_clone(input_q, history):
            history = history or []
            s = list(sum(history, ()))
            s.append(input_q)
            output = requests.get('https://canadabuild-f527cb72e976.herokuapp.com/support/'+input_q)
            data = output.json()
            history.append((input_q, data["Answer"]))
            return history, history

        submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

    global app
    demo.queue()
    demo.startup_events()
    app = gr.mount_gradio_app(app, demo, f'/gradio')
