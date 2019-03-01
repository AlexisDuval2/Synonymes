# -*- coding: utf-8 -*-

# --------------------------------------
# classe Outils
# --------------------------------------
class Outils:

    mots = "un \
            une \
            les"
    listeDArret = {}
    for mot in mots.split():
        listeDArret[mot] = 1

    @staticmethod
    def afficher(tuple):
        print()
        for i in tuple:
            print(i)
    
    @staticmethod
    def validerChoixMot():
        print ("validerChoixMot")
    
    @staticmethod
    def validerChoixNbDeResultats():
        print ("validerChoixNbDeResultats")
    
    @staticmethod
    def validerChoixMethodeChoisie():
        print ("validerChoixMethodeChoisie")
