- [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1) | [KR](https://wikidocs.net/book/8056)


[Soloura](https://huggingface.co/Soloura)

### [Text Generation](https://huggingface.co/tasks/text-generation)

Generating text is the task of producing new text. These models can, for example, fill in incomplete text or paraphrase.

---

## :books: [Docs](https://huggingface.co/docs)

Get Started | Tutorials | :books: Task Guides | Developer Guides | Performance and Scalability | Contribute | Conceptual Guides | API

:pencil2: Natural Language Processing | Audio | :eyes: Computer Vision | :rainbow: Multimodal | :hammer_and_wrench: Generation | Prompting

## :pencil2: Natural Language Processing - Task Guides

### [Text Classification](https://huggingface.co/docs/transformers/tasks/sequence_classification)

Text classification is a common NLP task that assigns a label or class to text. Some of the largest companies run text classification in production for a wide range of practical applications. One of the most popular forms of text classification is sentiment analysis, which assigns a label like positive, negative, or neutral to a sequence of text.

### [Token Classification](https://huggingface.co/docs/transformers/tasks/token_classification)

Token classification assigns a label to individual tokens in a sentence. One of the most common token classification tasks is Named Entity Recognition (NER). NER attempts to find a label for each entity in a sentence, such as a person, location, or organization.

### [Question Answering](https://huggingface.co/docs/transformers/tasks/question_answering)

Question answering tasks return an answer given a question. If you've ever asked a virtual assistant like Alexa, Siri or Google what the weather is, then you've used a questing answering model before. There are two common types of question answering tasks:

* Extractive: extract the answer from the given context.

* Abstractive: generate an answer from the context that correctly answers the question.

### [Causal Language Modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)

Causal language modeling predicts the next token in a sequence of tokens, and the model can only attend to tokens on the left. This means the model cannot see future tokens. GPT-2 is an example of a causal language model.

### [Masked Language Modeling](https://huggingface.co/docs/transformers/tasks/masked_language_modeling)

Masked language modeling predicts a masked token in a sequence, and the model can attend to tokens bidirectionally. This means the model full access to the tokens on the left and right. Masked language modeling is great for tasks that requires a good contextual understandinging of an entire sequence. BERT is an example of a masked language model.

### [Translation](https://huggingface.co/docs/transformers/tasks/masked_language_modeling)

Translation converts a sequence of text from one language to another. It is one of several tasks you can formulate as a sequence-to-sequence problem, a powerful framework for returning some output from an input, like translation or summarization. Translation systems are commonly used for translation between different language texts, but it can also be used for speech or some combination in between like text-to-speech or speech-to-text.

### [Summarization](https://huggingface.co/docs/transformers/tasks/summarization)

Summarization creates a shorter version of a document or an article that captures all the important information. Along with translation, it is another example of a task that can be formulated as a sequence-to-sequence task. Summarization can be:

* Extractive: extract the most relevant information from a document.

* Abstractive: generate new text that captures the most relevant information.

### [Multiple Choice](https://huggingface.co/docs/transformers/tasks/multiple_choice)

A multiple choice task is similar to question answering, except several candidate answers are provided along with a context and the model is trained to select the correct answer.

## :eyes: Computer Vision - Task Guides

### [Image Classification](https://huggingface.co/docs/transformers/tasks/image_classification)

Image classification assigns a label or class to an image. Unlike text or audio classification, the inputs are the pixel values that comprise an image. There are many applications for image classification, such as detecting damage after a natural disaster, monitoring crop health, or helping screen medical images for signs of disease.

### [Semantic Segmentation](https://huggingface.co/docs/transformers/tasks/semantic_segmentation)

Semantic segmentation assigns a label or class to each individual pixel of an image. There are several tpyes of segmentation, and in the case of semantic segmentation, no distinction is made between unique instances of the same object. Both objects are given the same label (for example, "car" instead of "car-1" and "car-2"). Common real-world applications of semantic segmentation include training self-driving cars to identify pedestrians and important traffic information, identify celss and abnormalities in medical imagery, and monitoring environmental changes from satellite imagery.

### [Video Classification](https://huggingface.co/docs/transformers/tasks/video_classification)

Video classification is the task of assigning a label or class to an entire video. Videos are expected to have only one class for each video. Video classification models take a video as input and return a prediction about which class the video belongs to. These models can be used to categorize what a video is all about. A real-world application of video classification is action / activity recognition, which is useful for fitneww applications. It is also helpful for vision-imparied individuals, especially when they are commuting.

### [Object Detection](https://huggingface.co/docs/transformers/tasks/object_detection)

Object detection is the computer vision task of detecting instances (such as humans, buildings, or cars) in an image. Object detection models receive an image as input and output coordinates of the bounding boxes and associated labels of the detected objects. An image can contain multiple objects, each with its own bounding box and a label (e.g. it can have a car and a building), and each object can be present in different parts of an image (e.g. the image can have several cars). This task is commonly used in autonomous driving for detecting things like pedestrians, road signs, and traffic lights. Other applications include counting objects in images, image search, and more.

### [Zero-shot Object Detection](https://huggingface.co/docs/transformers/tasks/object_detection)

Traditionally, models used for object detection require labeled image datasets for training, and are limited to detecting the set of classes from the training data.

Zero-shot object detection is supported by the OWL-ViT model which uses a different approach. OWL-ViT is an open-vocabulary object detector. It means that it can detect objects in images based on free-text queries without the need to fine-tune the model on labeled datasets.

OWL-ViT leverages multi-model representations to perform open-vocabulary detection. It combines CLIP with lightweight object classification and localization heads. Open-vocabulary detection is achieved by embedding free-text queries with the text encoder of CLIP and using them as input to the object classification and localization heads. Associate images and their corresponding textual descriptions, and ViT processes iamge patches as inputs. The authors of OWL-ViT first trained CLIP from scratch and then fine-tuned OWL-ViT end to end on standard object detection datasets using a bipartite matching loss.

With this approach, the model can detect objects based on textual descriptions without prior training on labeled datasets.

### [Zero-shot Image Classification](https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification)

Zero-shot image classification is a task that involves classifying images into different categories using a model that was not explicitly trained on data containing labeled examples from those specific categories.

Traditionally, image classification requires training a model on a specific set of labeled images, and this model learns to "map" certain image features to labels. When there's a need to use such model for a classification task that introduces a new set of labels, fine-tuning is required to "recalibrate" the model.

In contrast, zero-shot or open vocabulary image classification models are typcially multimodal models that have been trained on a large dataset of images and associated descriptions. These models learn aligned vision-language representations that can be used for many downstream tasks including zero-shot image classification.

This is a more flexible approach to image classification that allows models to generalize to new and unseen categories without the need for additional training data and enables users to query images with free-form text descriptions of their target objects.

### [Monocular Depth Estimation](https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation)

Monocular depth estimation is a computer vision task that involves predicting the depth information of a scene from a single image. In other words, it is the process of estimating the distance of objects in a scene from a single camera viewpoint.

Monocular depth estimation has various applications, including 3D reconstruction, augmented reality, autonomous driving, and robotics. It is a challenging task as it requires the model to understand the complex relationships between objects in the scene and the corresponding depth information, which can be affected by factors such as lighting conditions, occlusion, texture.

## :rainbow: Multimodal - Task Guides

### [Image Captioning](https://huggingface.co/docs/transformers/tasks/image_captioning)

Image captioning is the task of predicting a caption for a given image. Common real world applications of it include aiding visually impaired people that can help them navigate through different situations. Therefore, image captioning helps to improve content accessibility for people for describing images to them.

### [Document Question Answering](https://huggingface.co/docs/transformers/tasks/document_question_answering)

Document Question Answering, also referred to as Document Visual Question Answering, is a task that involves providing answers to questions posed about document images. The input to models supporting this task is typically a combination of an image and a question, and the output is an answer expressed in natural language. These models utilize multiple modalities, including text, the positions of words (bounding boxes), and the image itself.

### [Visual Question Answering](https://huggingface.co/docs/transformers/tasks/visual_question_answering)

Visual Question Answering (VQA) is the task of answering open-ended questions based on an image. The input to models supporting this task is typically a combination of an image and a question, and the output is an answer expressed in natural language.

Some noteworthy use case examples for VQA include:

* Accessibility applications for visually impaired individuals

* Education: posting questions about visual materials presented in lectures or textbooks. VQA can also be utilized in interactive museum exhibits or historical sites.

* Customer service and e-commerce: VQA can enhance user experience by letting users ask questions about products.

* Image retrieval: VQA models can be used to retrieve images with specific characteristic. For example, the user can ask "Is there a dog?" to find all images with dogs from a set of images.

### [Text to Speech](https://huggingface.co/docs/transformers/tasks/text-to-speech)

Text-to-speech (TTS) is the task of creating natural-souding speech from text, where the speech can be generated in multiple languages and for multiple speakers. Several text-to-speech models are currently available in Transformers, such as Bark, MMS, VITS and SpeechT5.

You can easily generate audio using the "text-to-audio" pipeline (or its alias - "text-to-speech"). Some models, like Bark, can also be conditioned to generate non-verbal communications such as laughing, sighing and crying, or even add music. Here's an example of how you would use the "text-to-speech" pipeline with Bark:

```Python
>>> from transformers import pipeline

>>> pipe = pipeline("text-to-speech", model="suno/bark-small")
>>> text = "[clears throat] This is a test ...  and I just took a long pause."
>>> output = pipe(text)
```

Here's a code snippet you can use to listen to the resulting audio on a notebook:

```Python
>>> from IPython.display import Audio
>>> Audio(output["audio"], rate=output["sampling_rate"])
```

## :hammer_and_wrench: Generation

### [Text Generation Strategies](https://huggingface.co/docs/transformers/generation_strategies)

Text generation is essential to many NLP tasks, such as open-ended text generation, summarization, translation, and more. It also plays a role in a variety of mixed-modality applications that have text as an output like speech-to-text and vision-to-text. Some of the models that can generate text include GPT2, XLNet, OpenAI GPT, CTRL, TransformerXL, XLM, Bart, T5, GIT, Whisper.

Check out a few examples that use generate() method to produce text outputs for different tasks:

* Text summarization
* Image captioning
* Audio transcription

Note that the inputs to the generate method depend on the model's modality. They are returned by the model's preprocessor class, such as AutoTokenizer or AutoProcessor. If a model's preprocessor creates more than one kind of input, pass all the inputs to generate(). You can learn more about the individual model's preprocessor in the corresponding model's documentation.

The process of selecting output tokens to generate text is known as decoding, and you can customize the decoding strategy that the generate() method will use. Modifiying a decoding strategy does not change the values of any trainable parameters. However, it can have a noticeable impact on the quality of the generated output. It can help reduce repetition in the text and make it more coherent

---

### Reference
- Docs, https://huggingface.co/docs, 2023-10-18-Wed.
- Text Geneartion, https://huggingface.co/tasks/text-generation, 2023-10-18-Wed.
- Text Classification, https://huggingface.co/docs/transformers/tasks/sequence_classification, 2023-10-18-Wed.
- Question Answering, https://huggingface.co/docs/transformers/tasks/question_answering, 2023-10-18-Wed.
- Causal Language Modeling, https://huggingface.co/docs/transformers/tasks/language_modeling, 2023-10-18-Wed.
- Masked Language Modeling, https://huggingface.co/docs/transformers/tasks/masked_language_modeling, 2023-10-18-Wed.
- Translation, https://huggingface.co/docs/transformers/tasks/translation, 2023-10-18-Wed.
- Summarization, https://huggingface.co/docs/transformers/tasks/summarization, 2023-10-18-Wed.
- Multiple Choice, https://huggingface.co/docs/transformers/tasks/multiple_choice, 2023-10-18-Wed.
- Image Classification, https://huggingface.co/docs/transformers/tasks/image_classification, 2023-10-18-Wed.
- Semantic Segmentation, https://huggingface.co/docs/transformers/tasks/semantic_segmentation, 2023-10-18-Wed.
- Video Classification, https://huggingface.co/docs/transformers/tasks/video_classification, 2023-10-18-Wed.
- Object Detection, https://huggingface.co/docs/transformers/tasks/object_detection, 2023-10-18-Wed.
- Zero-shot Object Detection, https://huggingface.co/docs/transformers/tasks/zero_shot_object_detection, 2023-10-18-Wed.
- Zero-shot Image Classification, https://huggingface.co/docs/transformers/tasks/zero_shot_image_classification, 2023-10-18-Wed.
- Monocular Depth Prediction, https://huggingface.co/docs/transformers/tasks/monocular_depth_estimation, 2023-10-18-Wed.
- Image Captioning, https://huggingface.co/docs/transformers/tasks/image_captioning, 2023-10-18-Wed.
- Document Question Answering, https://huggingface.co/docs/transformers/tasks/document_question_answering, 2023-10-18-Wed.
- Visual Question Answering, https://huggingface.co/docs/transformers/tasks/visual_question_answering, 2023-10-18-Wed.
- Text to Speech, https://huggingface.co/docs/transformers/tasks/text-to-speech, 2023-10-18-Wed.
- Text Generation Strategies, https://huggingface.co/docs/transformers/generation_strategies, 2023-10-19-Thu.
