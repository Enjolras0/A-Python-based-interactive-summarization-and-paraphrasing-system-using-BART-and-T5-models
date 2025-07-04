from transformers import pipeline
import gradio as gr

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text.strip())==0:
        return '请输入一段文字！'
    summary=summarizer(text,max_length=100,min_length=30,do_sample=False)
    return summary[0]['summary_text']

iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=15, placeholder="请输入英文文章...", label="原始文本"),
    outputs=gr.Textbox(label="生成的摘要"),
    title="文本摘要生成器",
    description="使用 BART 模型生成摘要"
)

iface.launch()