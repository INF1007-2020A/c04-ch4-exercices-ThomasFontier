#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    taille = len(string)
    reste = taille % 2
    print('reste == 0')


def remove_third_char(string: str) -> str:
    for c in range(len(string))
        if (c != 3):
            print(c)


def replace_char(string: str, old_char: str, new_char: str) -> str:

    return string
    pass


def get_number_of_char(string: str, char: str) -> int:
    binaire = ord('char')
    for c in range(string):
        binaire_2 = ord('c')
        if (binaire == banaire_2):
            k += 1 
    return k


def get_number_of_words(sentence: str, word: str) -> int:
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
