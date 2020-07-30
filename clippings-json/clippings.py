from collections import defaultdict
import json
# Lee el archivo 'My Cipplings.txt' y crea diccionario con las frases de los distintos libros

def read_quote(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quote = []
        for line in file:
            if '=========' in line:
                yield quote
                quote = []
            else:
                fixed_line = line.replace('\n', '')
                quote.append(fixed_line)

def write_quotes(filename, json_string):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_string)

if __name__ == '__main__':
    quote_dict = defaultdict(list)
    quote_iterator = read_quote('My Clippings.txt')
    for q in quote_iterator:
        book = q[0]
        date = q[1]
        quote = q[3]
        if book not in quote_dict:
            quote_dict[book] = [{'date': date, 'quote': quote}]
        else:
            quote_dict[book].append({'date': date, 'quote': quote})

    json_quotes = json.dumps(quote_dict, ensure_ascii=False, indent=4, sort_keys=True)
    print(json_quotes)

    write_quotes('quotes.json', json_quotes)
