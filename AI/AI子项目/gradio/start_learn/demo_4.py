import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

# An Image Example
# Gradio supports many types of components, such as Image, DataFrame, 
# Video, or Label. Let's try an image-to-image function to get a feel for these!
demo = gr.Interface(sepia, gr.Image(), "image")
demo.launch()