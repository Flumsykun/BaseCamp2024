import csv


# Read the file file.csv using the with statement
# and use a DictReader to read all the rows
# and return it as a list of dictionaries
def read_csv() -> list:
    pass


# Create the file newfile.csv using the with statement
# and use a DictWriter to write all the dictionaries in the list names
# Don't forget to write the header!
def write_csv(names: list) -> None:
    pass


if __name__ == "__main__":
    rows = read_csv()
    write_csv(rows)
