import gradio as gr
from app.config.settings.base import ROOT_DIR


def simple_ai() -> gr.Blocks:

    with gr.Blocks(title="Simple AI") as demo:

        gr.HTML("<h1 align=center>🐻 Simple AI</h1>")

    demo.favicon_path = ROOT_DIR / "static" / "favicon.ico"
    return demo
