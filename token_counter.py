import re

def count_tokens(text):
    tokens = re.findall(r'\b\w+\b', text)
    return len(tokens)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    return text.count('.') + text.count('!') + text.count('?')

if __name__ == "__main__":
    sample_text = "This is a sample text. It has two sentences!"
    print(count_tokens(sample_text))
    print(count_words(sample_text))
    print(count_sentences(sample_text))
