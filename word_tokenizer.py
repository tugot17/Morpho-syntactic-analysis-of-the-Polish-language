import re

def get_words_from_sentence(text):
    """
    Function returns a list of words for a given sentence
    :param text: string, e.g. "etc. I go to school. I really like it."
    :return: List[string], e.g. ["etc", "I", "go" "to, "school", "I", "really", "like", "it"]
    """
    regex = r"(\()?(\b[^\s]+\b)((?<=\.\w).)?(\,)?(\:)?(\))?"

    matches = re.findall(regex, text, re.MULTILINE)

    return [m[1] for m in matches]


if __name__ == '__main__':
    text = "etc. I go to school. I really like it."

    print(get_words_from_sentence(text))