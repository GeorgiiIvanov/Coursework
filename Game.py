import pygame
from random import randint
import time
from PyQt5 import uic


def newGame(bool):
    global field
    global white, black
    global x, y, player, poluhod
    global hit, end, winW, winB, bot
    global dam
    global moves, board
    pygame.init()
    field = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Двухходовые шашки - Поддавки")
    field.fill((255, 255, 255))
    board = [[0, -1, 0, -1, 0, -1, 0, -1],
             [-1, 0, -1, 0, -1, 0, -1, 0],
             [0, -1, 0, -1, 0, -1, 0, -1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0]]
    white = pygame.image.load("w.png")
    black = pygame.image.load("b.png")
    white = pygame.transform.scale(white, (75, 75))
    black = pygame.transform.scale(black, (75, 75))
    player = 1
    x = -1
    y = -1
    hit = False
    poluhod = 1
    moves = []
    winW = False
    winB = False
    end = False
    bot = bool
    f = pygame.font.SysFont(None, 48)
    dam = f.render("D", True, (255, 0, 0))
    for i in range(8):
        moves.append([])
        for j in range(8):
            moves[i].append(-1)

def switch():
    global player
    if player == 1:
        player = -1
    else:
        player = 1


def drow_board():
    for i in range(8):
        for j in range(8):
            if i % 2 != 0 and j % 2 == 0:
                pygame.draw.rect(field, (40, 40, 40), (i * 75, j * 75, 75, 75))
            if i % 2 == 0 and j % 2 != 0:
                pygame.draw.rect(field, (40, 40, 40), (i * 75, j * 75, 75, 75))
            if board[j][i] == 1:
                field.blit(white, (i * 75, j * 75))
            if board[j][i] == -1:
                field.blit(black, (i * 75, j * 75))
            if board[j][i] == 2:
                field.blit(white, (i * 75, j * 75))
                field.blit(dam, (i * 75 + 27, j * 75 + 23))
            if board[j][i] == -2:
                field.blit(black, (i * 75, j * 75))
                field.blit(dam, (i * 75 + 27, j * 75 + 23))
            if moves[j][i] == 0 or moves[j][i] == 1:
                pygame.draw.rect(field, (0, 255, 0), (i * 75, j * 75, 75, 75), 3)
            if moves[j][i] == 2:
                pygame.draw.rect(field, (255, 0, 0), (i * 75, j * 75, 75, 75), 3)


def way():
    global hit
    for i in range(8):
        for j in range(8):
            moves[i][j] = -1
    if board[x][y] == player:
        if player == 1:
            if (x - 1 >= 0) and (y - 1 >= 0) and board[x - 1][y - 1] == 0:
                moves[x - 1][y - 1] = 0
            if (x - 1 >= 0) and (y + 1 <= 7) and board[x - 1][y + 1] == 0:
                moves[x - 1][y + 1] = 0
        if player == -1:
            if (x + 1 <= 7) and (y - 1 >= 0) and board[x + 1][y - 1] == 0:
                moves[x + 1][y - 1] = 0
            if (x + 1 <= 7) and (y + 1 <= 7) and board[x + 1][y + 1] == 0:
                moves[x + 1][y + 1] = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0 and (x + i >= 0) and (x + i <= 7) and (y + j >= 0) and (y + j <= 7) and board[x + i][y + j] != 0 and board[x + i][y + j] != board[x][y] and board[x + i][y + j] != player * 2:
                    ii = i
                    jj = j
                    if ii == 1:
                        ii += 1
                    else:
                        ii -= 1
                    if jj == 1:
                        jj += 1
                    else:
                        jj -= 1
                    if (x + ii >= 0) and (x + ii <= 7) and (y + jj >= 0) and (y + jj <= 7) and board[x + ii][y + jj] == 0:
                        moves[x + ii][y + jj] = 1
    if board[x][y] == player * 2:
        LeftUpDiag, RightUpDiag, RightDownDiag, LeftDownDiag = 0, 0, 0, 0
        for i in range(1, 8):
            if (x - i >= 0) and (y - i >= 0) and LeftUpDiag < 2:
                if board[x - i][y - i] == 0:
                    moves[x - i][y - i] = LeftUpDiag
                if board[x - i][y - i] == player or board[x - i][y - i] == player * 2:
                    LeftUpDiag = 2
                if board[x - i][y - i] != player and board[x - i][y - i] != 0:
                    if (x - i - 1 >= 0) and (y - i - 1 >= 0) and board[x - i - 1][y - i - 1] == 0:
                        LeftUpDiag = 1
            if (x - i >= 0) and (y + i <= 7) and RightUpDiag < 2:
                if board[x - i][y + i] == 0:
                    moves[x - i][y + i] = RightUpDiag
                if board[x - i][y + i] == player or board[x - i][y + i] == player * 2:
                    RightUpDiag = 2
                if board[x - i][y + i] != player and board[x - i][y + i] != 0:
                    if (x - i - 1 >= 0) and (y + i + 1 <= 7) and board[x - i - 1][y + i + 1] == 0:
                        RightUpDiag = 1

            if (x + i <= 7) and (y + i <= 7) and RightDownDiag < 2:
                if board[x + i][y + i] == 0:
                    moves[x + i][y + i] = RightDownDiag
                if board[x + i][y + i] == player or board[x + i][y + i] == player * 2:
                    RightDownDiag = 2
                if board[x + i][y + i] != player and board[x + i][y + i] != 0:
                    if (x + i + 1 <= 7) and (y + i + 1 <= 7) and board[x + i + 1][y + i + 1] == 0:
                        RightDownDiag = 1

            if (x + i <= 7) and (y - i >= 0) and LeftDownDiag < 2:
                if board[x + i][y - i] == 0:
                    moves[x + i][y - i] = LeftDownDiag
                if board[x + i][y - i] == player or board[x + i][y - i] == player * 2:
                    LeftDownDiag = 2
                if board[x + i][y - i] != player and board[x + i][y - i] != 0:
                    if (x + i + 1 <= 7) and (y - i - 1 >= 0) and board[x + i + 1][y - i - 1] == 0:
                        LeftDownDiag = 1
    if hit:
        for i in range(8):
            for j in range(8):
                if moves[i][j] == 0:
                    moves[i][j] = -1


