input_sentence = "Hello, World! Welcome to Python programming."
words = input_sentence.split()
reversed_words = list(reversed(words))
output_sentence = " ".join(reversed_words)
print("Output after reverse =", output_sentence)