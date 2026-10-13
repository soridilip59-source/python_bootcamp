# Homework - Finding the Longest Word



# You have a list of words. Use the max function with a lambda key based on string length to find the longest word in the list.

words = ["apple", "banana", "cherry", "date", "elderberry"] 

longest_word = max(words, key=lambda word: len(word))
print(longest_word)