import pygame, random

import gui.screen as scr
import resources.audio as audio

from scenes.menu import MainMenu

clock = pygame.time.Clock()
clock.tick(60)

# None of these fix the crashing... :(
pygame.mixer.pre_init(44100, 16, 2, 256)
pygame.mixer.set_num_channels(1)


# We'll use a state stack system instead of each scene having its own individual loops
class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, True
        self.actions = {
            "up": False,
            "left": False,
            "down": False,
            "right": False,
            "space": False,
            "backspace": False,
            "enter": False,
            "escape": False,
        }
        self.fps = 60
        self.clock = pygame.time.Clock()

        # Checks if user is trying to type instead of send commands
        self.typing = False

        # Holds the currently typed text in a buffer so we can assign it to a variable before clearing the buffer
        self.text_buffer = ""
        self.text_ready = False

        self.screen_width = scr.SCREEN_WIDTH
        self.screen_height = scr.SCREEN_HEIGHT

        self.canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.stack = []
        self.event_log = ["INITIALISING GAME\n"]
        self.rounds = 1

        # gives every sprite an id
        self.sprites = pygame.sprite.Group()
        self.all_units = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.stat_guis = pygame.sprite.Group()

        self.max_enemies = 3

        self.max_players = 3

        self.start()
        self.music = True
        self.sound = True
        self.volume = 0.4

        # attempt to fix sound crashing bug by preloading all sound objects into a class (did nothing)
        self.audio_handler = audio.SoundEffects()

        # # Limit sounds to one channel to prevent freezing; give it two channels here so it sounds smoother
        # self.click_channel = pygame.mixer.Channel(0)

        # # Give everything a custom channel; how many channels we can assign is limited by how many channels we've reserved
        # self.player_channel = pygame.mixer.Channel(1)
        # self.enemy_channel = pygame.mixer.Channel(2)

        # self.misc_channel = pygame.mixer.Channel(3)

        self.main_channel = pygame.mixer.Channel(0)

        self.intro_music_path = self.audio_handler.menu_bgm_path

        pygame.mixer.music.load(self.intro_music_path)
        if self.music:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(self.volume)

    def game_loop(self):
        while self.playing:
            self.event_handler()
            self.update()
            self.render()

            # print(len(self.stack))  # DEBUG
            # print(self.stack[-1])  # DEBUG
            # print(len(self.sprites)) # DEBUG

            # print(self.event_log[-1])

    def save_log(self):
        with open("gamelog.txt", "w") as f:
            for line in self.event_log:
                f.write(f"{line}\n")

    def event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.save_log()

            if event.type == pygame.KEYDOWN:
                if not self.typing:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.actions["up"] = True

                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.actions["left"] = True

                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.actions["down"] = True

                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.actions["right"] = True

                    if event.key == pygame.K_SPACE:
                        self.actions["space"] = True

                    if event.key == pygame.K_BACKSPACE:
                        self.actions["backspace"] = True

                    if event.key == pygame.K_RETURN:
                        self.actions["enter"] = True

                    if event.key == pygame.K_ESCAPE:
                        self.actions["escape"] = True

                if self.typing:
                    if event.key == pygame.K_BACKSPACE:

                        self.text_buffer = self.text_buffer[:-1]

                    elif event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:

                        # If escape is pressed, exit typing mode and clear the string as well
                        if event.key == pygame.K_ESCAPE:
                            self.text_buffer = ""

                        # Indicate that the text buffer is ready to be saved somewher
                        else:
                            self.text_ready = True

                        # Exit typing mode and resume normal input
                        self.typing = False

                    else:
                        # Add the text to the text buffer string
                        self.text_buffer += event.unicode

                # Randomly select between either of the available channels since this is a spam clicky thing
                # if self.sound:
                #     if (
                #         not self.main_channel.get_queue()
                #         and not self.main_channel.get_busy()
                #     ):
                #         # self.main_channel.stop()

                #         self.main_channel.queue(self.audio_handler.click_sfx)
                # if random.randrange(2):
                #     self.click_channel_1.stop()
                #     self.click_channel_1.play(self.audio_handler.click_sfx)
                # else:
                #     self.click_channel_2.stop()
                #     self.click_channel_2.play(self.audio_handler.click_sfx)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.actions["up"] = False

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.actions["left"] = False

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.actions["down"] = False

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.actions["right"] = False

                if event.key == pygame.K_SPACE:
                    self.actions["space"] = False

                if event.key == pygame.K_BACKSPACE:
                    self.actions["backspace"] = False

                if event.key == pygame.K_RETURN:
                    self.actions["enter"] = False

                if event.key == pygame.K_ESCAPE:
                    self.actions["escape"] = False

    def update(self):
        self.clock.tick(self.fps)
        self.stack[-1].update(self.actions)
        self.sprites.update()

        if self.music:
            pygame.mixer.music.unpause()

        if not self.music:
            pygame.mixer.music.pause()

        pygame.mixer.music.set_volume(self.volume)

    def render(self):
        self.stack[-1].render(self.canvas)
        self.sprites.draw(self.canvas)

        self.screen.blit(
            pygame.transform.scale(
                self.canvas, (self.screen_width, self.screen_height)
            ),
            (0, 0),
        )

        pygame.display.update()

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def start(self):
        # Initialise the first item in the stack, which is the Main Menu
        self.start = MainMenu(self)
        self.stack.append(self.start)


# Make sure the function below only runs if this is the main file
if __name__ == "__main__":
    # Initialise the game class
    game = Game()

    # Set game.running to False to stop the game
    while game.running:

        # game_loop loops through the state checking methods as long as game.playing is True
        game.game_loop()
