import json
import argparse


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as data_file:
        ugly_data = json.load(data_file)
    return ugly_data


def pretty_print_json(ugly_data):
    pretty_json = json.dumps(
        ugly_data,
        ensure_ascii=False,
        sort_keys=True,
        indent=4
    )
    print(pretty_json)
    return pretty_json


def write_to_file(filepath, pretty_data):
    with open(filepath, encoding='utf-8', mode='w+') as output_file:
        output_file.write(pretty_data)


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Input and output files"
    )
    parser.add_argument(
        "input_file",
        help="Input path to the input file"
    )
    parser.add_argument(
        "output_file",
        nargs='?',
        help="Input path to the output file"
    )
    arguments = parser.parse_args()
    return arguments

def main():
    arguments = get_parser_args()
    if arguments.input_file is None:
        exit("Error: You did not enter paths to the input and output files!")
    try:
        json_data = load_data(arguments.input_file)
    except FileNotFoundError:
        exit("Error: file or path '{0}' not found!\n".format(arguments.input_file))
    except json.JSONDecodeError:
        exit("Error: this is not json-file!")
    pretty_json_data = pretty_print_json(json_data)
    if arguments.output_file is not None:
        write_to_file(arguments.output_file, pretty_json_data)


if __name__ == "__main__":
    main()
