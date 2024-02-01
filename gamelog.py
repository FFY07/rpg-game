'''

(yea.. game_log  )
( for now it cannot save log in a file)
^^^           ^^^             ^^^
need to work on this if possible 


'''





import gui.screen as sc
import resources.font as font 
game_logs = []


def draw_game_logs():
    with open("gamelog.txt", "w") as f:
        y = 433 # initial y value
        for log in game_logs[-4:]:  # display only the last 4 logs
            text_surface = font.game_log_font.render(log, True, (255, 0, 0))
            sc.screen.blit(text_surface, (520, y))
            y += 23  # increment y value for next log
            
        # Writes to file
        for log in game_logs:
            f.write(f"{log.strip()}\n")
        