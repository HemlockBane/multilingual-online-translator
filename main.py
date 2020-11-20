import requests
from bs4 import BeautifulSoup

lang_codes = {'en': 'english', 'fr': 'french'}

target_lang = input(
    'Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
text = input('Type the word you want to translate:')
print(f'You chose "{target_lang}" as the language to translate "{text}".')

src_lang = 'en'
if target_lang == 'en':
    src_lang = 'fr'

base_translation_url = 'https://context.reverso.net/translation/'
translation_direction = f'{lang_codes[src_lang]}-{lang_codes[target_lang]}/'

url = f'{base_translation_url}{translation_direction}{text}'
chrome_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {
    'user-agent': chrome_user_agent}

res = requests.get(url, headers=headers)
print(f'{res.status_code} {res.reason}')
b_soup = BeautifulSoup(res.content, 'html.parser')

div_tag = b_soup.find('div', id='translations-content')
filtered_contents = [i for i in div_tag.contents if i not in ['\n']]
translations = [i.text.strip() for i in filtered_contents]

print('Translations', translations, sep='\n')

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
print(filtered_examples)
