import random

questions = ("commerce", "inciter, stimuler", "étouffant", "est monté en flèche", "écoulement", "maitrise", "versatile (synonym)",
             "hors ligne", "rarement", "je vais rarement à la plage", "modèle", "toile", "toile d'araignée", "aucune expérience professionnelle antérieur", "l'industrie m'attire", "à l'intention de",
             "une demande d'emploi", "standard exemplaire", "j'accomplirai toutes mes taches pour devenir un standard exemplaire",
             "pret a l'emploi", "sensibilisation au commerce", "s'assurer", "bégayer", "taquiner", "une pierre deux coups", "pertinent", "se faire avoir, duper",
             "lanceur d'alerte", "a lot of (synonym)", "ils font du télétravail", "l'éspérence de vie", "mordre", "mouvements", "éclaircissements", "imprévisible")



for i in range(5):
    
    
    robot = random.choice(questions)
    
    print(robot)
    
    you = input("Translate the word or phrase: ")



    if robot == "commerce" and you == "trade":
        print("Correct")
        
    elif robot == "inciter" and you == "to spur":
        print("Correct")
        
    elif robot == "étouffant" and you == "stifling":
        print("Correct")
        
    elif robot == "est monté en flèche" and you == "skyrocketed":
        print("Correct")
        
    elif robot == "écoulement" and you == "flowing":
        print("Correct")
        
    elif robot == "maitrise" and you == "fluency":
        print("Correct")

    elif robot == "versatile (synonym)" and you == "multitasker":
        print("Correct")
        
    elif robot == "hors ligne" and you == "offline":
        print("Correct")
        
    elif robot == "rarement" and you == "seldom":
        print("Correct")
        
    elif robot == "je vais rarement à la plage" and you == "I seldom go to the beach because I live far from the cost":
        print("Correct")
        
    elif robot == "modèle" and you == "template" or "pattern":
        print("Correct")
        
    elif robot == "toile" and you == "canva":
        print("Correct")
        
    elif robot == "aucune expérience professionnelle antérieur" and you == "no previous experience":
        print("Correct")
        
    elif robot == "une demande d'emploi" and you == "job application":
        print("Correct")
        
    elif robot == "l'industrie m'attire" and you == "the industry is appealing to me":
        print("Correct")
        
    elif robot == "standard exemplaire" and you == "examplary standard":
        print("Correct")
        
    elif robot == "j'accomplirai toutes mes taches pour devenir un standard exemplaire" and you == "I will perform all my duties to become an examplary standard":
        print("Correct")
        
    elif robot == "pret a l'emploi" and you == "ready made":
        print("Correct")
        
    elif robot == "sensibilisation au commerce" and you == "awarness of commercial":
        print("Correct")

    elif robot == "s'assurer" and you == "to ensure":
        print("Correct")
        
    elif robot == "bégayer" and you == "sluttering":
        print("Correct")
        
    elif robot == "taquiner" and you == "to tease":
        print("Correct")
        
    elif robot == "une pierre deux coups" and you == "kill two birds with one stone":
        print("Correct")
        
    elif robot == "pertinent" and you == "relevant":
        print("Correct")
        
    elif robot == "se faire avoir, duper" and you == "to fool":
        print("Correct")
        
    elif robot == "lanceur d'alerte" and you == "whistleblower":
        print("Correct")
        
    elif robot == "a lot of (synonym)" and you == "a litany of":
        print("Correct")
        
    elif robot == "ils font du télétravail" and you == "they are telecommute":
        print("Correct")

    elif robot == "l'éspérence de vie" and you == "life expectancy":
        print("Correct")
        
    elif robot == "mordre" and you == "to bite":
        print("Correct")
        
    elif robot == "mouvements" and you == "motions":
        print("Correct")
        
    elif robot == "éclaircissements" and you == "enlightenments":
        print("Correct")
        
    elif robot == "imprévisible" and you == "unpredictable":
        print("Correct")
        
    else:
        print("Incorrect")
        