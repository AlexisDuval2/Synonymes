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
        
    def produitScalaire(self, mot):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = np.dot(self.matrice[indexDuMot], self.matrice[index])
                    self.resultats.append((cooccurrence, score))
            self.resultats.sort(key=itemgetter(1), reverse=True)
        
    def moindresCarres(self, mot):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = np.sum((self.matrice[indexDuMot] - self.matrice[index])**2)
                    self.resultats.append((cooccurrence, score))
            self.resultats.sort(key=itemgetter(1))

    def blocDeVille(self, mot):
        if mot in self.dictionnaire:
            indexDuMot = self.dictionnaire[mot]
            for cooccurrence, index in self.dictionnaire.items():
                if cooccurrence not in Outils.listeDArret and indexDuMot != index:
                    score = np.sum(np.abs(self.matrice[indexDuMot] - self.matrice[index]))
                    self.resultats.append((cooccurrence, score))
            self.resultats.sort(key=itemgetter(1))

    def lancer(self, mot, nbDeResultats, methode):
        if methode == '0':
            self.produitScalaire(mot)
        elif methode == '1':
            self.moindresCarres(mot)
        elif methode == '2':
            self.blocDeVille(mot)
        
        return self.resultats[:nbDeResultats]
