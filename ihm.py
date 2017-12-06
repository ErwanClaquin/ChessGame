from data import *

def convertitPixelEnCase():
    """On créer des tailles de carré à remplir (TailleCases) avant de choisir la couleur de cette sélection si il y'a un clic ou non"""
    position_souris = pygame.mouse.get_pos()  # Nous renvoie un tuple qui est (x,y)
    x = position_souris[0] // TailleCases
    y = position_souris[1] // TailleCases  # ces deux lignes nous disent dans quelle case on est

    if pygame.mouse.get_pressed()[0]:  #  Si le bouton gauche de la souris est pressé
        selection.fill((255, 0, 0, 128))

    else:
        selection.fill((0, 255, 0, 64)) # on la remplit en vert transparent
    pygame.draw.rect(selection, (255, 0, 0, 40), pygame.Rect(0, 0, TailleCases, TailleCases), 2)

    ecran.blit(selection, (x * TailleCases, y * TailleCases))



def affichageEchiquier():
    """" affichage du damier vide"""

    y = 0
    for i in range(1, 9):
        x = 0
        for j in range(1, 9):
            if ((x + y) / 64) % 2 == 0:
                ecran.blit(caseVideBlanc, (x, y))
            else:
                ecran.blit(caseVideNoir, (x, y))
            x += 64
        y += 64

    """On place ici toutes les images des pièces sur le damier"""
    for i in range(0, 8):
        for j in range(0, 8):
            if echiquier[i, j] == ['pion', 'blanc']:
                ecran.blit(ImagePionBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['pion', 'noir']:
                ecran.blit(ImagePionNoir, (i * 64, j * 64))
            elif echiquier[i, j] == ['cavalier', 'blanc']:
                ecran.blit(ImageCavalierBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['cavalier', 'noir']:
                ecran.blit(ImageCavalierNoir, (i * 64, j * 64))
            elif echiquier[i, j] == ['tour', 'blanc']:
                ecran.blit(ImageTourBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['tour', 'noir']:
                ecran.blit(ImageTourNoir, (i * 64, j * 64))
            elif echiquier[i, j] == ['fou', 'blanc']:
                ecran.blit(ImageFouBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['fou', 'noir']:
                ecran.blit(ImageFouNoir, (i * 64, j * 64))
            elif echiquier[i, j] == ['reine', 'blanc']:
                ecran.blit(ImageReineBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['reine', 'noir']:
                ecran.blit(ImageReineNoir, (i * 64, j * 64))
            elif echiquier[i, j] == ['roi', 'blanc']:
                ecran.blit(ImageRoiBlanc, (i * 64, j * 64))
            elif echiquier[i, j] == ['roi', 'noir']:
                ecran.blit(ImageRoiNoir, (i * 64, j * 64))

    return



def ImageSurCurseur(piece):
    """Renvoie l'image de la pièce"""
    if piece == ['pion', 'blanc']:
        return ImagePionBlanc
    elif piece == ['pion', 'noir']:
        return ImagePionNoir
    elif piece == ['cavalier', 'blanc']:
        return ImageCavalierBlanc
    elif piece == ['cavalier', 'noir']:
        return ImageCavalierNoir
    elif piece == ['tour', 'blanc']:
        return ImageTourBlanc
    elif piece == ['tour', 'noir']:
        return ImageTourNoir
    elif piece == ['fou', 'blanc']:
        return ImageFouBlanc
    elif piece == ['fou', 'noir']:
        return ImageFouNoir
    elif piece == ['reine', 'blanc']:
        return ImageReineBlanc
    elif piece == ['reine', 'noir']:
        return ImageReineNoir
    elif piece == ['roi', 'blanc']:
        return ImageRoiBlanc
    elif piece == ['roi', 'noir']:
        return ImageRoiNoir
    else:
        return None



def changeCouleurDuJoueur(couleurDuJoueur):
    """Cela permet de changer de joueur, donc de tour lorsque cette fonction est appelée"""
    if couleurDuJoueur == 'noir':
        return 'blanc'
    else:
        return 'noir'



def bonneCouleurPieceChoisie(piece,couleurDuJoueur):
    """Cette fonction permet de vérifier que le joueur à bien pris une pièce de sa couleur"""
    if piece[1]== couleurDuJoueur:
        return True
    else:
        return False



def dansLEchiquier(coordx,coordy):
    """On vérifie que les coordonnées prises sont bien entre 0 et 7 inclus"""
    return (coordx >= 0 and coordx < 8 ) and ( coordy >= 0 and coordy < 8)

