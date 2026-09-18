opponent_history = []
my_history = []
strategy_counter = {}

def player(prev_play):
    global opponent_history, my_history, strategy_counter

    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()
        my_history.clear()
        strategy_counter.clear()

    if len(opponent_history) < 3:
        my_next_move = "R"
        my_history.append(my_next_move)
        return my_next_move

    n = 3
    recent_sequence = "".join(opponent_history[-n:])
    
    if len(opponent_history) > n:
        prev_sequence = "".join(opponent_history[-(n + 1):-1])
        last_move = opponent_history[-1]
        key_str = prev_sequence + last_move
        strategy_counter[key_str] = strategy_counter.get(key_str, 0) + 1

    predicted_next_move = max(
        ["R", "P", "S"],
        key=lambda m: strategy_counter.get(recent_sequence + m, 0)
    )

    counters = {"R": "P", "P": "S", "S": "R"}
    my_next_move = counters[predicted_next_move]

    my_history.append(my_next_move)
    return my_next_move