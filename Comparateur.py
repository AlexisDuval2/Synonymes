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
        self.methodeChoisie = None

    def produitScalaire(self, indexDuMot, index):
        return np.dot(self.matrice[indexDuMot], self.matrice[index])
        
    def moindresCarres(self, indexDuMot, index):
        return np.sum((self.matrice[indexDuMot] - self.matrice[index])**2)

    def blocDeVille(self, indexDuMot, index):
        return np.sum(np.abs(self.matrice[indexDuMot] - self.matrice[index]))

    def trouverMethodeChoisie(self, methodeChoisie):
        if methodeChoisie == '0':
            self.methodeChoisie = self.produitScalaire
        elif methodeChoisie == '1':
            self.methodeChoisie = self.moindresCarres
        elif methodeChoisie == '2':
            self.methodeChoisie = self.blocDeVille

    def calculer(self, mot, methode):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = methode(indexDuMot, index)
                    self.resultats.append((cooccurrence, score))

    def trier(self, methodeChoisie):
        if methodeChoisie == '0':
            self.resultats.sort(key=itemgetter(1), reverse=True)
        else:
            self.resultats.sort(key=itemgetter(1))

    def lancer(self, mot, nbDeResultats, methodeChoisie):
        self.trouverMethodeChoisie(methodeChoisie)
        self.calculer(mot, self.methodeChoisie)
        self.trier(methodeChoisie)
        return self.resultats[:nbDeResultats]
