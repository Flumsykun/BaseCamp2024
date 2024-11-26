import json


# Transform the string content from JSON into a list
# and return that list
def json_to_data(content: str) -> list:
    pass


# Transform the list data into a JSON string
# and return that string
def data_to_json(data: list) -> str:
    pass


# Read the file file.json and transform the JSON content into a list with json.loads
# and return that list
def read_file_as_data_with_json_loads() -> list:
    pass


# Read the file file.json with json.load as a list and
# and return that list
def read_file_as_data_with_json_load() -> list:
    pass


# Transform the list data into a JSON string with json.dumps
# and write that string to file newfile.json
# Don't forget to use 4 spaces as indent
def write_json_file_with_json_dumps(data: list):
    pass


# Open the file newfile.json
# and write the transformed list data as a JSON string with json.dump
# Don't forget to use 4 spaces as indent
def write_json_file_with_json_dump(data: list):
    pass
