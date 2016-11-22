    player1 = input("Player 1: ?")
    player2 = input("Player 2: ?")

    if (player1 == 'rock' and player2 == 'scissors'):
        print "Player 1 wins."

    elif (player1 == 'rock' and player2 == 'rock'):
        print "Tie"

    elif (player1 == 'scissors' and player2 == 'paper'):
        print "Player 1 wins."

    elif (player2 == 'scissors' and player2 == 'scissors'):
        print "Tie"

    elif (player1 == 'paper' and player2 == 'paper'):
        print "Tie"

    elif (player1 == 'paper' and player2 == 'scissors'):
        print "Player 2 wins."

    elif (player1 == 'rock'and player2 == 'paper'):
        print "Player 2 wins."

    elif (player1 == 'paper' and player2 == 'rock'):
        print "Player 2 wins."

    elif (player1 == 'scissors' and player2 == 'rock'):
        print "Player 2 wins."
    else:
        print "This is not a valid object selection."
