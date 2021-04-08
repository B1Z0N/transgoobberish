from google_trans_new import google_translator
from progressbar import progressbar

from random import shuffle, randint


LANGUAGES = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

with open('in.txt') as f:
    txt = f.read()

lang_num = int(input(f'Enter the number of languages you would like to translate your text to before returning to your main language(there are up to {len(LANGUAGES)} languages): '))
translator = google_translator()

src_lang = translator.detect(txt)[0]
is_right_src = input(f'Detected source language is "{src_lang}". Is it true? [Y/n] ').lower()
if is_right_src != 'y' and is_right_src != '':
    src_lang = input('Enter input lang in short format("en" for english): ').lower()

langs = LANGUAGES.copy()
shuffle(langs)
langs = [src_lang, *langs[:lang_num], src_lang]

for i in progressbar(range(len(langs) - 1)):
    txt = translator.translate(txt, lang_src=langs[i], lang_tgt=langs[i + 1])

print('The result is: ', end='\n\n')
print(txt, end='\n\n')
print('Your text have made it through this: \n' + ' -> '.join(langs), end='\n\n')

