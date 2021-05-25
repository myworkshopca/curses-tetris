import curses

# Tetris page on wikipedia: https://en.wikipedia.org/wiki/Tetris

# characters for building Tetriminos could be found here:
# - http://xahlee.info/comp/unicode_index.html
#
def paintTetrimino(stdscr, type):

    # 9619 - ▓, 9609 - ▉, 9608 - █, 9611 - ▋
    # 9634 - ▢,
    unit_ch = chr(9634)

    stdscr.addstr(4, 2, chr(9608))

    if type == 'square':
        # 2 x 2 tetrimino
        stdscr.addstr(5, 2, unit_ch)
        stdscr.addstr(5, 4, unit_ch)
        stdscr.addstr(6, 2, unit_ch)
        stdscr.addstr(6, 4, unit_ch)
    elif type == 'line':
        for x in range(2, 10, 2):
            stdscr.addstr(8, x, unit_ch)

def tetris(stdscr):

    curses.curs_set(False)

    stdscr.addstr(2, 2, 'Painting tetriminos!')
    
    paintTetrimino(stdscr, 'square')
    paintTetrimino(stdscr, 'line')

    stdscr.getch()

curses.wrapper(tetris)