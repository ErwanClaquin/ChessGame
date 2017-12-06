from deplacementAutorise import *
from RocPossible import *
from CasesPossibles import *
from Echec.EchecEtMat import *
from MatchNul import *

while partieEnCours and not verifieSiMatchNul:
    """On regarde s'il y'a une pièce en déplacement ou non afin de faire un drag and drop"""
    if not deplacementPieceEnCours:
        affichageEchiquier()
        convertitPixelEnCase()
        pygame.display.flip()

    if deplacementPieceEnCours:
        coordx = event.pos[0] - 32
        coordy = event.pos[1] - 32
        affichageEchiquier()
        casesPossibles(savePiece, xDepart, yDepart, changeCouleurDuJoueur(couleurDuJoueur))
        convertitPixelEnCase()
        ecran.blit(imageADeplacer, (coordx, coordy))
        pygame.display.flip()

    for event in pygame.event.get():
        """On fait la liste de tous les évenements qui peuvent se produirent"""
        if event.type == QUIT:
            """Si l'utilisateur clic sur al croix en haut à droite, le programme se ferme"""
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            """Lorsque l'utilisateur fait un clic gauche, on prend les coordonnées de son clic et on les adaptes en cases de l'echiquier"""
            coordonnees_ancienne = pygame.mouse.get_pos()
            xDepart = coordonnees_ancienne[0] // TailleCases
            yDepart = coordonnees_ancienne[1] // TailleCases
            coordonnees_ancienne = (xDepart, yDepart)

            if dansLEchiquier(xDepart, yDepart):
                """On vérifie qu'il clic bien dans l'échiquier et non à côté"""
                savePiece = echiquier[coordonnees_ancienne]
                saveCoordonne = coordonnees_ancienne

                if bonneCouleurPieceChoisie(echiquier[coordonnees_ancienne], couleurDuJoueur):
                    """On vérifie que le joueur prends la bonne couleur de pièce et non pas une adverse. On l'enlève de l'échiquier pour la placer sur le curseur en mettant le déplacement sur True"""
                    deplacementPieceEnCours = True
                    imageADeplacer = ImageSurCurseur(echiquier[coordonnees_ancienne])
                    echiquier[coordonnees_ancienne] = ['vide', 'incolore']

                    """Ici sont les 3 cas échéants des vérifications ci-dessus"""
                elif savePiece[1] == 'incolore':
                    print("Aucune pièce choisie !")

                else:
                    print("Ce n'est pas votre pièce !")

            else:
                print("Vous êtes en dehors de l'échiquier !")



        if event.type == MOUSEBUTTONUP and event.button == LEFT_BUTTON:
            """On vérifie quand est-ce que le joueur relâche son clic gauche. On prends alors les coordonnées où il a relaâcher le clic et on les adaptes en cases de l'échiquier"""
            coordonnees_nouvelles = pygame.mouse.get_pos()
            xArrive = coordonnees_nouvelles[0] // TailleCases
            yArrive = coordonnees_nouvelles[1] // TailleCases
            coordonnees_nouvelles = (xArrive, yArrive)
            caseArrive = echiquier[xArrive, yArrive]

            if dansLEchiquier(xArrive, yArrive):
                """On vérifie qu'il clic bien dans l'échiquier et non à côté"""

                if bonneCouleurPieceChoisie(savePiece, couleurDuJoueur):
                    """On vérifie que le joueur prends la bonne couleur de pièce et non pas une adverse."""

                    if deplacementAutorise(xDepart, yDepart, xArrive, yArrive, savePiece, changeCouleurDuJoueur(couleurDuJoueur)):
                        """On vérifie que la pièce qu'il à déplacer se situe bien sur sa zone de déplacement, et si oui on place la pièce là où il à relâcher"""
                        print("déplacement de " + str(savePiece) + " en " + str(coordonnees_nouvelles))
                        deplacementPieceEnCours = False
                        echiquier[coordonnees_nouvelles] = savePiece

                        if couleurDuJoueur == 'blanc':
                            """On prends la couleur du joueur actuelle (ici blanc) afin d'executer éventuellement des actions ci-dessous"""

                            if savePiece[0] == 'pion' and yArrive == 7:
                                """Si un pion blanc arrive sur la dernière ligne en face de lui, on le transorme en reine"""
                                TransformePionEnReine(xDepart, yDepart, xArrive, yArrive, savePiece[1])
                                print("Un pion", savePiece[1], "s'est transformé en reine !")

                            if savePiece[0] == 'roi' and compteurRoiBlanc == 0:
                                compteurRoiBlanc = 1
                            if savePiece[0] == 'tour' and xDepart == 7:
                                compteurDeplacementDeTourDroiteBlanche = 1
                            if savePiece[0] == 'tour' and xDepart == 0:
                                compteurDeplacementDeTourGaucheBlanche = 1

                            if roiBlancEnEchec():
                                """A la fin du déplacement, on vérifie que le roi blanc est en échec. Si il l'est, on annule le déplacement du joueur"""
                                print("Votre roi blanc est en échec")
                                echiquier[saveCoordonne] = savePiece
                                echiquier[coordonnees_nouvelles] = caseArrive
                                break



                            if roiNoirEchecEtMat():
                                partieEnCours=False
                                break

                        elif couleurDuJoueur == 'noir':
                            """On prends la couleur du joueur actuelle (ici noir) afin d'executer éventuellement des actions ci-dessous"""
                            if savePiece[0] == 'pion' and yArrive == 0:
                                """Si un pion noir arrive sur la dernière ligne en face de lui, on le transorme en reine"""
                                TransformePionEnReine(xDepart, yDepart, xArrive, yArrive, savePiece[1])
                                print("Un pion", savePiece[1], "s'est transformé en reine !")

                            if savePiece == 'roi' and compteurRoiNoir == 0:
                                compteurRoiNoir = 1
                            if savePiece[0] == 'tour' and xDepart == 7:
                                compteurDeplacementDeTourDroiteNoire = 1
                            if savePiece[0] == 'tour' and xDepart == 0:
                                compteurDeplacementDeTourGaucheNoire = 1

                            if roiNoirEnEchec():
                                """A la fin du déplacement, on vérifie que le roi blanc est en échec. Si il l'est, on annule le déplacement du joueur"""
                                print("Votre roi noir est en échec")
                                echiquier[saveCoordonne]= savePiece
                                echiquier[coordonnees_nouvelles]= caseArrive
                                break

                            if roiBlancEchecEtMat():
                                partieEnCours=False
                                break

                        """On change la couleur du joueur"""
                        couleurDuJoueur = changeCouleurDuJoueur(couleurDuJoueur)

                        """Ici on affiche la cuoleur du joueur qui va jouer et si les rois sont en échecs ou non."""
                        if roiBlancEnEchec():
                            print("Le roi blanc est en échec !")
                        elif roiNoirEnEchec():
                            print("Le roi noir est en échec !")
                        print("===========\n Nouveau Tour ! Tour du joueur " + str(couleurDuJoueur))

                        if matchNul(changeCouleurDuJoueur(couleurDuJoueur)):
                            """On vérifie si la partie est nulle, c'est à dire que le roi, seul sur un plateau, n'est pas en échec sur sa case mais peut importe où il va il le sera"""
                            partieEnCours = False
                            verifieSiMatchNul = True
                            break

                        """Il existe les ROCS qui ne sont pas comptés dans les déplacements autorisés. On vérifie alors que si le joueur veut faire cette action, il puisse."""
                    elif petitRocBlanc(xDepart, yDepart, xArrive, yArrive, compteurDeplacementDeTourDroiteBlanche,savePiece):
                        compteurDeplacementDeTourDroiteBlanche = 1
                        compteurRoiBlanc = 1
                        echiquier[5, 0] = ['tour', 'blanc']
                        echiquier[7, 0] = ['vide', 'incolore']
                        echiquier[6, 0] = ['roi', 'blanc']
                        echiquier[4, 0] = ['vide', 'incolore']
                        couleurDuJoueur = changeCouleurDuJoueur(couleurDuJoueur)
                        print("===========\n Nouveau Tour ! Tour du joueur " + str(couleurDuJoueur))
                        deplacementPieceEnCours = False

                    elif petitRocNoir(xDepart, yDepart, xArrive, yArrive, compteurDeplacementDeTourDroiteNoire,savePiece):
                        compteurDeplacementDeTourDroiteNoire = 1
                        compteurRoiNoir = 1
                        echiquier[5, 7] = ['tour', 'noir']
                        echiquier[7, 7] = ['vide', 'incolore']
                        echiquier[6, 7] = ['roi', 'noir']
                        echiquier[4, 7] = ['vide', 'incolore']
                        couleurDuJoueur = changeCouleurDuJoueur(couleurDuJoueur)
                        print("===========\n Nouveau Tour ! Tour du joueur " + str(couleurDuJoueur))
                        deplacementPieceEnCours = False

                    elif grandRocBlanc(xDepart, yDepart, xArrive, yArrive, compteurDeplacementDeTourGaucheBlanche,savePiece):
                        compteurDeplacementDeTourGaucheBlanche = 1
                        compteurRoiBlanc = 1
                        echiquier[3, 0] = ['tour', 'blanc']
                        echiquier[0, 0] = ['vide', 'incolore']
                        echiquier[2, 0] = ['roi', 'blanc']
                        echiquier[4, 0] = ['vide', 'incolore']
                        couleurDuJoueur = changeCouleurDuJoueur(couleurDuJoueur)
                        print("===========\n Nouveau Tour ! Tour du joueur " + str(couleurDuJoueur))
                        deplacementPieceEnCours = False

                    elif grandRocNoir(xDepart, yDepart, xArrive, yArrive, compteurDeplacementDeTourGaucheNoire,savePiece):
                        compteurDeplacementDeTourGaucheNoire = 1
                        compteurRoiNoir = 1
                        echiquier[3, 7] = ['tour', 'noir']
                        echiquier[0, 7] = ['vide', 'incolore']
                        echiquier[2, 7] = ['roi', 'noir']
                        echiquier[4, 7] = ['vide', 'incolore']
                        couleurDuJoueur = changeCouleurDuJoueur(couleurDuJoueur)
                        print("===========\n Nouveau Tour ! Tour du joueur " + str(couleurDuJoueur))
                        deplacementPieceEnCours = False

                    else:
                        """Si le joueur à déplacer sa pièce autre part qu'en faisant un ROC ou dans les déplacements de la pièce, on annule son déplacement"""
                        print("Pas le bon déplacement")
                        deplacementPieceEnCours = False
                        echiquier[saveCoordonne] = savePiece

                else:
                    """Si le joueur n'a pas sélectionner sa pièce lors du clic, on empêche que la pièce bouge tout de même et que cela duplique les pièces"""
                    print("Vous avez pris la mauvaise couleur !")
                    deplacementPieceEnCours = False
                    echiquier[saveCoordonne] = savePiece

            else:
                """Affiche si le joueur n'est pas dans l'échiquier"""
                print("Vous n'êtes pas dans l'échiquier !")
                deplacementPieceEnCours = False
                echiquier[saveCoordonne] = savePiece

print("La partie est finie ! le joueur", couleurDuJoueur, "gagne !")