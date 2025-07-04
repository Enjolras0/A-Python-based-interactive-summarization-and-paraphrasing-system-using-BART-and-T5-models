import gradio as gr
import re
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_sentences(text):
    return re.split(r'(?<=[.?!])\s+', text.strip())

def handle_generate(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    sentences = split_sentences(summary)
    result = []
    for i in range(5):
        if i < len(sentences):
            result.append(gr.update(value=sentences[i], visible=True))
        else:
            result.append(gr.update(value="", visible=False))
    return result

with gr.Blocks() as demo:
    input_box = gr.Textbox(lines=10, label="输入英文原文")
    generate_button = gr.Button("生成摘要")
    output_boxes = [gr.Textbox(label=f"摘要句 {i+1}", visible=False) for i in range(5)]
    generate_button.click(handle_generate, inputs=[input_box], outputs=output_boxes)

demo.launch()
