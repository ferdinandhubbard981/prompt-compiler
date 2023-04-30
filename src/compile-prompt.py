import argparse
import re
import os

def read_file_content(base_path, filepath):
    abs_path = os.path.join(base_path, filepath)
    with open(abs_path, "r") as file:
        return file.read()

def replace_filepaths_with_content(base_path, input_text):
    pattern = r"\{(.+?)\}"
    result = re.sub(pattern, lambda match: read_file_content(base_path, match.group(1)), input_text)
    return result

def main(input_file, output_file):
    with open(input_file, "r") as file:
        input_text = file.read()

    base_path = os.path.dirname(input_file)
    output_text = replace_filepaths_with_content(base_path, input_text)

    with open(output_file, "w") as file:
        file.write(output_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace {filepath} with file content")
    parser.add_argument("--input", type=str, required=True, help="Path to the input text file")
    parser.add_argument("--output", type=str, required=True, help="Path to the output text file")

    args = parser.parse_args()

    main(args.input, args.output)
