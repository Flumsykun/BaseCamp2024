def unique_chars_dict(chars):
    unique_chars = {}
    for char in chars:
        unique_chars[char] = 1
    return len(unique_chars)


def unique_chars_set(chars):
    return len(set(chars))


def main():
    chars = input("Please enter a string: ")  # Added a prompt here
    print(f"Unique characters (dict): {unique_chars_dict(chars)}")
    print(f"Unique characters (set): {unique_chars_set(chars)}")


if __name__ == "__main__":
    main()
