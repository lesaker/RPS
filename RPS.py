# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    anti = { "R":"P","P":"S","S":"R" } 

    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)
    guess = "S"
    n = 7

    if len(opponent_history) <= n:
        return guess
    
    last_n = "".join(opponent_history[-n:])

    if last_n in play_order.keys():
        play_order[last_n] += 1
    else:
        play_order[last_n] = 1

    potential_plays = [
        "".join(opponent_history[-(n-1):]) + "R",
        "".join(opponent_history[-(n-1):]) + "P",
        "".join(opponent_history[-(n-1):]) + "S",
    ]

    for element in potential_plays:
        if not element in play_order:
            play_order[element] = 0
    
    opponent_guess = max(potential_plays, key=play_order.get)[-1]

    final_guess = anti[opponent_guess]
    return final_guess
