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

def Gestion_erreur():
    if len(arguments) != 2:
    	print("entrer 2 arguments")
