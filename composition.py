import gradio as gr
import anthropic_gradio  # Changed from openai_gradio to anthropic_gradio

with gr.Blocks() as demo:
    with gr.Tab("Claude-3-Opus"):
        gr.load('claude-3-opus-20240229', src=anthropic_gradio.registry)
    with gr.Tab("Claude-3-Sonnet"):
        gr.load('claude-3-sonnet-20240229', src=anthropic_gradio.registry)

demo.launch()