import curses

def draw_menu(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    menu = ["Start", "Settings", "About", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()

        # Display menu options
        for idx, item in enumerate(menu):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))  # Highlight selection
                stdscr.addstr(idx + 2, 5, item)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 2, 5, item)

        stdscr.refresh()

        key = stdscr.getch()

        # Handle input
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord("\n"):  # Enter key
            stdscr.clear()
            stdscr.addstr(5, 5, f"You selected: {menu[current_row]}")
            stdscr.refresh()
            stdscr.getch()  # Wait for user input
            if menu[current_row] == "Exit":
                break
        elif key == ord("q"):  # Press 'q' to exit
            break

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()


# ----------
# macos

# windows
# pip install windows-curses