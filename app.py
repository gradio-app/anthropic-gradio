import gradio as gr
import anthropic_gradio

gr.load(
    name='claude-3-opus-20240229',
    src=anthropic_gradio.registry,
).launch()