import textwrap


def clean_up(string: str) -> str:
    return textwrap.dedent(string.rstrip()).strip()


def escape_characters(string):
    string = clean_up(string)
    string = string.translate(str.maketrans({"'": r"\'", '"': r"\""}))
    return str(string)
