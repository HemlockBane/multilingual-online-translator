import requests
from bs4 import BeautifulSoup
import sys


def get_translation(session, src_lang, target_lang, text):
    base_translation_url = 'https://context.reverso.net/translation/'
    translation_direction = f'{src_lang.lower()}-{target_lang.lower()}/'

    url = f'{base_translation_url}{translation_direction}{text}'
    chrome_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    headers = {
        'user-agent': chrome_user_agent}

    try:
        res = session.get(url, headers=headers)
        # print(f'{res.status_code} {res.reason}', end='\n\n')
        if res.status_code != 200:
            print(f"Sorry, unable to find {text}")
            return
    except requests.exceptions.ConnectionError as e:
        print('Something wrong with your internet connection')
        return

    b_soup = BeautifulSoup(res.content, 'html.parser')

    div_tag = b_soup.find('div', id='translations-content')
    filtered_contents = [i for i in div_tag.contents if i not in ['\n']]
    translations = [i.text.strip() for i in filtered_contents]

    with open(f'{text}.txt', mode='a', encoding='utf-8') as file:
        print('Context examples:', end='\n')
        print('Context examples:', end='\n', file=file)

        print(f'{target_lang.capitalize()} Translations:')
        print(f'{target_lang.capitalize()} Translations:', file=file)

        for v in translations[:5]:
            print(v)
            print(v, file=file)
        print('')
        print('', file=file)

    section_tag = b_soup.find('section', id='examples-content')
    filtered_contents = [i for i in section_tag.contents if i not in ['\n']]
    examples = []
    for v in filtered_contents:
        src = v.find('div', class_='src ltr')
        if src:
            examples.append(src.text)
        trg = v.find('div', class_='trg ltr')
        if trg:
            examples.append(trg.text)
    filtered_examples = [i.strip() for i in examples if i not in ['\n']]
    print(f'{target_lang.capitalize()} Examples:')

    with open(f'{text}.txt', mode='a', encoding='utf-8') as file:
        print(f'{target_lang.capitalize()} Examples:', file=file)
        # print(filtered_examples)

        for i, v in enumerate(filtered_examples[:10], 1):
            print(v)
            print(v, file=file)
            if i % 2 == 0 and i < 10:
                print('')
                print('', file=file)


def run_online_translator():
    supported_langs = ['arabic',
                       'german',
                       'english',
                       'spanish',
                       'french',
                       'hebrew',
                       'japanese',
                       'dutch',
                       'polish',
                       'portuguese',
                       'romanian',
                       'russian',
                       'turkish']

    # print("Hello, welcome to the translator. Translator supports: ")
    # for idx, lang in enumerate(supported_langs, 1):
    #     print(f'{idx}. {lang}')
    # src_lang_idx = int(input('Type the number of your language: '))
    # target_lang_idx = int(
    #     input("Type the number of language you want to translate to or '0' to translate to all languages: "))
    # text = input('Type the word you want to translate:')
    #
    # src_lang = supported_langs[src_lang_idx - 1]

    args = sys.argv

    if len(args) != 4:
        pass

    src_lang = args[1]
    target_lang = args[2]
    text = args[3]

    if target_lang not in supported_langs and target_lang != 'all':
        print(f"Sorry, the program doesn't support {target_lang}")
        return

    # Comment from requests docs: If you’re making several requests to the same host,
    # the underlying TCP connection will be reused, which can result in a significant performance increase
    # (see HTTP persistent connection).
    session = requests.Session()

    if target_lang == 'all':
        for trg_lang in supported_langs:
            if src_lang != trg_lang:
                get_translation(session, src_lang, trg_lang, text)
    else:
        get_translation(session, src_lang, target_lang, text)

    # session = requests.Session()
    #
    # if target_lang_idx == 0:
    #     for trg_lang in supported_langs:
    #         if src_lang != trg_lang:
    #             get_translation(session, src_lang, trg_lang, text)
    # else:
    #     target_lang = supported_langs[target_lang_idx - 1]
    #     get_translation(session, src_lang, target_lang, text)


run_online_translator()
