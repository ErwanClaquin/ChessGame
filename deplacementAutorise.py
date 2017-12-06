from deplacementAutorisePion import *
from deplacementAutoriseCavalier import *
from deplacementAutoriseFou import *
from deplacementAutoriseTour import *
from deplacementAutoriseRoi import *
from deplacementAutoriseReine import *

def deplacementAutorise (positionDepartX,positionDepartY,positionArriveeX,positionArriveeY,pieceSelectionnee,couleurJoueurAdverse) :
    if pieceSelectionnee == ['pion', 'blanc']:
        return deplacementAutorisePionBlanc (positionDepartX,positionDepartY,positionArriveeX,positionArriveeY)

    elif pieceSelectionnee == ['pion', 'noir']:
        return deplacementAutorisePionNoir(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY)

    elif pieceSelectionnee[0] == 'cavalier':
        return deplacementAutoriseCavalier(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,couleurJoueurAdverse)

    elif pieceSelectionnee[0] == 'fou':
        return deplacementAutoriseFou(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,couleurJoueurAdverse)

    elif pieceSelectionnee[0] == 'tour':
        return deplacementAutoriseTour(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,couleurJoueurAdverse)

    elif pieceSelectionnee[0] == 'reine':
        return deplacementAutoriseReine(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,couleurJoueurAdverse)

    elif pieceSelectionnee[0] == 'roi':
        return deplacementAutoriseRoi(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,couleurJoueurAdverse)

    else:
        return False