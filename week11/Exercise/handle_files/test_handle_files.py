from handle_files import (
    read_file_using_open,
    read_file_using_with,
    read_second_line,
    read_second_line_without_new_line,
    read_lines_using_for_loop,
    read_lines_using_readlines,
    write_line_to_a_file,
    write_lines_to_a_file,
    add_line_to_a_file,
)

line_one = "This is the first line."
line_two = "This is the second line."
line_three = "This is the third line."
lines_without_new_lines = [line_one, line_two, line_three]
lines_with_new_lines = [line_one + "\n", line_two + "\n", line_three]
content = "\n".join(lines_without_new_lines)


def test_read_file_using_open() -> str:
    assert read_file_using_open() == content


def test_read_file_using_with():
    assert read_file_using_with() == content


def test_read_second_line():
    assert read_second_line() == line_two + "\n"


def test_read_second_line_without_new_line():
    assert read_second_line_without_new_line() == line_two


def test_read_lines_using_for_loop():
    assert read_lines_using_for_loop() == lines_with_new_lines


def test_read_lines_using_readlines():
    assert read_lines_using_readlines() == lines_with_new_lines


def test_write_line_to_a_file():
    write_line_to_a_file("Hello")
    with open("newfile.txt") as inputfile:
        assert inputfile.read() == "Hello"


def test_write_lines_to_a_file():
    write_lines_to_a_file(["Hello", "world"])
    with open("newfile.txt") as inputfile:
        assert inputfile.read() == "Hello\nworld"


def test_add_line_to_a_file():
    with open("newfile.txt", "w") as outputfile:
        outputfile.write("Hello\n")
    add_line_to_a_file("world")
    with open("newfile.txt") as inputfile:
        assert inputfile.read() == "Hello\nworld"
