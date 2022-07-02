from util import loop, waiting_screen

while True:
    end_game = loop()
    if end_game: break
    end_game = waiting_screen()
    if end_game: break
