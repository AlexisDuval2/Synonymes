# -*- coding: utf-8 -*-

import sys
from Comparateur import *
from Lecteur import *
from Vue import *

# --------------------------------------
# Main
# --------------------------------------
def main():

    try:
        tailleFenetre = int(sys.argv[1])
        encodage = sys.argv[2]
        chemin = sys.argv[3]

        vue = Vue()
        vue.algo()
        vue.lancer()
        
    except Exception as e:
        print()
        print("Problème avec le main")
        raise(e)
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
