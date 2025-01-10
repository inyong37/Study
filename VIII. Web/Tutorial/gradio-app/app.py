import gradio as gr

def page_1_content():
    return "Content for Page 1"

def page_2_content():
    return "Content for Page 2"

def page_3_content():
    return "Content for Page 3"

def page_4_content():
    return "Content for Page 4"

def page_5_content():
    return "Content for Page 5"

def page_6_content():
    return "Content for Page 6"

# Define interface components
with gr.Blocks() as demo:
    with gr.Tab("Page 1"):
        gr.Textbox(label="Page 1", interactive=False, value=page_1_content())
        
    with gr.Tab("Page 2"):
        gr.Textbox(label="Page 2", interactive=False, value=page_2_content())
        
    with gr.Tab("Page 3"):
        gr.Textbox(label="Page 3", interactive=False, value=page_3_content())
        
    with gr.Tab("Page 4"):
        gr.Textbox(label="Page 4", interactive=False, value=page_4_content())
        
    with gr.Tab("Page 5"):
        gr.Textbox(label="Page 5", interactive=False, value=page_5_content())
        
    with gr.Tab("Page 6"):
        gr.Textbox(label="Page 6", interactive=False, value=page_6_content())

demo.launch()
