from chess import *
def main():
    winner = 0
    screen = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    while 1:
        printScreen(screen)
        n = list(input('input(xy)'))
        n[0] = int(n[0])
        n[1] = int(n[1])
        if screen[n[0]][n[1]] == ' ':
            screen[n[0]][n[1]] = 'x'
        printScreen(screen)
        winner = win(screen,'x')
        if winner == 'x':
            print('X win!')
            break
        n = list(input('input(xy)'))
        n[0] = int(n[0])
        n[1] = int(n[1])
        if screen[n[0]][n[1]] == ' ':
            screen[n[0]][n[1]] = 'o'
        winner = win(screen,'o')
        if winner == 'o':
            print('O win!')
        print(screen)
        if ' ' not in screen[0] and ' ' not in screen[1] and ' ' not in screen[2]:
            print('No one win!')
            break
main()