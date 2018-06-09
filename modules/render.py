import curses

class Render:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.world = ""
        self.current_level = 1
        
    def update_world(self, world):
        self.world = world
    
    def refresh(self):
        #print(self.world[self.current_level])
        for index_y, y in enumerate(self.world[self.current_level]):
            print(y)
            for index_x, x in enumerate(y):
                self.stdscr.addstr(index_y*2, index_x*2, "A")

        self.stdscr.refresh()
        
    def stop(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
