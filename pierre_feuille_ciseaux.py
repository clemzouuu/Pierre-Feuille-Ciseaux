from random import randint

def pierre_feuille_ciseaux():

    # Le bot a 3 choix
    choix_bot_complet = ["pierre","feuille","ciseaux"]

    # Vos points et ceux du bot sont initiés à 0 
    points_bot = 0
    points_joueurs = 0

    # Compteur de tours
    i = 0

    # Seulement 10 tours disponibles durant la partie
    while i < 10 :

        # Votre choix de jeu est demandé jusqu'à 10 fois max
        choix_joueur = input("Entrez pierre feuille ou ciseaux -> ")

        # Le choix du bot sera tiré au hasard suivant le résultat de cette variable
        choix_hasard_bot = randint(0,2)

        # Le choix du bot est tiré d'un randint servant d'index à tirer de la liste des choix possibles 
        choix_bot = choix_bot_complet[choix_hasard_bot]

        # On affiche le choix du bot afin de comparer
        print("bot :",choix_bot)

        # Si votre choix et celui du bot sont identiques, égalité
        if choix_joueur == choix_bot :
            print('\n')
            print("Égalité")
            print('\n')

        # Si votre choix == pierre et le choix du bot == feuille, point pour le bot.
        # Ses points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[0] and choix_bot == choix_bot_complet[1]:
            print('\n')
            print("Point pour le bot")
            print('\n')
            points_bot += 1
            i = i + 1
        
        # Si votre choix == pierre et le choix du bot == ciseaux, point pour vous.
        # Vos points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[0] and choix_bot == choix_bot_complet[2]:
            print('\n')
            print("Points pour vous")
            print('\n')
            points_joueurs += 1
            i = i + 1

        # Si votre choix == feuille et le choix du bot == pierre, point pour vous.
        # Vos points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[1] and choix_bot == choix_bot_complet[0]:
            print('\n')
            print("Point pour vous")
            print('\n')
            points_joueurs += 1
            i = i + 1

        # Si votre choix == feuille et le choix du bot == ciseaux, point pour le bot.
        # Ses points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[1] and choix_bot == choix_bot_complet[2]:
            print('\n')
            print("Points pour le bot")
            print('\n')
            points_bot += 1
            i = i + 1

        # Si votre choix == ciseaux et le choix du bot == pierre, point pour le bot.
        # Vos points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[2] and choix_bot == choix_bot_complet[0]:
            print('\n')
            print("Point pour le bot")
            print('\n')
            points_bot += 1
            i = i + 1

        # Si votre choix == ciseaux et le choix du bot == feuille, point pour vous.
        # Vos points augementent, on incrémente de 1 les tours
        elif choix_joueur == choix_bot_complet[2] and choix_bot == choix_bot_complet[1]:
            print('\n')
            print("Points pour vous")
            print('\n')
            points_joueurs += 1
            i = i + 1

        # Si vous entrez une mauvaise valeur, erreur, inserez de nouveau
        else :
            print('\n')
            print("Veuillez rentrer une bonne valeur")
            print('\n')

        # Si vous ou le bot atteint un score de 3, la partie est terminée     
        if points_joueurs == 3 or points_bot == 3 :
            print("Partie terminée")
            print("Vous avez",points_joueurs,"et l'AI a",points_bot,"points")
            break

        print("Vous avez",points_joueurs,"et l'AI a",points_bot,"points")
        print('\n')


pierre_feuille_ciseaux()
 
