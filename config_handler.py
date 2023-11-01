import configparser

def save_config(keystrokes, words, typed_words):
    config = configparser.ConfigParser()
    config['Metrics'] = {'Keystrokes': str(keystrokes), 'Words': str(words), 'TypedWords': str(typed_words)}
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    try:
        keystrokes = int(config['Metrics']['Keystrokes'])
        words = int(config['Metrics']['Words'])
        typed_words = int(config['Metrics']['TypedWords'])
    except KeyError:
        keystrokes, words, typed_words = 0, 0, 0
    
    return keystrokes, words, typed_words
