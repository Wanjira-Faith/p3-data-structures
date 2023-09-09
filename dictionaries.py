# Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 

# sample input = 

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)


import string

def word_frequency(sentence):
    # Initialize a dictionary to store word frequencies
    word_freq = {}
    
    # Remove punctuation and split the sentence into words
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).lower().split()
    
    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq


sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