def moving(x2, y2):
    global hit
    global bot
    global x, y, poluhod
    if poluhod == 1:
        board[x2][y2] = board[x][y]
        board[x][y] = 0
        hit0 = False
        if board[x2][y2] == 1 and x2 == 0:
            board[x2][y2] = player * 2
        if board[x2][y2] == -1 and x2 == 7:
            board[x2][y2] = player * 2
        if abs(x - x2) > 1:
            xx = x2
            yy = y2
            while xx != x and yy != y:
                if xx > x:
                    xx -= 1
                else:
                    xx += 1
                if yy > y:
                    yy -= 1
                else:
                    yy += 1
                if board[xx][yy] == player * -1 or board[xx][yy] == player * -2:
                    hit0 = True
                    board[xx][yy] = 0
        EndGame()
        hit1 = False
        if hit0:
            x = x2
            y = y2
            way()
            for i in range(8):
                for j in range(8):
                    if moves[i][j] == 0:
                        moves[i][j] = -1
                    if moves[i][j] == 1:
                        hit1 = True
            if hit1:
                hit = True
            else:
                hit = False
        if not hit1:
            for i in range(8):
                for j in range(8):
                    moves[i][j] = -1
            x = -1
            y = -1
            if player < 0 and bot:
                time.sleep(1)
                drow_board()
                pygame.display.update()
            else:
                drow_board()
                pygame.display.update()
            poluhod = 2
            hit = False
            requiredHit()
    else:
        board[x2][y2] = board[x][y]
        board[x][y] = 0
        hit0 = False
        if board[x2][y2] == 1 and x2 == 0:
            board[x2][y2] = player * 2
        if board[x2][y2] == -1 and x2 == 7:
            board[x2][y2] = player * 2
        if abs(x - x2) > 1:
            xx = x2
            yy = y2
            while xx != x and yy != y:
                if xx > x:
                    xx -= 1
                else:
                    xx += 1
                if yy > y:
                    yy -= 1
                else:
                    yy += 1
                if board[xx][yy] == player * -1 or board[xx][yy] == player * -2:
                    hit0 = True
                    board[xx][yy] = 0
        EndGame()
        hit1 = False
        if hit0:
            x = x2
            y = y2
            way()
            for i in range(8):
                for j in range(8):
                    if moves[i][j] == 0:
                        moves[i][j] = -1
                    if moves[i][j] == 1:
                        hit1 = True
            if hit1:
                hit = True
            else:
                hit = False
        if not hit1:
            for i in range(8):
                for j in range(8):
                    moves[i][j] = -1
            x = -1
            y = -1
            if player < 0 and bot:
                time.sleep(1)
                drow_board()
                pygame.display.update()
            else:
                drow_board()
                pygame.display.update()
            switch()
            poluhod = 1
            hit = False
            requiredHit()
    if player < 0 and not end and bot:
        randomBOT()


