import random

questions = ["étendue engloutissante", "il regarde l'étendue engloutissant", "chagrin", "sans relache", "je poursuis sans relache mon objectif",
             "redoutable, effrayant", "significatif", "je suis un nouveau diplomé", "un créneau horaire", "puis-je", "merci de me rappeler",
             "évaluer", "rarement", "l'auditeur", "on peut soit dire...", "compétences", "précis", "avec précision", "mon niveau dans cette langue",
             "départ", "paysage", "accusation", "canular", "apprivoiser", "dévoué", "rude, dure, sévère", "épreuve", "pour approfondir", "pour approfondir le sujet",
             "un coup d'oeil", "cadeaux", "avec facilité", "baignoire"]



for i in range(4):
    
    
    robot = random.choice(questions)
    
    print(robot)
    
    you = input("Tranlate the word ou the phrase: ")
    
    
    
    
    if robot == "étendue englouissante" and you == "engulfing expanse":
        print("correct")
        
    elif robot == "il regarde l'étendue engloutissant" and you == "he look over the engulfing expanse":
        print("correct")
        
    elif robot == "chagrin" and you == "sorrow":
        print("correct")
    
    elif robot == "sans relache" and you == "relentlessly, tirelessly":
        print("correct")
        
    elif robot == "je poursuis sans relache mes objectifs" and you == "I relentlessly persue my goal":
        print("correct")
        
    elif robot == "redoutable, effrayant" and you == "fearsome":
        print("correct")
        
    elif robot == "significatif" and you == "meaningful":
        print("correct")
        
    elif robot == "je suis un nouveau diplomé" and you == "I am a new graduate":
        print("correct")
        
    elif robot == "un créneau horaire" and you == "a time slot":
        print("correct")
        
    elif robot == "puis-je" and you == "may I":
        print("correct")
        
    elif robot == "merci de me rappeler" and you == "thanks to calling me back":
        print("correct")
        
    elif robot == "évaluer" and you == "to assess":
        print("correct")
        
    elif robot == "rarement" and you == "seldom":
        print("correct")
        
    elif robot == "l'auditeur" and you == "the hearer":
        print("correct")
        
    elif robot == "on peut soit dire..." and you == "we can either say...":
        print("correct")
        
    elif robot == "compétences" and you == "profencies , skills":
        print("correct")
        
    elif robot == "précis" and you == "accurate":
        print("correct")
        
    elif robot == "avec précision" and you == "accurately":
        print("correct")
        
    elif robot == "mon niveau dans cette langue" and you == "my accurency in this language":
        print("correct")
        
    elif robot == "départ" and you == "departure":
        print("correct")
        
    elif robot == "paysage" and you == "landscape, scenery":
        print("correct")
        
    elif robot == "accusation" and you == "indictement":
        print("correct")
        
    elif robot == "canular" and you == "hoax":
        print("correct")
        
    elif robot == "apprivoiser, dompter, maitriser" and you == "to tame":
        print("correct")
        
    elif robot == "dévoué" and you == "devoted":
        print("correct")
        
    elif robot == "rude, dure, sévère" and you == "harsh , harsh":
        print("correct")
        
    elif robot == "pour approfondir" and you == "to dive deep into":
        print("correct")
        
    elif robot == "pour approfondir le sujet" and you == "to dive deep into the issue":
        print("correct")
        
    elif robot == "un coup d'oeil" and you == "a peek":
        print("correct")
        
    elif robot == "cadeaux" and you == "godies, gifts":
        print("correct")
        
    elif robot == "avec facilité" and you == "with ease":
        print("correct")
        
    elif robot == "baignoire" and you == "bathtub":
        print("correct")
        
    else:
        print("Incorrect")
        