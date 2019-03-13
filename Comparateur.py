# -*- coding: utf-8 -*-

import numpy as np
from operator import itemgetter
from Outils import *
        
# --------------------------------------
# classe Comparateur
# --------------------------------------
class Comparateur:

    def __init__(self, lecteur):
        self.lecteur = lecteur
        self.liste = lecteur.liste
        self.dictionnaire = lecteur.dictionnaire
        self.matrice = lecteur.matrice
        self.resultats = []
        self.motsASupprimer = {}
        self.ordreDuTri = False
        
#     def produitScalaire(self, mot):
#         if mot in self.dictionnaire:
#             indexDuMot = self.dictionnaire[mot]
#             for cooccurrence, index in self.dictionnaire.items():
#                 if cooccurrence not in Outils.listeDArret and indexDuMot != index:
#                     score = np.dot(self.matrice[indexDuMot], self.matrice[index])
#                     self.resultats.append((cooccurrence, score))
#             self.resultats.sort(key=itemgetter(1), reverse=True)
#         
#     def moindresCarres(self, mot):
#         if mot in self.dictionnaire:
#             indexDuMot = self.dictionnaire[mot]
#             for cooccurrence, index in self.dictionnaire.items():
#                 if cooccurrence not in Outils.listeDArret and indexDuMot != index:
#                     score = np.sum((self.matrice[indexDuMot] - self.matrice[index])**2)
#                     self.resultats.append((cooccurrence, score))
#             self.resultats.sort(key=itemgetter(1))
# 
#     def blocDeVille(self, mot):
#         if mot in self.dictionnaire:
#             indexDuMot = self.dictionnaire[mot]
#             for cooccurrence, index in self.dictionnaire.items():
#                 if cooccurrence not in Outils.listeDArret and indexDuMot != index:
#                     score = np.sum(np.abs(self.matrice[indexDuMot] - self.matrice[index]))
#                     self.resultats.append((cooccurrence, score))
#             self.resultats.sort(key=itemgetter(1))
# 
#     def lancer(self, mot, nbDeResultats, methode):
#         if methode == '0':
#             self.produitScalaire(mot)
#         elif methode == '1':
#             self.moindresCarres(mot)
#         elif methode == '2':
#             self.blocDeVille(mot)
# 
#         return self.resultats[:nbDeResultats]

    def produitScalaire(self, indexDuMot, index):
        return np.dot(self.matrice[indexDuMot], self.matrice[index])
        
    def moindresCarres(self, indexDuMot, index):
        return np.sum((self.matrice[indexDuMot] - self.matrice[index])**2)

    def blocDeVille(self, indexDuMot, index):
        return np.sum(np.abs(self.matrice[indexDuMot] - self.matrice[index]))

    def trouverOrdreDuTri(self, methode):
        if methode == '0':
            self.ordreDuTri = True
        elif methode == '1' or methode == '2':
            self.ordreDuTri = False

    def calculer(self, fonction, methode):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = fonction(indexDuMot, index)
                    self.resultats.append((cooccurrence, score))
            trouverOrdreDuTri(methode)
            self.resultats.sort(key=itemgetter(1), reverse=self.ordreDuTri)

    def lancer(self, mot, nbDeResultats, methode):
        
        fonction = produitScalaire

        if methode == '0':
            self.produitScalaire(mot)
        elif methode == '1':
            self.moindresCarres(mot)
        elif methode == '2':
            self.blocDeVille(mot)

        calculer(mot, f)
 
        return self.resultats[:nbDeResultats]

#-----------------------------------------
# simplifier fonctions...
#-----------------------------------------
# 
# NE PAS METTRE DE PARENTHÈSES LORSQUE J'APPELLE DES FONCTIONS!
#
#     def incremente(x):
#         return x+1
#     
#     f = incremente
#     f(3) # ça va donner 4
#
#----------------------
#
#     def test(vecteur1, vecteur2):
#         np.sum(np.square(v1, v2))
#
#     def calculer(mot, fonction):
#         fonction(v1, v2)
#     
#     f = test
#     calculer(mot, f)
#     
#-----------------------------------------
