""
from pathlib import Path

path = Path('siddhartha.txt')
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
 print(line)

def sort_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        sorted_lines = sorted(lines)

        with open(file_path, 'w') as file:
            file.writelines(sorted_lines)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = 'my_file.txt'
sort_file(file_path)