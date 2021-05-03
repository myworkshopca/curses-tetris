import curses

def tetris(stdscr):

    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()

    # find the border for game board.
    #border_ch = chr(127999)
    border_ch = chr(9634)
    #border_ch = chr(9609)

    #stdscr.addstr(1, 0, border_ch)
    #stdscr.addstr(1, 3, border_ch)

    # paint the top and bottom border
    for x in range(5, 24 + 5, 2):
        #stdscr.addstr(2, x, border_ch)
        stdscr.addstr(23, x, border_ch)
    # paint the left and right border
    for y in range(2, 24):
        stdscr.addstr(y, 5, border_ch)
        stdscr.addstr(y, 5 + 24, border_ch)

    stdscr.getch()

curses.wrapper(tetris)
