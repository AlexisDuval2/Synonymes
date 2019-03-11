# -*- coding: utf-8 -*-

import re
import numpy as np

# --------------------------------------
# classe Lecteur
# --------------------------------------
class Lecteur:

    def __init__(self, tailleFenetre, encodage, chemins):
        self.tailleFenetre = tailleFenetre
        self.decalage = self.tailleFenetre//2
        self.encodage = encodage
        self.chemins = chemins

        self.texte = []
        self.expression = "\w+"
        self.liste = []
        self.dictionnaire = {}
        self.matrice = None
    
    def extraire(self):
        try:
            for fichier in self.chemins:
                fichier = open(fichier, 'r', encoding = self.encodage)
                self.texte.append(fichier.read())
                fichier.close()
            resultat = ''.join(self.texte)
            self.texte = resultat
        except FileNotFoundError as fnf:
            print()
            print("Problème de chemin")
        except Exception as e:
            print()
            print("Problème générique")
            
    def mettreEnMinuscule(self):
        self.texte = self.texte.lower()
        
    def chargerListe(self):
        self.liste = re.findall(self.expression, self.texte)
        
    def chargerDictionnaire(self):
        compteur = 0
        for mot in self.liste:
            if mot not in self.dictionnaire:
                self.dictionnaire[mot] = compteur
                compteur += 1
            
    def chargerMatrice(self):
        taille = len(self.dictionnaire)
        self.matrice = np.zeros((taille, taille))
        for i in range(self.decalage, len(self.liste) - self.decalage):
            mot = self.liste[i]
            ligne = self.dictionnaire[mot]
            for j in range(i - self.decalage, i + self.decalage):
                motTemp = self.liste[j]
                colonne = self.dictionnaire[motTemp]
                if colonne == ligne:
                    continue
                self.matrice[ligne][colonne] += 1
    
    def lancer(self):
        self.extraire()
        self.mettreEnMinuscule()
        self.chargerListe()
        self.chargerDictionnaire()
        self.chargerMatrice()
