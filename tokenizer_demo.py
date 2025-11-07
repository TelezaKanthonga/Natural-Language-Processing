# Simple NLP Tokenization Example
# by Teleza Kanthonga

from tensorflow.keras.preprocessing.text import Tokenizer

# A small and simple set of sentences
sentences = [
    "I like apples",
    "I like bananas",
    "You like apples too",
    "He loves fruits"
]

# Create a tokenizer object
tokenizer = Tokenizer(num_words=100, oov_token="<OO)

# Fit the tokenizer on the sentences
tokenizer.fit_on_texts(sentences)

# Get the word index dictionary
word_index = tokenizer.word_index

# Print the word index
print("Word Index (vocabulary):")
print(word_index)
