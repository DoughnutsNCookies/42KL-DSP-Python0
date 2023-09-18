import sys


def validate_string(string: str) -> bool:
    """
        Validates the string

        Returns:
            True if the string is valid, else False
    """
    for char in string:
        if not (char.isalnum() or char == ' '):
            return False
    return True


def validate_input() -> str:
    """
        Validates the input

        Returns:
            text: text and count
    """
    try:
        assert (len(sys.argv)) == 2, "the arguments are bad"
        assert validate_string(sys.argv[1]), "the arguments are bad"
    except AssertionError as msg:
        print("AssertionError:", msg)
        exit()
    return sys.argv[1]


def main():
    """
        Validates the input first
    """
    nested_morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': '/',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }
    string = validate_input()
    print(' '.join([nested_morse[char.upper()] for char in string]))


if __name__ == "__main__":
    main()
