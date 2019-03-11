# -*- coding: utf-8 -*-

import sys
from Lecteur import *
from Comparateur import *
from Outils import *
import re

# --------------------------------------
# classe Vue
# --------------------------------------
class Vue:

    def __init__(self):
        self.tailleFenetre = int(sys.argv[1])
        self.encodage = sys.argv[2]
        self.chemin = sys.argv[3]
        self.produitScalaire = '0';
        self.moindresCarres = '1';
        self.blocDeVille = '2';
        self.quitter = 'q'
        self.choix = []
        self.nbDArguments = 3
        self.resultats = []
        
    def lancer(self):
        lecteur = Lecteur()
        lecteur.lancer()
        for i in range(self.nbDArguments):
            self.choix.append(None)
        while True:
            Outils.afficherMsgInitial()
            self.choix = input().split()
            if self.choix[0] == self.quitter:
                Outils.afficherMsgQuitter()
                return 0
            elif len(self.choix) >= 3:
                comparateur = Comparateur(lecteur)
                if re.match("^[1-9]\d*$", self.choix[1]):
                    self.choix[1] = int(self.choix[1])
                else:
                    self.choix[1] = 0
                self.resultats = comparateur.lancer(self.choix[0], self.choix[1], self.choix[2])
                Outils.afficher(self.resultats)
            self.choix = []
            for i in range(self.nbDArguments):
                self.choix.append(None)
