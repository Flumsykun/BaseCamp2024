from handle_csv import read_csv, write_csv


names = [
    {"first_name": "Arjen", "last_name": "Lubach"},
    {"first_name": "Diederik", "last_name": "Smit"},
]

content = "first_name,last_name\nArjen,Lubach\nDiederik,Smit\n"


def test_read_csv():
    assert read_csv() == names


def test_write_csv():
    write_csv(names)
    with open("newfile.csv") as txtfile:
        assert txtfile.read() == content
