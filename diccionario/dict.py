import requests
import sys

def request_dict(lang_code, word):
    # lang_code (string): language code. Ex: es, en, etc...
    # word (string): word that will be searched in the dictionary.

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

if __name__ == '__main__':
    words_file = sys.argv[1]
    print('Write the number of the word you want to search')
    words_list = []
    with open(words_file, 'r', encoding='utf-8') as file:
        count = 1
        for line in file:
            if line != '\n':
                words_list.append(line.lower().replace('\n', '').split(':'))
                print(count, line.split(':')[1].lower(), end='')
                count += 1
                if count % 20 == 0:
                    print('Press enter to see next batch of words')
                    choice = input()
                    if choice != '':
                        try:
                            choice = int(choice) - 1
                            lang_code = words_list[choice][0]
                            word = words_list[choice][1].lower()
                            print('Definitions of', word)
                            print('------------')
                            request_dict(lang_code, word)
                            print('Press enter')
                            input()    
                        except ValueError:
                            print('Invalid number')
                            break
