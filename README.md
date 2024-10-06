# `anthropic-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by Anthropic's API.

# Installation

1. Clone this repo: `git clone https://github.com/AK391/anthropic-gradio.git`
2. Navigate into the folder that you cloned this repo into: `cd anthropic-gradio`
3. Install this package: `pip install -e .`

<!-- ```bash
pip install anthropic-gradio
``` -->

That's it! 

# Basic Usage

Just like if you were to use the `anthropic` API, you should first save your Anthropic API key to this environment variable:

```
export ANTHROPIC_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import anthropic_gradio

gr.load(
    name='claude-3-opus-20240229',
    src=anthropic_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to the model on Anthropic!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from an Anthropic endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example:

```py
import gradio as gr
import anthropic_gradio

gr.load(
    name='claude-3-opus-20240229',
    src=anthropic_gradio.registry,
    title='Anthropic-Gradio Integration',
    description="Chat with Claude 3 Opus model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import anthropic_gradio

with gr.Blocks() as demo:
    with gr.Tab("Claude 3 Opus"):
        gr.load('claude-3-opus-20240229', src=anthropic_gradio.registry)
    with gr.Tab("Claude 3 Sonnet"):
        gr.load('claude-3-sonnet-20240229', src=anthropic_gradio.registry)

demo.launch()
```

# Under the Hood

The `anthropic-gradio` Python library has two dependencies: `anthropic` and `gradio`. It defines a "registry" function `anthropic_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models in Anthropic

| Model | Context Length | Output Length | Dtype / Precision |
|-------|----------------|---------------|-------|
| claude-3-opus-20240229 | 200,000 | Varies | - |
| claude-3-sonnet-20240229 | 200,000 | Varies | - |
| claude-3-haiku-20240307 | 200,000 | Varies | - |
| claude-2.1 | 200,000 | Varies | - |
| claude-2.0 | 100,000 | Varies | - |

-------

Note: if you are getting an authentication error, then the Anthropic API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```py
import os

os.environ["ANTHROPIC_API_KEY"] = ...
```