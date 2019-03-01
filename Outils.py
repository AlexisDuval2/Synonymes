# -*- coding: utf-8 -*-

# --------------------------------------
# classe Outils
# --------------------------------------
class Outils:

    mots = "un \
            une \
            les \
            de \
            le \
            il \
            à \
            l \
            d \
            des \
            que \
            en \
            qui \
            dans \
            se \
            elle \
            qu \
            s \
            du \
            sur \
            vous \
            était \
            son \
            lui \
            au \
            pas \
            pour \
            avait \
            ce \
            ne \
            je \
            sa \
            avec \
            on \
            plus \
            comme \
            par \
            la \
            et \
            est \
            mais \
            tout \
            ses \
            artagnan \
            dit \
            deux \
            c \
            cette \
            n \
            m \
            si \
            ils \
            même \
            sans \
            a \
            où \
            nous \
            tous \
            y \
            "
    listeDArret = {}
    for mot in mots.split():
        listeDArret[mot] = 1

    @staticmethod
    def afficher(tuple):
        print()
        for i in tuple:
            print(i)
    
    @staticmethod
    def validerChoixMot():
        print ("validerChoixMot")
    
    @staticmethod
    def validerChoixNbDeResultats():
        print ("validerChoixNbDeResultats")
    
    @staticmethod
    def validerChoixMethodeChoisie():
        print ("validerChoixMethodeChoisie")
