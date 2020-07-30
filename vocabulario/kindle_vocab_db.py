import requests
import sqlite3
import sys

def request_dict(lang_code, word):
    # lang_code (string): language code. Ex: es, en, etc...
    # word (string): word that will be searched in the dictionary.
    # searches the word in a dictionary. Returns definitions and examples.

    url = f"https://api.dictionaryapi.dev/api/v2/entries/{lang_code}/{word}"
    r = requests.get(url).json()

    # print(r)
    definitions = r[0]['meanings'][0]['definitions']
    
    count = 1
    for d in definitions:
        print(str(count))
        count += 1
        print(d['definition'])
        try:
            print(d['example'])
        except KeyError:
            pass
        print('------------')

def importdb(db):
    # Read .db file with vocab words
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("SELECT word_key FROM LOOKUPS;")
    for item in cursor.fetchall():
        yield item[0].lower()

def explore_vocab(word_generator):
    count = 1
    words_list = []
    for item in word_generator:
        lang_code, word = item.split(':') 
        words_list.append(item.split(':'))
        print(count, word)
        count += 1
        if count % 20 == 0:
            print('Press enter to see next batch of words')
            choice = input()
            if choice != '':
                try:
                    choice = int(choice) - 1
                    print('Definitions of', words_list[choice][1])
                    print('------------')
                    request_dict(words_list[choice][0], words_list[choice][1])
                    print('Press enter')
                    input() 
                except ValueError:
                    print('Invalid number')
                    break


if __name__ == '__main__':
    db = sys.argv[1]
    word_generator = importdb(db)
    explore_vocab(word_generator)