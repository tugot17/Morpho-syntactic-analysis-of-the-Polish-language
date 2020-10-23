import re

def get_sentences_from_text(text):
    """
    Function returns a list of words for a given sentence
    :param text: string, e.g. "I go to school. My school is a decent place to go to, unlike yours"
    :return: List[string], e.g. ["I go to school", "My school is a decent place to go to, unlike yours"]
    """
    regex = r"(?<=[.!?])\s+(?=[A-Z])"

    # subst = "\\n\\n"

    # matches = re.findall(regex, text)
    matches = re.finditer(regex, text, re.MULTILINE)

    subst = "\\n\\n"
    subst = ""

    result = re.sub(regex, subst, text, 0, re.MULTILINE)

    return result, list(matches)

if __name__ == '__main__':
    text = "I go to school. My school is a decent place to go to, unlike yours"

    print(get_sentences_from_text(text))