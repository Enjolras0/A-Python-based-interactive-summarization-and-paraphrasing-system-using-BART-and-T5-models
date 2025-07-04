from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


tokenizer = AutoTokenizer.from_pretrained("prithivida/parrot_paraphraser_on_T5", use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/parrot_paraphraser_on_T5")

def paraphrase(sentence, diversity=3):
    input_text = f"paraphrase: {sentence} </s>"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)

    outputs = model.generate(
        input_ids=input_ids,
        max_length=128,
        num_return_sequences=diversity,
        do_sample=True,
        top_k=120,
        top_p=0.98,
        temperature=1.5,
        no_repeat_ngram_size=2
    )

    return [tokenizer.decode(out, skip_special_tokens=True) for out in outputs]


if __name__ == "__main__":
    s = "Digital innovations have permeated almost every aspect of modern life."
    res = paraphrase(s)
    for i, r in enumerate(res):
        print(f"候选改写{i+1}: {r}")
