import random

def empty_board():
    return [0]*9

win_lines = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner(board):
    for a, b, c in win_lines:
        s = board[a] + board[b] + board[c]
        if s == 3:
            return 1
        if s == -3:
            return -1
    if 0 not in board:
        return 0
    return None

Q = {}

def get_Q(state, action):
    return Q.get((tuple(state), action), 0.0)

def choose_actions(board, epsilon):
    empty_cells = [i for i in range(9) if board[i] == 0]

    if random.random() < epsilon:
        return random.choice(empty_cells)

    qs = [(get_Q(board, a), a) for a in empty_cells]
    return max(qs)[1]

ALPHA = 0.1
GAMMA = 0.9

def update_Q(state, action, reward, next_state):
    old_q = get_Q(state, action)
    future_qs = [get_Q(next_state, a) for a in range(9) if next_state[a] == 0]
    max_future_q = max(future_qs) if future_qs else 0

    new_q = old_q + ALPHA * (reward + GAMMA * max_future_q - old_q)
    Q[(tuple(state), action)] = new_q

def training(episodes=50000):
    epsilon = 1.0

    for _ in range(episodes):
        board = empty_board()
        history = []

        while True:
            state = board.copy()
            action = choose_actions(board, epsilon)
            board[action] = 1

            result = check_winner(board)
            if result is not None:
                reward = 1 if result == 1 else 0.5 if result == 0 else -1
                for s, a in history:
                    update_Q(s, a, reward, board)
                break

            opp_move = random.choice([i for i in range(9) if board[i] == 0])
            board[opp_move] = -1

            result = check_winner(board)
            if result is not None:
                reward = -1 if result == -1 else 0.5
                for s, a in history:
                    update_Q(s, a, reward, board)
                break

            history.append((state, action))

        epsilon = max(0.01, epsilon * 0.999)
