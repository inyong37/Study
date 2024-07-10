# [Transformers](https://huggingface.co/docs/transformers/en/index)

State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX.

Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as: Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation; Computer Vision: image classification, object detection, and segmentation; Audio: automatic speech recognition and audio classification; Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classificatin, and visual question answering.

Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model's life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.

## Quick Tour

| Task | Description | Modality | Pipeline identifier |
|:-|:-|:-|:-|
| Text classification | assign a label to a given sequence of text | NLP | `pipeline(task='sentiment-analysis')` |
| Text generation | generate text given a prompt | NLP | `pipeline(task='text-generation')` |
| Summarization | generate a summary of a sequence of text or document | NLP | `pipeline(task='summarization')` |
| Image classification | assign a label to an image | Computer vision | `pipeline(task='image-classification')` |
| Image segmentation | assign a label to each individual pixel of an image (supports semantic, panoptic, and instance segmentation) | Computer vision | `pipeline(task='image-segmentation')` |
| Object detection | predict the bounding boxes and classes of objects in an image | Computer vision | `pipeline(task='object-detection')` |
| Audio classification | assign a label to some audio data | Audio | `pipeline(task='audio-classification')` |
| Automatic speech recognition | transcribe speech into text | Audio | `pipeline(task='automatic-speech-recognition')` |
| Visual question answering | answer a question about the image, given an image and a question | Multimodal | `pipeline(task='vqa')` |
| Document question answering | answer a question about the document, given a document and a question | Multimodal | `pipeline(task='document-question-answering')`
| Image captioning | generate a caption for a given image | Multimodal | `pipeline(task='image-to-text')` |

---

### Reference
- Transformers, https://huggingface.co/docs/transformers/en/index, 2024-07-10-Wed.
