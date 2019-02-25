# -*- coding: utf-8 -*-

import numpy as np
from operator import itemgetter
        
# --------------------------------------
# classe Comparateur
# --------------------------------------
class Comparateur:

    def __init__(self, liste, dictionnaire, matrice):
        self.liste = liste
        self.dictionnaire = dictionnaire
        self.matrice = matrice
        self.resultats = []
        self.motsASupprimer = {}
        
    def produitScalaire(self, mot):
        indexDuMot = self.dictionnaire[mot]
        score = []
        for cooccurrence, index in self.dictionnaire.items():
#             ici il y a un dictionnaire de stop word
#             lui-même
            score = np.dot(self.matrice[indexDuMot], self.matrice[index])
            self.resultats.append((cooccurrence, score))
        self.resultats.sort(key=itemgetter(1), reverse=True)
        
    def lancer(self):
        self.produitScalaire("je")
