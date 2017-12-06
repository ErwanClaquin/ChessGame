import pygame
from pygame.locals import *
import sys

'''
définition de la base de données echiquier contenant les pièces
'''
echiquier = {(i, j): ['vide', 'incolore'] for i in range(8) for j in range(8)}

echiquier[0, 1] = ['pion', 'blanc']
echiquier[1, 1] = ['pion', 'blanc']
echiquier[2, 1] = ['pion', 'blanc']
echiquier[3, 1] = ['pion', 'blanc']
echiquier[4, 1] = ['pion', 'blanc']
echiquier[5, 1] = ['pion', 'blanc']
echiquier[6, 1] = ['pion', 'blanc']
echiquier[7, 1] = ['pion', 'blanc']
echiquier[0, 0] = ['tour', 'blanc']
echiquier[1, 0] = ['cavalier', 'blanc']
echiquier[2, 0] = ['fou', 'blanc']
echiquier[3, 0] = ['reine', 'blanc']
echiquier[4, 0] = ['roi', 'blanc']
echiquier[5, 0] = ['fou', 'blanc']
echiquier[6, 0] = ['cavalier', 'blanc']
echiquier[7, 0] = ['tour', 'blanc']

echiquier[0, 6] = ['pion', 'noir']
echiquier[1, 6] = ['pion', 'noir']
echiquier[2, 6] = ['pion', 'noir']
echiquier[3, 6] = ['pion', 'noir']
echiquier[4, 6] = ['pion', 'noir']
echiquier[5, 6] = ['pion', 'noir']
echiquier[6, 6] = ['pion', 'noir']
echiquier[7, 6] = ['pion', 'noir']
echiquier[0, 7] = ['tour', 'noir']
echiquier[1, 7] = ['cavalier', 'noir']
echiquier[2, 7] = ['fou', 'noir']
echiquier[3, 7] = ['reine', 'noir']
echiquier[4, 7] = ['roi', 'noir']
echiquier[5, 7] = ['fou', 'noir']
echiquier[6, 7] = ['cavalier', 'noir']
echiquier[7, 7] = ['tour', 'noir']



coordonnees_ancienne = 0
coordonnees_nouvelles = 0
deplacementPieceEnCours = False

LEFT_BUTTON = 1
couleurDuJoueur = 'blanc'
compteurDeplacementDeTourGaucheBlanche = 0
compteurDeplacementDeTourGaucheNoire = 0
compteurDeplacementDeTourDroiteBlanche = 0
compteurDeplacementDeTourDroiteNoire = 0
compteurRoiBlanc = 0
compteurRoiNoir = 0

partieEnCours = True
verifieSiMatchNul = False


"""
Definition et initialisation de l'ecran ainsi que des cases qui changeront de couleur
"""

TailleCases = 64
selection = pygame.Surface((TailleCases, TailleCases), pygame.SRCALPHA)

ecran = pygame.display.set_mode((TailleCases * 8, TailleCases * 8))

"""
Definition et initialisation des images des pièces et des case
"""
caseVideBlanc = pygame.image.load("ivoire.png").convert_alpha()
caseVideNoir = pygame.image.load("ebene.png").convert_alpha()
ImagePionBlanc = pygame.image.load("PionBlanc1.png").convert_alpha()
ImagePionNoir = pygame.image.load("PionNoir1.png").convert_alpha()
ImageCavalierBlanc = pygame.image.load("CavalierBlanc1.png").convert_alpha()
ImageCavalierNoir = pygame.image.load("CavalierNoir1.png").convert_alpha()
ImageTourBlanc = pygame.image.load("TourBlanche1.png").convert_alpha()
ImageTourNoir = pygame.image.load("TourNoire1.png").convert_alpha()
ImageFouBlanc = pygame.image.load("FouBlanc1.png").convert_alpha()
ImageFouNoir = pygame.image.load("FouNoir1.png").convert_alpha()
ImageReineBlanc = pygame.image.load("ReineBlanche.png").convert_alpha()
ImageReineNoir = pygame.image.load("ReineNoire.png").convert_alpha()
ImageRoiBlanc = pygame.image.load("RoiBlanc.png").convert_alpha()
ImageRoiNoir = pygame.image.load("RoiNoir.png").convert_alpha()

"""
Initialisation de variables
"""

