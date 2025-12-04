import re
import string

# Obtener archivos
DICTIONARY = "data/dictionary.txt"
INPUT_FILE = "input/input.txt"
OUTPUT_FILE = "output/output.txt"

# Expresión regular de los caracteres válidos
VALID_CHAR_REGEX = re.compile(r"^[a-z][a-zA-Z0-9_]*$")

# Inicializa diccionario
def load_dictionary(path):
    mapeo = {}
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            lex = line.strip()
            if not lex:
                continue
            token = f"KW_{lex.upper()}"
            mapeo[lex] = token
    return mapeo

# Quita la puntuación
def delete_punctuation(word):
    return word.strip(string.punctuation + '¿¡')

# Clasifica las palabras
def classificate(word, dictionary):
    if word == "":
        return None
    if word in dictionary:
        return(dictionary[word], word)
    if VALID_CHAR_REGEX.match(word):
        return ("IDENTIFICAR", word)
    return ("SINTAXYS_ERROR", word)

# Procesa el archivo de entrada
def process_file(input_path, dictionary):
    tokens = []
    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            for raw in line.split():
                word = delete_punctuation(raw)
                clas = classificate(word, dictionary)
                if clas:
                    tokens.append(clas)
    return tokens

# Imprime la salida
def print_output(tokens, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(f"{'Token':<20}\tLexema\n")
        file.write("-"*40 + "\n")
        for tok, lex in tokens:
            file.write(f"{tok:<20}\t{lex}\n")
    print(f"Tokens escritos en {OUTPUT_FILE}")

def main():
    dic = load_dictionary(DICTIONARY)
    tokens = process_file(INPUT_FILE, dic)
    print_output(tokens, OUTPUT_FILE)
    for tok, lex in tokens:
        print(f"{tok:<20} {lex}")

if __name__ == "__main__":
    main()