from fastapi import FastAPI
import gradio as gr

from chat import run

app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200

app = gr.mount_gradio_app(app, run, path='/gradio')