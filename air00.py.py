#Split
#Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).

"""Votre programme devra utiliser une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	 votre algorithme
	return (tableau)
}"""


import sys 

argument = sys.argv[1:]

liste = []

def separateur(argument):
    if len(argument) < 1:
        print("Error")
    elif len(argument) == 1:
        for element in argument:
            sous_chaines = element.split()
            liste.append(sous_chaines)
    else:
        for arg in argument:
            sous_chaines = arg.split()
            liste.append(sous_chaines)
            
separateur(argument)

for element in liste:
    for sous_chaine in element:
        print(sous_chaine)