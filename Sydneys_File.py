score = 0
catpick = input("Welcome to Trvia Night!! Pick one olf the three following categories: \n  - Music \n  - Sports \n  - Movies")
if catpick == "Music":
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

elif catpick == "Movies":
    categories3 == True and questions3 == True
    categories2 == False and questions2 == False
    categories1 == False and questions1 == False
    print("You've selected moveis. Get ready to guess the movie based on their descriptions and fun facts!")
    print("Great! Time for the first question. \n Enter answers with proper capitalization and, if there is a double-answer, enter your answers as X, Y.")
