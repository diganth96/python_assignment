# Open the file for reading
file_name = "demo.txt"

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print(f'Total number of lines in {file_name}: {line_count}')
except FileNotFoundError:
    print(f'File not found: {file_name}')
except Exception as e:
    print(f'An error occurred: {str(e)}')