import sys

def read_file(input_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        return "Error: File not found or cannot read"

def summarize(text):
    lines = text.split('\n')
    return '\n'.join(lines[:3])

def write_file(output_path, content):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python app.py <input_file> <output_file>")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    text = read_file(input_file)

    if "Error" in text:
        print(text)
        sys.exit()

    summary = summarize(text)
    write_file(output_file, summary)

    print("Done! Summary generated successfully.")