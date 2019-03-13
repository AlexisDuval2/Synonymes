# -*- coding: utf-8 -*-

from Lecteur import *
from Comparateur import *
from Outils import *
import re
import time

# --------------------------------------
# classe Vue
# --------------------------------------
class Vue:

    def __init__(self, tailleFenetre, encodage, chemins):
        self.tailleFenetre = tailleFenetre
        self.encodage = encodage
        self.chemins = chemins
        self.quitter = 'q'
        self.choix = []
        self.nbDArguments = 3
        self.resultats = []
        
    def lancer(self):
        lecteur = Lecteur(self.tailleFenetre, self.encodage, self.chemins)
        
        debut = time.time()
        lecteur.lancer()
        fin = time.time()
        duree = fin - debut
        print(duree)
        
        for i in range(self.nbDArguments):
            self.choix.append(None)
        while True:
            Outils.afficherMsgInitial()
            self.choix = input().split()
            if self.choix[0] == self.quitter:
                Outils.afficherMsgQuitter()
                return 0
            elif len(self.choix) >= self.nbDArguments:
                self.choix[0] = self.choix[0].lower()
                comparateur = Comparateur(lecteur)
                if re.match("^[1-9]\d*$", self.choix[1]):
                    self.choix[1] = int(self.choix[1])
                else:
                    self.choix[1] = 0

                debut = time.time()
                self.resultats = comparateur.lancer(self.choix[0], self.choix[1], self.choix[2])
                Outils.afficher(self.resultats)
                fin = time.time()
                duree = fin - debut
                print(duree)

            self.choix = []
            for i in range(self.nbDArguments):
                self.choix.append(None)
