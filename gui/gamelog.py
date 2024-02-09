import gui.screen as sc
import resources.font as font 
game_logs = []

HEIGHT_SPACING = 23
def draw_game_logs():
    with open("gamelog.txt", "w") as f:
        y = 433 # initial y value
        for log in game_logs[-4:]:  # display only the last 4 logs
            text_surface = font.game_log_font.render(log, True, (255, 0, 0))
            sc.screen.blit(text_surface, (720, y))
            y += HEIGHT_SPACING  # increment y value for next log
            
        # Writes to file
        for log in game_logs:
            f.write(f"{log.strip()}\n")
        