# Introduction to GPT

Generalized Pretraining Transformer, more commonly known as GPT, is an innovative model in the realm of language processing AI. With an interface built on the principles of machine learning algorithms, GPT provides a framework for constructing more efficient and versatile language models.

## What is GPT?

GPT is based on the transformer model, an attention-based model that processes input text as a whole, unlike the previous sequential processing methods used in RNNs and LSTMs. Built by OpenAI, GPT is designed to generate fluent and coherent text by predicting the next word in a sequence, using the context from the preceding words.

In other words, it learns to predict the future based on the past. GPT achieves this by using a transformer-based architecture where all the inputs are processed concurrently, unlike the traditional sequential processing. Thus, it significantly enhances the speed and efficiency of language processing tasks.

## GPT's Architecture

GPT utilizes the transformer model, but it only uses the decoder part of the transformer. The architecture comprises of stacked transformer decoders, and the number of stacked decoders usually defines the version of GPT. For instance, **GPT-1** has 12 stacked transformer decoders, **GPT-2** has 48 layers and the latest **GPT-3** contains 175 billion parameters making it the largest among its kind.

Each transformer in GPT takes in an input sequence and gives out an output sequence of the same length. This allows GPT to be trained as a language model by setting up a prediction task where the model needs to predict the i-th token in the sequence based upon the tokens before i.

## How GPT Differs from Other Models?
Many other models require task-specific architectures for effective functioning. However, GPT stands out as it eliminates task-specific architectures and could be effectively employed for multiple tasks without modifications. This introduces flexibility and adaptability to GPT, which differentiates itself from other language processing models.

In comparison to other popular models like BERT, GPT is trained as a causal language model, predicting each token conditioned on the previous ones in the sequence whereas BERT uses a bidirectional model that has information from both the preceding and following tokens.

That all contributes to its proficiency in generating full length human-like paragraphs with great coherency, making it an exceptional model for tasks like language translation, semantic understanding, summarization, and even creating human-like text!

In the next module, we will examine how GPT employs transfer learning and the benefits derived from it. With an in-depth understanding of the GPT model, we will be able to better appreciate the power and potential of this novel AI design.