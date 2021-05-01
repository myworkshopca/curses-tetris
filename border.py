import curses

def tetris(stdscr):

    sh, sw = stdscr.getmaxyx()

    # find the border for game board.
    border_ch = chr(127999)

    # paint the top and bottom border
    for x in range(5, 24 + 5):
        stdscr.addstr(2, x, border_ch)
        stdscr.addstr(23, x, border_ch)
    # paint the left and right border
    for y in range(2, 24):
        stdscr.addstr(y, 5, border_ch)
        stdscr.addstr(y, 5 + 24, border_ch)

    stdscr.getch()

curses.wrapper(tetris)
