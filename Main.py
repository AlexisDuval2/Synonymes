# -*- coding: utf-8 -*-

import sys
from Vue import *

# --------------------------------------
# Main
# --------------------------------------
def main():
    print(sys.path)
    try:
        tailleFenetre = int(sys.argv[1])
        encodage = sys.argv[2]
        chemins = sys.argv[3:]
        vue = Vue(tailleFenetre, encodage, chemins)
        vue.lancer()
    except Exception as e:
        print()
        print("Veuillez contacter Alexis Duval immédiatement s'il-vous-plaît")
    return 0
if __name__ == '__main__':
    sys.exit(main())
