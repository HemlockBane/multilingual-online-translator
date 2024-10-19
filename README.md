# Multilingual Online Translator

This is a command-line tool that scrapes translations and contextual examples for a word or phrase from **Reverso Context** using `requests` and `BeautifulSoup`. The script can translate between various supported languages and output the translation and examples in a text file.

## Features
- **Translate Words or Phrases**: Translates between supported languages using Reverso Context.
- **Contextual Examples**: Fetches real-world sentence examples showing how the word/phrase is used.
- **Batch Translation**: Option to translate a word/phrase into all supported languages.
- **Efficient Requests**: Uses session reuse for faster multiple requests to the same server.

## Supported Languages
- Arabic
- German
- English
- Spanish
- French
- Hebrew
- Japanese
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Turkish

## Prerequisites
Ensure you have the following Python libraries installed:

```bash
pip install requests beautifulsoup4
```

## Usage

To use the script, run it with the following arguments:

```bash
python translator.py <source_language> <target_language> <word_or_phrase>
```

For example, to translate "hello" from English to French:

```bash
python translator.py english french hello
```

### Translate to All Supported Languages

You can translate a word or phrase into all available languages by using `all` as the target language:

```bash
python translator.py english all hello
```

### Output

The translations and contextual examples will be saved in a text file named after the word being translated (e.g., `hello.txt`).

## Example

To translate the word "apple" from English to French:

```bash
python translator.py english french apple
```

The script will:
- Fetch translations of the word "apple" in French.
- Retrieve sentence examples from Reverso Context.
- Save these translations and examples in `apple.txt`.

## Error Handling
- If a translation is not found or there’s an issue with the network connection, an error message will be shown.
- If you provide an unsupported language, the program will notify you.

## Future Improvements
- Add support for additional languages.
- Develop a GUI for easier use.
- Improve handling of multi-word phrases.
