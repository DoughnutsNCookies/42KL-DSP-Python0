import sys


def validate_string(string: str) -> bool:
    """
        Validates the string

        Returns:
            True if the string is valid, else False
    """
    for char in string:
        if not (char.isalpha() or char == ' '):
            return False
    return True


def validate_number(number: str) -> bool:
    """
        Validates the number

        Returns:
            True if the number is valid, else False
    """
    for i, char in enumerate(number):
        if not (char.isdigit()
                or (char == '-' and i == 0 and len(number) > 1)):
            return False
    return True


def validate_input() -> (str, int):
    """
        Validates the input

        Returns:
            text: text and count
    """
    try:
        assert (len(sys.argv)) == 3, "the arguments are bad"
        assert validate_string(sys.argv[1]), "the arguments are bad"
        assert validate_number(sys.argv[2]), "the arguments are bad"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()
    return sys.argv[1], int(sys.argv[2])


def main():
    """
        Validates the input first
        Converts the string to a list
        Use a list comprehension with a lambda function
        Filter words by length
        Prints the results
    """
    string, count = validate_input()
    print([word for word in string.split()
           if (lambda word: len(word) > count)(word)])


if __name__ == "__main__":
    main()
