from data import *
def TransformePionEnReine(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY,couleurPiece):
    echiquier[positionArriveeX,positionArriveeY]= ['reine', couleurPiece]
    echiquier[positionDepartX, positionDepartY] = ['vide', 'incolore']


def deplacementAutorisePionBlanc (positionDepartX, positionDepartY,positionArriveeX, positionArriveeY) :

    if (positionArriveeY == positionDepartY+1) and (positionArriveeX == positionDepartX):
        if echiquier [positionArriveeX,positionArriveeY] == ['vide', 'incolore']:
            TransformePionEnReine(positionDepartX, positionDepartY,positionArriveeX, positionArriveeY,'blanc')
            return True


    elif (positionArriveeY == positionDepartY+2) and (positionArriveeX==positionDepartX) and positionDepartY == 1:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            if echiquier[positionArriveeX, positionArriveeY - 1 ] == ['vide', 'incolore'] and echiquier [positionArriveeX,positionArriveeY]==['vide', 'incolore']:
                return True


    elif (positionArriveeY == positionDepartY + 1) and (positionArriveeX==positionDepartX + 1 or positionArriveeX==positionDepartX - 1) :
        if echiquier[positionArriveeX, positionArriveeY][1] =='noir':
            TransformePionEnReine(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,'blanc')
            return True

    return False

def deplacementAutorisePionNoir (positionDepartX, positionDepartY,positionArriveeX, positionArriveeY) :

    if (positionArriveeY == positionDepartY-1) and (positionArriveeX==positionDepartX):
        if echiquier [positionArriveeX,positionArriveeY] ==['vide', 'incolore']:
            TransformePionEnReine(positionDepartX, positionDepartY,positionArriveeX, positionArriveeY,'noir')
            return True


    elif (positionArriveeY == positionDepartY-2) and (positionArriveeX==positionDepartX) and positionDepartY == 6:
        if echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
            if echiquier[positionArriveeX, positionArriveeY + 1 ] == ['vide', 'incolore'] and echiquier [positionArriveeX,positionArriveeY]==['vide', 'incolore']:
                return True


    elif (positionArriveeY == positionDepartY - 1) and (positionArriveeX==positionDepartX + 1 or positionArriveeX==positionDepartX - 1) :
        if echiquier[positionArriveeX, positionArriveeY][1] =='blanc':
            TransformePionEnReine(positionDepartX, positionDepartY, positionArriveeX, positionArriveeY,'noir')
            return True

    return False