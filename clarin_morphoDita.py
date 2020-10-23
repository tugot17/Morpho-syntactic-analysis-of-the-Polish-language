import xml.etree.ElementTree as ET
import json
import requests


def get_word_base_and_tag(text):
    clarinpl_url = "http://ws.clarin-pl.eu/nlprest2/base"
    user_mail = "demo2019@nlpday.pl"

    url = clarinpl_url + "/process"
    lpmn = "morphoDita"

    payload = {'text': text, 'lpmn': lpmn, 'user': user_mail}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    ccl = r.content.decode('utf-8')
    tree = ET.fromstring(ccl)

    return [[orth.text, base.text, ctag.text] for orth, base, ctag in zip(tree.iter('orth'), tree.iter('base'), tree.iter('ctag'))]

if __name__ == '__main__':
    text = """A mogę, bo moim zdaniem jest do niczego. I to delikatnie mówiąc... Rzecz gustu :) Ja sobie z przyjemnością obejrzałam wczoraj "Live and Let Die". Nareszcie bez Connery'ego!!! Pasuje. Najbardziej ze wszystkich. Może trochę za ładny, ale grą pasuje. IMHO. A Connery to nie święta krowa ;)"""

    print(get_word_base_and_tag(text))


