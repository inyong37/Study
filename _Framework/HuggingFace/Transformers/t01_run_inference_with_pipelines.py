# Pipelines for inference

# Pipeline usage

audio_input_file_0 = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
audio_input_file_1 = "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac"

from transformers import pipeline

transcriber = pipeline(task='automatic-speech-recognition')
transcriber(audio_input_file_0)

transcriber = pipeline(model="openai/whisper-large-v2")
transcriber(audio_input_file_0)

transcriber(
    [
        audio_input_file_0,
        audio_input_file_1,
    ]
)

# Parameters

transcriber = pipeline(model='openai/whisper-large-v2', my_parameter=1)

out = transcriber(...)  # This will use `my_parameter=1`.
out = transcriber(..., my_parameter=2)  # This will override and use `my_parameter=2`.
out = transcriber(...)  # This will go back to using `my_parameter=1`.

# Device

transcriber = pipeline(model="openai/whisper-large-v2", device=0)

transcriber = pipeline(model="openai/whisper-large-v2", device_map="auto") # pip install --upgrade accelerate

# Batch size

transcriber = pipeline(model="openai/whisper-large-v2", device=0, batch_size=2)
audio_filenames = [f"https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/{i}.flac" for i in range(1, 5)]
texts = transcriber(audio_filenames)

# Task specific parameters

transcriber = pipeline(model="openai/whisper-large-v2", return_timestamps=True)
transcriber(audio_input_file_0)

transcriber = pipeline(model="openai/whisper-large-v2", chunk_length_s=30)
transcriber("https://huggingface.co/datasets/reach-vb/random-audios/resolve/main/ted_60.wav")

# Using pipelines on a dataset

def data():
    for i in range(1000):
        yield f"My example {i}"


pipe = pipeline(model="openai-community/gpt2", device=0)
generated_characters = 0
for out in pipe(data()):
    generated_characters += len(out[0]["generated_text"])

# KeyDataset is a util that will just output the item we're interested in.
from transformers.pipelines.pt_utils import KeyDataset
from datasets import load_dataset

pipe = pipeline(model="hf-internal-testing/tiny-random-wav2vec2", device=0)
dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation[:10]")

for out in pipe(KeyDataset(dataset, "audio")):
    print(out)

# Vision pipeline

from transformers import pipeline

vision_classifier = pipeline(model="google/vit-base-patch16-224")
preds = vision_classifier(
    images="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
)
preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
print(preds)

# Text pipeline

from transformers import pipeline

# This model is a `zero-shot-classification` model.
# It will classify text, except you are free to choose any label you might imagine
classifier = pipeline(model="facebook/bart-large-mnli")
classifier(
    "I have a problem with my iphone that needs to be resolved asap!!",
    candidate_labels=["urgent", "not urgent", "phone", "tablet", "computer"],
)

# Multimodal pipeline

from transformers import pipeline

vqa = pipeline(model="impira/layoutlm-document-qa")
output = vqa(
    image="https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png",
    question="What is the invoice number?",
)
output[0]["score"] = round(output[0]["score"], 3)
print(output)

# Using pipeline on large models with accelerate

# pip install accelerate
import torch
from transformers import pipeline

pipe = pipeline(model="facebook/opt-1.3b", torch_dtype=torch.bfloat16, device_map="auto")
output = pipe("This is a cool example!", do_sample=True, top_p=0.95)

# pip install accelerate bitsandbytes
import torch
from transformers import pipeline

pipe = pipeline(model="facebook/opt-1.3b", device_map="auto", model_kwargs={"load_in_8bit": True})
output = pipe("This is a cool example!", do_sample=True, top_p=0.95)

# Creating web demos from pipelines with gradio

from transformers import pipeline
import gradio as gr # pip install gradio

pipe = pipeline("image-classification", model="google/vit-base-patch16-224")

gr.Interface.from_pipeline(pipe).launch()
