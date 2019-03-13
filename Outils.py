# -*- coding: utf-8 -*-

from ListeDArret import *

# --------------------------------------
# classe Outils
# --------------------------------------
class Outils:
    
    listeDArret = {}
    for mot in ListeDArret.mots.split():
        listeDArret[mot] = 1

    @staticmethod
    def afficherMsgInitial():
        print()
        print("Entrez un mot, le nombre de synonymes que vous voulez et la méthode de calcul,")
        print("i.e. produit scalaire: 0, least squares: 1, cityblock: 2")
        print()
        print("Tapez q pour quitter")
        print()

    @staticmethod
    def afficherMsgQuitter():
        print()
        print("Merci beaucoup! A la prochaine :)")

    @staticmethod
    def afficher(tuple):
        for i in tuple:
            print(i)
