def count_vowels(input_string):
    vowels = set("AEIOUaeiou")
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
