score = 0
catpick = input("Welcome to Trvia Night!! Pick one olf the three following categories: \n  - Music \n  - Sports \n  - Movies")
if catpick == "Music":
<<<<<<< HEAD
    print("You've selected music. Get ready to guess the answers based on their descriptions and your knowledge of fun facts!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    music_questions = {
        "In 1967, what band released the hit song 'Ruby Tuesday'? " : "The Rolling Stones",
        "Who is referred to as the Queen of Pop? " : "Madonna",
        "What decade is the hit single 'Love Shack' by the B-52's from?(Spell it out) " : "Eighties",
        "Justin Timberlake started his career as a member of what band? " : "NSYNC",
        "Which female singer released 'Rolling in the Deep? " : "Adele",
        "Which singer is a godmother to Elton John's two sons? " : "Lady Gaga"
    }
    for question, answer in mu.items():
        guess = input (question + ": ")
        if guess == answer:
            print ("Correct")
            print()
            scoremusic += 1
            score += 1
        else:
            print ("Incorrect")
            print()

elif catpick == "Sports":
    print("You've selected sports. Get ready to guess the answers based on their descriptions and your knowledge of fun facts!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    sports_questions = {
        "The Walt Disney Company founded a professional sports franchise in 1993 and based the new team's name on a successful 1992 film. What sport did this team play?" : "Hockey",
        "What is the only sport to be played on the moon? " : "Golf",
        "During which inning is 'Take Me Out to the Ballgame' traditionally sung? (Only answer with number) " : "7",
        "In what sports league do the Minnesota Lynx play? " : "WNBA",
        "What since-relocated baseball team did Babe Ruth coach for a year after retiring? " : "Dodgers",
        "Only 1 NFL team has their logo on one side of the helmet and NOT on the other side. What team is this? (city not needed in team name) " : "Steelers"
    }
    for question, answer in sports_questions.items():
        guess = input (question + ": ")
        if guess == answer:
            print ("Correct")
            print()
            scoresports += 1
            score += 1
        else:
            print ("Incorrect")
            print()

elif catpick == "Movies":
    print("You've selected moveis. Get ready to guess the movie and actor facts based on their descriptions and fun facts!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    movie_questions = {
        "For which 1964 musical blockbuster did Julie Andrews win the Academy Award for Best Actress? " : "Mary Poppins",
        "How many suns does Luke's home planet of Tatooine have in Star Wars? " : "2",
        "What was the first James Bond Movie ever made? " : "Dr. No",
        "Goose, Jester, Hollywood, and Wolfman are nicknames of some characters in which 1986 movie? " : "Top Gun",
        "What is Indiana Jones' weapon of choice? " : "Whip",
        "Stan Lee made his final cameo in which Marvel movie? (include no spaces in your answer.) " : "Endgame"
    }
    for question, answer in movie_questions.items():
        guess = input (question + ": ")
        if guess == answer:
            print ("Correct")
            print()
            scoremovies += 1
            score += 1
        else:
            print ("Incorrect")
            print()

=======
    categories1 == True and questions1 == True
    categories2 == False and questions2 == False
    categories3 == False and questions3 == False
    print("You've selected Music. Get ready to guess songs based on their lyrics!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    q1music = input("XXX lyrics are from the song _____ by _____.")
    a1music = "ANSWER"
    if q1music == a1music:
        score += 1

elif catpick == "Sports":
    categories2 == True and questions2 == True
    categories1 == False and questions1 == False
    categories3 == False and questions3 == False
    print("You've selected sports. Get ready to show off your sports knowledge!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")

>>>>>>> 1a4b441f403582a5d7b0504f4684e007076cfaf2
