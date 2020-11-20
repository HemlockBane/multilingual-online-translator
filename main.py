import requests
from bs4 import BeautifulSoup

lang_codes = {'en': 'english', 'fr': 'french'}

supported_langs = ['Arabic',
                   'German',
                   'English',
                   'Spanish',
                   'French',
                   'Hebrew',
                   'Japanese',
                   'Dutch',
                   'Polish',
                   'Portuguese',
                   'Romanian',
                   'Russian',
                   'Turkish']

print("Hello, you're welcome to the translator. Translator supports: ")
for idx, lang in enumerate(supported_langs, 1):
    print(f'{idx}. {lang}')
src_lang_idx = int(input('Type the number of your language: '))
target_lang_idx = int(input('Type the number of language you want to translate to: '))
text = input('Type the word you want to translate:')

src_lang = supported_langs[src_lang_idx - 1]
target_lang = supported_langs[target_lang_idx - 1]

base_translation_url = 'https://context.reverso.net/translation/'
translation_direction = f'{src_lang.lower()}-{target_lang.lower()}/'

url = f'{base_translation_url}{translation_direction}{text}'
chrome_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {
    'user-agent': chrome_user_agent}

# print(url)

res = requests.get(url, headers=headers)
print(f'{res.status_code} {res.reason}', end='\n\n')
b_soup = BeautifulSoup(res.content, 'html.parser')

div_tag = b_soup.find('div', id='translations-content')
filtered_contents = [i for i in div_tag.contents if i not in ['\n']]
translations = [i.text.strip() for i in filtered_contents]

print('Context examples:', end='\n\n')
print(f'{target_lang} Translations:')
for v in translations[:5]:
    print(v)
print('')

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
print(f'{target_lang} Examples:', sep='\n')
# print(filtered_examples)
for i, v in enumerate(filtered_examples[:10], 1):
    print(v)
    if i % 2 == 0 and i < 10:
        print('')
