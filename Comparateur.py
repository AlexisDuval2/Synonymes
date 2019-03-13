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
        self.methodeChoisie = None

    def produitScalaire(self, indexDuMot, index):
        return np.dot(self.matrice[indexDuMot], self.matrice[index])
        
    def moindresCarres(self, indexDuMot, index):
        return np.sum((self.matrice[indexDuMot] - self.matrice[index])**2)

    def blocDeVille(self, indexDuMot, index):
        return np.sum(np.abs(self.matrice[indexDuMot] - self.matrice[index]))

    def trouverMethodeChoisie(self, entree):
        if entree == '0':
            fonction = self.produitScalaire
        elif entree == '1':
            fonction = self.moindresCarres
        elif entree == '2':
            fonction = self.blocDeVille
        return fonction

    def calculer(self, mot, fonction):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = fonction(indexDuMot, index)
                    self.resultats.append((cooccurrence, score))


        return fonction

    def trier(self, methode):
        if methode == '0':
            self.resultats.sort(key=itemgetter(1), reverse=True)
        else:
            self.resultats.sort(key=itemgetter(1))

    def lancer(self, mot, nbDeResultats, methode):
        calculer(mot, fonction)
        trier(methode)
 
        return self.resultats[:nbDeResultats]
