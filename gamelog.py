import screen as sc
import font 
game_logs = []


def draw_game_logs():
    y = 433 # initial y value
    for log in game_logs[-4:]:  # display only the last 4 logs
        text_surface = font.game_log_font.render(log, True, (255, 0, 0))
        sc.screen.blit(text_surface, (520, y))
        y += 23  # increment y value for next log