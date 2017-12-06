from data import *
def deplacementAutoriseFou(positionDepartX,positionDepartY,positionArriveeX,positionArriveeY, couleurEnnemi) :

    """
    On vérifie si le déplacement de la pièce 'fou' est correct tout en vérifiant si sur son chemin
    aucune pièce ne pourrait bloquer le passage jusqu"à la case d'arrivée.
    Si le chemin est possible on regarde sur la case d'arivée si il y a une pièce adverse : si c'est le cas la pièce est mangée.
    Si la case d'arrivée est vide le déplacement est possible
    Si il y a une pièce allié sur la case d'arrivée le déplacement est impossible

    :param positionDepartX: int
    :param positionDepartY: int
    :param positionArriveeX: int
    :param positionArriveeY: int
    :param couleur: string
    :param couleurEnnemi: string
    :return: True si le déplacement est bon et False si celui ci est incorrect
    """



    if abs(positionArriveeX - positionDepartX) == abs(positionArriveeY - positionDepartY) :

        if positionArriveeX > positionDepartX and positionArriveeY > positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX + i, positionDepartY + i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True



        elif positionArriveeX < positionDepartX and positionArriveeY > positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX - i, positionDepartY + i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True



        elif positionArriveeX < positionDepartX and positionArriveeY < positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX - i, positionDepartY - i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True

        elif positionArriveeX > positionDepartX and positionArriveeY < positionDepartY :
            for i in range (1, abs(positionArriveeX - positionDepartX)) :
                if echiquier[positionDepartX + i, positionDepartY - i] != ['vide', 'incolore'] :
                    return False
            if echiquier[positionArriveeX, positionArriveeY][1] == couleurEnnemi or echiquier[positionArriveeX, positionArriveeY] == ['vide', 'incolore']:
                return True

    return False