#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def cyr_to_latin(text):
    t = {
        'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    text = text.lower()
    latin_text = ''
    for char in text:
        if char in t:
            latin_text += t[char]
        else:
            latin_text += char
    return latin_text


def replace_chars(chars):
    def decorator(func):
        def wrapper(text):
            for char in chars:
                text = text.replace(char, '-')
            while '--' in text:
                text = text.replace('--', '-')
            return func(text)
        return wrapper
    return decorator


cyr_to_latin = replace_chars("?!:;,. ")(cyr_to_latin)

if __name__ == "__main__":
    text = "Привет, мир! Как дела? --Хорошо,   спасибо! :)"
    result = cyr_to_latin(text)
    print(result)