import gradio as gr
import anthropic_gradio

gr.load(
    name='claude-3-opus-20240229',
    src=anthropic_gradio.registry,
    title='Anthropic-Gradio Integration',
    description="Chat with Claude 3 Opus model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()