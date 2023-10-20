input_string = "Hello, World!"
given_char = "H"
starts_with_char = lambda string, char: string.startswith(char)
result = starts_with_char(input_string, given_char)
print(result)
