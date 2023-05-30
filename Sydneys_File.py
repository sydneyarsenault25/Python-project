scoremusic = 0
scoresports = 0
scoremovies = 0
score = 0

catpick = input("Welcome to Trvia Night!! Pick one olf the three following categories: \n  - Music \n  - Sports \n  - Movies")
if catpick == "Music":
    categories1 = True and questions1 = True
    categories2 = False and questions2 = False
    categories3 = False and questions3 = False
    print("You've selected Music. Get ready to guess songs based on their lyrics!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    q1music = input("XXX lyrics are from the song _____ by _____.")
    a1music = "ANSWER"
    if q1music == a1music:
        scoremusic += 1
        score += 1
    if q2music == a2music:
        scoremusic += 1
        score += 1
    if q3music == a3music:
        scoremusic += 1
        score += 1
    SERIALIZE

elif catpick == "Sports":
    categories2 = True and questions2 = True
    categories1 = False and questions1 = False
    categories3 = False and questions3 = False
    print("You've selected sports. Get ready to show off your sports knowledge!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    
    if q1sports == a1sports:
        scoresports += 1
        score += 1
    if q2sports == a2sports:
        scoresports += 1
        score += 1
    if q3sports == a3sports:
        scoresports += 1
        score += 1
    SERIALIZE

elif catpick == "Movies":
    categories3 = True and questions3 = True
    categories2 = False and questions2 = False
    categories1 = False and questions1 = False
    print("You've selected moveis. Get ready to guess the movie based on their descriptions and fun facts!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
    q1movies = input("Disney's first movie ever released is... _____")
    a1movies = "Snow White"
    if a1movies == q1movies:
        scoremovies += 1
        score += 1
    elif q1movies == "Snow White and the 7 Dwarves":
        scoremovies += 1.5
        score += 1.5
    q2movies = input("Quentin Tarantino's most popular film is... _____, released in... _____")
    a2movies = "Pulp Fiction, 1994"
    if "Pulp Fiction" in q2movies:
        scoremovies += 0.5
        score += 0.5
    if "1994" in q2movies:
        scoremovies += 0.5
        score += 0.5
    q3movies = input("In 'The Adam Project', Ryan Reynolds played a character named... _____")
    a3movies = "Adam Reed"
    if a3movies == q3movies:
        scoremovies += 1
        score += 1
    elif q3movies == "Adam":
        scoremovies += 0.5
        score += 0.5
    SERIALIZE

else:
    print("Please enter Music, Sports, or Movies.")