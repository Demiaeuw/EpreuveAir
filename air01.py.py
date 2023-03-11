#Split en fonction
#Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

"""Votre programme devra utiliser une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	 votre algorithme
	return (tableau)
}"""

import sys

arguments = sys.argv[1:]
phrase = sys.argv[1]
separateur = sys.argv[2]

def Separation(a, b):
    if b in a:
        phraseUn = a[:a.index(b)]
        phraseDeux = a[a.index(b) + len(b):]
        return [phraseUn, phraseDeux]
    else:
        return []

try:
    if len(arguments) != 2:
    	print("Entrer 2 arguments")
    else:
        result = Separation(phrase, separateur)
        if result:
            print(result[0], "\n", result[1])
        else:
            print("Le séparateur n'a pas été trouvé dans la phrase.")
except ValueError:
    print("Error")
