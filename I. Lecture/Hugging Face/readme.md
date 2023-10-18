- [Hugging Face Course](https://huggingface.co/learn/nlp-course/chapter1/1) | [KR](https://wikidocs.net/book/8056)


[Soloura](https://huggingface.co/Soloura)

### [Text Generation](https://huggingface.co/tasks/text-generation)

Generating text is the task of producing new text. These models can, for example, fill in incomplete text or paraphrase.

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

---

### Reference
- Text Geneartion, https://huggingface.co/tasks/text-generation, 2023-10-18-Wed.
- Text Classification, https://huggingface.co/docs/transformers/tasks/sequence_classification, 2023-10-18-Wed.
- Question Answering, https://huggingface.co/docs/transformers/tasks/question_answering, 2023-10-18-Wed.
- Causal Language Modeling, https://huggingface.co/docs/transformers/tasks/language_modeling, 2023-10-18-Wed.
- Masked Language Modeling, https://huggingface.co/docs/transformers/tasks/masked_language_modeling, 2023-10-18-Wed.
- Translation, https://huggingface.co/docs/transformers/tasks/translation, 2023-10-18-Wed.
- Summarization, https://huggingface.co/docs/transformers/tasks/summarization, 2023-10-18-Wed.
- Multiple Choice, https://huggingface.co/docs/transformers/tasks/multiple_choice, 2023-10-18-Wed.
