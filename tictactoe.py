
'''while True:
    # Set the game up here
    board = ['#'] + [None] * 9
    game_on = True
    player = choose_first()
    if player == 'Player1':
        markerPlayer1 = player_input()
        if markerPlayer1 == 'X':
            markerPlayer2 = 'O'
        else:
            markerPlayer2 = 'X'
    else:
        markerPlayer2 = player_input()
        if markerPlayer2 == 'X':
            markerPlayer1 = 'O'
        else:
            markerPlayer1 = 'X'

    while game_on:
        markerPlayer1 = ''
        markerPlayer2 = ''
        if not full_board_check(board):
            #Player 1 Turn
            if player == 'Player1':
                #As board is not full, continue until the player chooses a correct postion
                while True:
                    position = player_choice(board)
                    if position is not None:
                        place_marker(board, makerPlayer1, position)
                        break
                player = 'Player2'
                if win_check(markerPlayer1):
                    print('Player1 wins')
                    break
            # Player2's turn.
            else:
                #As board is not full, continue until the player chooses a correct postion
                while True:
                    position = player_choice(board)
                    if position is not None:
                        place_marker(board, makerPlayer2, position)
                        break
                player = 'Player1'
                if win_check(markerPlayer2):
                    print('Player2 wins')
                    break
        else:
            game_on = False
    replay()
    if not replay():
        break'''