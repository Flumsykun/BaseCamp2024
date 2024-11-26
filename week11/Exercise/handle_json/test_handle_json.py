from handle_json import (
    json_to_data,
    data_to_json,
    read_file_as_data_with_json_load,
    read_file_as_data_with_json_loads,
    write_json_file_with_json_dumps,
    write_json_file_with_json_dump,
)

content = """[
    {
        "name": "Arjen",
        "languages": [
            "Engels",
            "Spaans"
        ]
    },
    {
        "name": "Diederik",
        "languages": [
            "Engels",
            "Duits"
        ]
    }
]"""

compact = (
    '[{"name": "Arjen", "languages": ["Engels", "Spaans"]}, {"name": "Diederik", "languages": ["Engels", "Duits"]}]'
)

data = [
    {"name": "Arjen", "languages": ["Engels", "Spaans"]},
    {"name": "Diederik", "languages": ["Engels", "Duits"]},
]


def test_json_to_data():
    assert json_to_data(content) == data


def test_data_to_json():
    assert data_to_json(data) == compact


def test_read_file_as_data_with_json_loads():
    assert read_file_as_data_with_json_loads() == data


def test_read_file_as_data_with_json_load():
    assert read_file_as_data_with_json_load() == data


def test_write_json_file_with_json_dumps():
    write_json_file_with_json_dumps(data)
    with open("newfile.json", "r") as jsonfile:
        assert jsonfile.read() == content


def write_json_file_with_json_dump(data: list):
    write_json_file_with_json_dump(data)
    with open("newfile.json", "r") as jsonfile:
        assert jsonfile.read() == content
