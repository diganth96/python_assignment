def jtoi(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        corrected_content = content.replace('J', 'I')
        print(corrected_content)
    except FileNotFoundError:
        print(f'File not found: {file_name}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
file_name = "words.txt"
jtoi(file_name)