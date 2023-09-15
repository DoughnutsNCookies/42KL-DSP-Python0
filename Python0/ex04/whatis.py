import sys

if len(sys.argv) == 1:
    sys.exit(0)


def is_valid(input_str):
    for i, char in enumerate(input_str):
        if not (char.isdigit()
                or (char == '-' and i == 0 and len(input_str) > 1)):
            return False
    return True


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    assert is_valid(sys.argv[1]), "argument is not an integer"
except AssertionError as msg:
    print("AssertionError:", msg)
    sys.exit(1)

print(["I'm Odd.", "I'm Even."][int(sys.argv[1]) % 2 == 0])
