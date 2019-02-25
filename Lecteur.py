# -*- coding: utf-8 -*-

import sys
import re
import numpy as np

# --------------------------------------
# classe Lecteur
# --------------------------------------
class Lecteur:

    def __init__(self):
        self.tailleFenetre = int(sys.argv[1])
        self.decalage = int(self.tailleFenetre / 2)
        self.encodage = sys.argv[2]
        self.chemin = sys.argv[3]
        self.texte = ""
        self.expression = "\w+"
        self.liste = []
        self.dictionnaire = {}
        self.matrice = None
    
    def extraire(self):
        try:
            fichier = open(self.chemin, 'r', encoding = self.encodage)
            self.texte = fichier.read()
            fichier.close()
        except FileNotFoundError as fnf:
            print()
            print("Problème de chemin")
            print(fnf)
            return 0;
        except Exception as e:
            print()
            print("Problème générique")
            print(e)
            return 0
        return 1
            
    def mettreEnMinuscule(self):
        self.texte = self.texte.lower()
        
    def chargerListe(self):
        for mot in re.findall(self.expression, self.texte):
            self.liste.append(mot)
        
    def chargerDictionnaire(self):
        # note: le dictionnaire contient l'index de chaque mot
        compteur = 0
        for mot in self.liste:
            if mot not in self.dictionnaire:
                self.dictionnaire[mot] = compteur
                compteur += 1
            
    def chargerMatrice(self):
        taille = len(self.dictionnaire)
        self.matrice = np.zeros((taille, taille))
        
        for i in range(len(self.liste) - self.tailleFenetre):

            mot = self.liste[i]
            ligne = self.dictionnaire[mot]

            for j in range(-self.decalage, self.decalage):

                if j == 0:
                    continue

                motTemp = self.liste[i + j]
                colonne = self.dictionnaire[motTemp]
                self.matrice[ligne][colonne] += 1
    
    def lancer(self):
        self.extraire()
        self.mettreEnMinuscule()
        self.chargerListe()
        self.chargerDictionnaire()
        self.chargerMatrice()
