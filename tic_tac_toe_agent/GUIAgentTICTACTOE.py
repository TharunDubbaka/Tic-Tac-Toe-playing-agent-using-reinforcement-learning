import pygame
import random
import time
import matplotlib.pyplot as plt

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI Learning Visualization")

win_lines = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

Q = {}
ALPHA = 0.1
GAMMA = 0.9

def empty_board():
    return [0]*9

def check_winner(board):
    for a,b,c in win_lines:
        s = board[a]+board[b]+board[c]
        if s==3: return 1
        if s==-3: return -1
    if 0 not in board: return 0
    return None

def get_Q(state, action):
    return Q.get((tuple(state), action), 0.0)

def choose_actions(board, epsilon):
    empty_cells = [i for i in range(9) if board[i]==0]
    if random.random()<epsilon:
        return random.choice(empty_cells)
    qs=[(get_Q(board,a),a) for a in empty_cells]
    return max(qs)[1]

def update_Q(state, action, reward, next_state):
    old_q = get_Q(state, action)
    future_qs = [get_Q(next_state,a) for a in range(9) if next_state[a]==0]
    max_future_q = max(future_qs) if future_qs else 0
    delta = reward + GAMMA*max_future_q - old_q
    Q[(tuple(state), action)] = old_q + ALPHA * delta
    return abs(delta)  

def grid():
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (CELL_SIZE*i,0),(CELL_SIZE*i,HEIGHT),5)
        pygame.draw.line(screen, BLACK, (0,CELL_SIZE*i),(WIDTH,CELL_SIZE*i),5)

def draw_marks(board):
    for row in range(ROWS):
        for col in range(COLS):
            x = col*CELL_SIZE
            y = row*CELL_SIZE
            if board[row*3+col]==1:
                pygame.draw.line(screen, RED, (x+20,y+20), (x+CELL_SIZE-20,y+CELL_SIZE-20),8)
                pygame.draw.line(screen, RED, (x+CELL_SIZE-20,y+20), (x+20,y+CELL_SIZE-20),8)
            elif board[row*3+col]==-1:
                pygame.draw.circle(screen, BLUE, (x+CELL_SIZE//2, y+CELL_SIZE//2), CELL_SIZE//2-20,8)

def train_visual(episodes=200, delay=0.05):
    epsilon = 1.0
    losses = []
    plt.ion() 
    fig, ax = plt.subplots()
    for ep in range(episodes):
        board = empty_board()
        history = []
        player = 1
        ep_losses = []
        while True:
            state = board.copy()
            action = choose_actions(board, epsilon)
            board[action] = player
            result = check_winner(board)
            if result is not None:
                for s,a,p in history:
                    reward = 0.5
                    if result==p: reward=1
                    elif result==-p: reward=-1
                    td_error = update_Q(s,a,reward,board)
                    ep_losses.append(td_error)
                break
            history.append((state, action, player))
            player = -player
            screen.fill(WHITE)
            grid()
            draw_marks(board)
            pygame.display.update()
            time.sleep(delay)

        if ep_losses:
            losses.append(sum(ep_losses)/len(ep_losses))
        epsilon = max(0.01, epsilon*0.995)
        if ep % 10 == 0:
            ax.clear()
            ax.plot(losses, color='red')
            ax.set_xlabel("Episode")
            ax.set_ylabel("Average TD Error (Loss)")
            ax.set_title("Learning Curve")
            plt.pause(0.001)
    plt.ioff()
    plt.show()
    return losses

def ai_self_play_visual():
    board = empty_board()
    running = True
    player = 1
    while running:
        screen.fill(WHITE)
        grid()
        draw_marks(board)
        pygame.display.update()
        pygame.time.delay(300)

        action = choose_actions(board, epsilon=0)
        board[action] = player

        result = check_winner(board)
        if result is not None:
            screen.fill(WHITE)
            grid()
            draw_marks(board)
            font = pygame.font.SysFont(None, 72)
            if result == 1: text = font.render("X won", True, RED)
            elif result == -1: text = font.render("O Won", True, BLUE)
            else: text = font.render("Draw", True, BLACK)
            screen.blit(text, (200, 250))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        player = -player

def play_with_human():
    board = empty_board()
    running = True
    game_over = False
    while running:
        screen.fill(WHITE)
        grid()
        draw_marks(board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                idx = row*3 + col
                if board[idx]==0:
                    board[idx] = -1
                result = check_winner(board)
                if result is not None:
                    game_over=True
                    break
                action = choose_actions(board, epsilon=0)
                board[action] = 1
                result = check_winner(board)
                if result is not None:
                    game_over=True
                    break

        if game_over:
            screen.fill(WHITE)
            grid()
            draw_marks(board)
            font = pygame.font.SysFont(None, 72)
            result = check_winner(board)
            if result == 1: text = font.render("The clanker won", True, RED)
            elif result == -1: text = font.render("You won", True, BLUE)
            else: text = font.render("Draw ", True, BLACK)
            screen.blit(text, (150, 250))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False

print("Training AI ")
train_visual(episodes=50000)
print("Training completed")
ai_self_play_visual()
play_with_human()
pygame.quit()
