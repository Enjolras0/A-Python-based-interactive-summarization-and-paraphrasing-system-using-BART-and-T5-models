# A-Python-based-interactive-summarization-and-paraphrasing-system-using-BART-and-T5-models
A Python-based interactive summarization and paraphrasing system using BART and T5 models.
项目名称
基于 Transformer 的英文文本摘要与句子改写工具
A Python-based interactive summarization and paraphrasing system using BART and T5 models.

一、项目简介
本项目旨在构建一个基于现代自然语言处理技术的文本摘要与改写系统。用户可输入一段英文长文，系统将自动生成摘要，并允许用户对每一句摘要进行语义等价的改写，最终输出一个“可控、可编辑”的摘要版本。

本系统强调人机协作而非纯自动化，突出用户参与和句子级微调控制能力，适用于写作辅助、摘要润色、教育用途等场景。

二、技术栈与依赖
Python 3.x
Transformers 库（transformers）
PyTorch（torch）
SentencePiece（sentencepiece，用于加载T5 tokenizer）
Gradio（用于构建前端界面）

安装依赖示例：
pip install transformers torch sentencepiece gradio

三、使用模型
文本摘要模型：facebook/bart-large-cnn

基于 BART 的英文摘要模型，适合通用性英文段落的生成式摘要任务。

句子改写模型：prithivida/parrot_paraphraser_on_T5

基于 T5-base 的改写模型，适用于生成语义等价的句子候选版本，具备较高的语言多样性。

四、系统功能模块与使用流程

Step 1：英文长文本自动摘要（Gradio 界面）
功能描述：
用户输入一段英文长文，系统调用 BART 模型生成压缩后的摘要段落。

运行方式：
python step1_summarize.py

交互逻辑：

输入英文原文（可粘贴自任何英文文本）

点击按钮，模型生成摘要

显示英文摘要段落（1段）

技术说明：

使用 transformers 的 pipeline("summarization") 接口

使用 facebook/bart-large-cnn 模型

最大长度设置：max_length=100，min_length=30，do_sample=False

Step 2：摘要内容分句展示（Gradio 界面）
功能描述：
将摘要段落进行英文分句处理，拆分为最多5句，供后续句子级改写操作使用。

运行方式：
python step2_split_sentences.py

交互逻辑：

输入英文原文（可直接粘贴 Step 1 的输出）

点击 “生成摘要” 按钮

系统生成摘要，并自动拆分为最多5个句子，显示为独立句子框

技术说明：

调用同样的 BART 模型生成摘要

使用正则表达式分句：re.split(r'(?<=[.?!])\s+', text)

Step 3：摘要句子改写（控制台交互）
功能描述：
针对每一个摘要句子，系统可生成3个改写候选句子，用户可根据语义偏好进行选择替换。

运行方式：
python step3_paraphrase.py

交互逻辑：

手动复制 Step 2 输出的摘要句子之一

将该句粘贴到 paraphrase.py 的输入中

控制台输出 3 个改写候选句

用户可选择其中一个替换原句，拼接生成最终版本摘要

技术说明：

使用 prithivida/parrot_paraphraser_on_T5 模型

采用采样生成策略，设置如下：
do_sample=True
top_k=120
top_p=0.98
temperature=1.5
no_repeat_ngram_size=2

五、完整运行流程建议

使用 Step 1 对一段英文原文生成摘要段落

将摘要段落粘贴到 Step 2 中进行分句

对每一句摘要句，使用 Step 3 生成 paraphrase 候选句

根据语义喜好，选择或保留原句，组合出最终摘要版本

六、项目亮点

支持自动摘要 + 半自动改写，强调人机协作

模型选型合理，分别使用 BART 和 T5 完成各自子任务

交互逻辑清晰，功能拆分明确，可用于展示或扩展

项目兼容 CLI 和 Gradio 界面，便于教学演示和系统部署

七、项目目录结构建议
summarize_project/
├── step1_summarize.py # 功能一：文本摘要生成器（Gradio）
├── step2_split_sentences.py # 功能二：摘要句子分句展示（Gradio）
├── step3_paraphrase.py # 功能三：句子改写生成（控制台）
├── requirements.txt # 依赖库列表
├── README.txt # 项目说明文档（本文件）
└── screenshots/ # 可选：运行过程截图

八、可选拓展方向

支持中文摘要（可替换为 Pegasus 或 Randeng 模型）

添加 paraphrase 候选句评分（如句子相似度、语言流畅度）

改写句排序优化与用户定制控制（如风格、语气）

将三步流程整合为单一 Gradio 页面，支持可视化交互

九、参考资料与致谢

HuggingFace Transformers 官方文档：https://huggingface.co/docs

facebook/bart-large-cnn 模型页：https://huggingface.co/facebook/bart-large-cnn

prithivida/parrot_paraphraser_on_T5 模型页：https://huggingface.co/prithivida/parrot_paraphraser_on_T5
