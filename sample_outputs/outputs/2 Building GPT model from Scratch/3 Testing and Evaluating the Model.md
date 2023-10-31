# Testing and Evaluating the Model

Now that we have established our GPT model and trained it, it's time to evaluate our model's performance. It is necessary to ensure that our model is correctly understanding the sequence and generating appropriate outputs.

## Evaluation Metrics

There are several ways to evaluate the performance of a GPT model, but the two most common are:

1. **Perplexity:**
Perplexity is commonly used to evaluate language models. It measures how well a model predicts a sample and is a good indication of its precision. The lower the perplexity, the better the performance of the language model.

2. **BLEU score:**
BLEU (Bilingual Evaluation Understudy) score is used in machine translation tasks. It measures how close a machine translation output is to a set of human translator references. The closer the BLEU score is to 1, the more the two sequences are alike.

## Model Testing

Testing involves running the model on a set of inputs for which we know the outputs, and then comparing the model's predictions to these known values. This will help us understand how accurate our model is in making predictions.

Lets split our dataset into train data and test data. Following this, we'll evaluate our model on the test data.

~~~python
from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(dataset, test_size = 0.2)
~~~

## Model Evaluation

~~~python
# Perplexity on Test Data
def evaluate_perplexity(model, test_data):
    total_log_prob = 0
    total_tokens = 0

    for sentence in test_data:
        tokens = tokenizer.EncodeAsIds(sentence).tokenization
        total_tokens += len(tokens)

        input_tokens = tokens[:-1] # all tokens excluding the last one
        target_tokens = tokens[1:] # all tokens excluding the first one

        with torch.no_grad(): 
            outputs = model(torch.tensor(input_tokens).unsqueeze(0))
            predictions = outputs[0]

        total_log_prob += criterion(predictions.squeeze(0), torch.tensor(target_tokens)).item()

    perplexity = math.exp(total_log_prob / total_tokens)

    return perplexity

print('Test Perplexity: ', evaluate_perplexity(model, test_data))
~~~

## Conclusion

Test results and evaluation metrics provide insights into our model's understanding and performance. In turn, these valuable pieces of information help us refine and optimize our GPT model moving forward. The key in testing and evaluating is to maintain consistent measures to get a clearer picture of how our model improves over time. 

In the following module, we'll move forward to provide fine-tuning of your GPT model for better and efficient outputs.