import chess
import ai

def main():
    winner = 0
    screen = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    while 1:
        chess.printScreen(screen)
        n = list(input('input(xy):'))
        n[0] = int(n[0])
        n[1] = int(n[1])
        if screen[n[0]][n[1]] == ' ':
            screen[n[0]][n[1]] = 'o'
        chess.printScreen(screen)
        winner = chess.win(screen,'o')
        if winner == 'o':
            print('O win!')
            break
        ai.isline(screen,'x')
        winner = chess.win(screen,'x')
        chess.printScreen(screen)
        if winner == 'x':
            print('X win!')
            break
        if ' ' not in screen[0] and ' ' not in screen[1] and ' ' not in screen[2]:
            print('No one win!')
            break
main()