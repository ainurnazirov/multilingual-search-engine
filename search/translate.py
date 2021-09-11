import requests

def translate_tr(text):
    url_translate = 'https://translate.tatar/translate?lang=1&text={}'
    text = text.replace(';', ',')
    text_t = requests.get(url_translate.format(text)).text
    if text_t.startswith('<res>'):
        b = text_t.find('<mt>') + 4
        e = text_t.find('</mt>')
        text_t = text_t[b:e]
    if text_t.startswith('<!DOCTYPE'):
        text_t = text

    return text_t

def translate_rt(text):
    url_translate = 'https://translate.tatar/translate?lang=0&text={}'
    text = text.replace(';', ',')
    text_t = requests.get(url_translate.format(text)).text
    if text_t.startswith('<res>'):
        b = text_t.find('<mt>') + 4
        e = text_t.find('</mt>')
        text_t = text_t[b:e]
    if text_t.startswith('<!DOCTYPE'):
        text_t = text

    return text_t
