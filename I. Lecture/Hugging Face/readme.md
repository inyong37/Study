- [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1) | [KR](https://wikidocs.net/book/8056)


[Soloura](https://huggingface.co/Soloura)

### [Text Generation](https://huggingface.co/tasks/text-generation)

Generating text is the task of producing new text. These models can, for example, fill in incomplete text or paraphrase.

---

## :books: [Docs](https://huggingface.co/docs)

Get Started | Tutorials | :books: Task Guides | Developer Guides | Performance and Scalability | Contribute | Conceptual Guides | API

:pencil2: Natural Language Processing | Audio | :eyes: Computer Vision | Multimodal | Generation | Prompting

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

## :eyes: Computer Vision

### [Image Classification](https://huggingface.co/docs/transformers/tasks/image_classification)

Image classification assigns a label or class to an image. Unlike text or audio classification, the inputs are the pixel values that comprise an image. There are many applications for image classification, such as detecting damage after a natural disaster, monitoring crop health, or helping screen medical images for signs of disease.

### [Semantic Segmentation](https://huggingface.co/docs/transformers/tasks/semantic_segmentation)

Semantic segmentation assigns a label or class to each individual pixel of an image. There are several tpyes of segmentation, and in the case of semantic segmentation, no distinction is made between unique instances of the same object. Both objects are given the same label (for example, "car" instead of "car-1" and "car-2"). Common real-world applications of semantic segmentation include training self-driving cars to identify pedestrians and important traffic information, identify celss and abnormalities in medical imagery, and monitoring environmental changes from satellite imagery.

### [Video Classification](https://huggingface.co/docs/transformers/tasks/video_classification)

Video classification is the task of assigning a label or class to an entire video. Videos are expected to have only one class for each video. Video classification models take a video as input and return a prediction about which class the video belongs to. These models can be used to categorize what a video is all about. A real-world application of video classification is action / activity recognition, which is useful for fitneww applications. It is also helpful for vision-imparied individuals, especially when they are commuting.



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