def requiredHit():
    global hit
    for i in range(8):
        for j in range(8):
            if board[i][j] == player:
                for n in range(-1, 2):
                    for k in range(-1, 2):
                        if (i + n >= 0) and (i + n <= 7) and (j + k >= 0) and (j + k <= 7) and (board[i + n][j + k] == player * -1 or board[i + n][j + k] == player * -2):
                            ii = n
                            jj = k
                            if ii == 1:
                                ii += 1
                            else:
                                ii -= 1
                            if jj == 1:
                                jj += 1
                            else:
                                jj -= 1
                            if (i + ii >= 0) and (i + ii <= 7) and (j + jj >= 0) and (j + jj <= 7) and board[i + ii][j + jj] == 0:
                                moves[i][j] = 2
                                hit = True
            if board[i][j] == player * 2:
                for k in range(1, 8):
                    if (i - k >= 0) and (j - k >= 0) and (board[i - k][j - k] == player or board[i - k][j - k] == player * 2):
                        break
                    if (i - k >= 0) and (j - k >= 0) and (board[i - k][j - k] == player * -1 or board[i - k][j - k] == player * -2):
                        if (i - k - 1 >= 0) and (j - k - 1 >= 0) and board[i - k - 1][j - k - 1] == 0:
                            moves[i][j] = 2
                            hit = True
                for k in range(1, 8):
                    if (i - k >= 0) and (j + k <= 7) and (board[i - k][j + k] == player or board[i - k][j + k] == player * 2):
                        break
                    if (i - k >= 0) and (j + k <= 7) and (board[i - k][j + k] == player * -1 or board[i - k][j + k] == player * -2):
                        if (i - k - 1 >= 0) and (j + k + 1 <= 7) and board[i - k - 1][j + k + 1] == 0:
                            moves[i][j] = 2
                            hit = True
                for k in range(1, 8):
                    if (i + k <= 7) and (j + k <= 7) and (board[i + k][j + k] == player or board[i + k][j + k] == player * 2):
                        break
                    if (i + k <= 7) and (j + k <= 7) and (board[i + k][j + k] == player * -1 or board[i + k][j + k] == player * -2):
                        if (i + k + 1 <= 7) and (j + k + 1 <= 7) and board[i + k + 1][j + k + 1] == 0:
                            moves[i][j] = 2
                            hit = True
                for k in range(1, 8):
                    if (i + k <= 7) and (j - k >= 0) and (board[i + k][j - k] == player or board[i + k][j - k] == player * 2):
                        break
                    if (i + k <= 7) and (j - k >= 0) and (board[i + k][j - k] == player * -1 or board[i + k][j - k] == player * -2):
                        if (i + k + 1 <= 7) and (j - k - 1 >= 0) and board[i + k + 1][j - k - 1] == 0:
                            moves[i][j] = 2
                            hit = True






def randomBOT():
    global x, y
    flag = False
    while not flag:
        a = randint(0, 7)
        b = randint(0, 7)
        if board[a][b] < 0:
            x = a
            y = b
            way()
            for v in range(8):
                for c in range(8):
                    if not flag and moves[v][c] > -1:
                        flag = True
                        moving(v, c)







def EndGame():
    global board
    global winW, winB, end
    global window4
    numW = 0
    numB = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] > 0:
                numW += 1
            if board[i][j] < 0:
                numB += 1
    if numW == 0:
        end = True
        winW = True
    if numB == 0:
        end = True
        winB = True
    if end:
        def click_ButtonNewgame():
            newGame(bot)
            window4.close()
        def click_ButtonExit():
            window4.close()
            exit()
        Form4, Window4 = uic.loadUiType("endwindow.ui")
        window4 = Window4()
        form4 = Form4()
        form4.setupUi(window4)
        window4.show()
        if winB:
            form4.labelWin.setText("победили черные")
        if winW:
            form4.labelWin.setText("победили белые")
        form4.ButtonNewgame.clicked.connect(click_ButtonNewgame)
        form4.ButtonExit.clicked.connect(click_ButtonExit)




def game():
    global x, y
    drow_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            click = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if click[0]:
                if pos[0] < 600 and pos[1] < 600:
                    if board[pos[1] // 75][pos[0] // 75] == player or board[pos[1] // 75][pos[0] // 75] == player * 2:
                        x = pos[1] // 75
                        y = pos[0] // 75
                        way()
                    if moves[pos[1] // 75][pos[0] // 75] > -1:
                        x2 = pos[1] // 75
                        y2 = pos[0] // 75
                        moving(x2, y2)
            drow_board()
            pygame.display.update()