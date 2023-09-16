from .greet import say_hello
from .functions import add, sub, mul, div, mod


def main():
    """
        To prevent all functions from not being used due to flake8.
    """
    return
    say_hello()
    add(1, 2)
    sub(1, 2)
    mul(1, 2)
    div(1, 2)
    mod(1, 2)


if __name__ == "__main__":
    main()
