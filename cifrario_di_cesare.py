from string import ascii_lowercase

def caesar_cypher_encrypt(s, key):
    alfabeto_minuscolo = ascii_lowercase
    alfabeto_maiuscolo = ascii_lowercase.upper()
    risultato = ""

    for lettera in s:
        if lettera in alfabeto_minuscolo:
            posizione = alfabeto_minuscolo.index(lettera)
            nuova_posizione = (posizione + key) % 26
            risultato += alfabeto_minuscolo[nuova_posizione]
        elif lettera in alfabeto_maiuscolo:
            posizione = alfabeto_maiuscolo.index(lettera)
            nuova_posizione = (posizione + key) % 26
            risultato += alfabeto_maiuscolo[nuova_posizione]
        else:
            risultato += lettera
    return risultato

def caesar_cypher_decrypt(s, key):
    return caesar_cypher_encrypt(s, -key)