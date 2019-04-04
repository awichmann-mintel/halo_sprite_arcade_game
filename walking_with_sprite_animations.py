"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
from datetime import datetime, timedelta
import requests
import random
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Move with a Sprite Animation Example"

COIN_SCALE = 0.5
COIN_COUNT = 7

MOVEMENT_SPEED = 5
TOTAL_TIME_SECONDS = 30


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player = None

    def setup(self):
        self.start_time = datetime.now()
        self.time_left = timedelta(seconds=TOTAL_TIME_SECONDS) - (datetime.now() - self.start_time)

        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = .75
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("images/spartan/spartan_rest.png",
                                                                    scale=character_scale))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("images/spartan/spartan_rest.png",
                                                                   scale=character_scale, mirrored=True))

        self.player.walk_right_textures = []

        self.player.walk_right_textures.append(arcade.load_texture("images/spartan/spartan_running_0.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/spartan/spartan_running_1.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/spartan/spartan_running_2.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/spartan/spartan_running_3.png",
                                                                   scale=character_scale))
        self.player.walk_right_textures.append(arcade.load_texture("images/spartan/spartan_running_4.png",
                                                                   scale=character_scale))

        self.player.walk_left_textures = []

        self.player.walk_left_textures.append(arcade.load_texture("images/spartan/spartan_running_0.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/spartan/spartan_running_1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/spartan/spartan_running_2.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/spartan/spartan_running_3.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/spartan/spartan_running_4.png",
                                                                  scale=character_scale, mirrored=True))
        self.player.texture_change_distance = 30

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.all_sprites_list.append(self.player)

        for i in range(COIN_COUNT):
            coin = arcade.AnimatedTimeSprite(scale=0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            coin.textures = []
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_0.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_1.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_2.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_3.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_2.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_1.png", scale=COIN_SCALE))
            coin.textures.append(arcade.load_texture("images/coin/gold_coin_0.png", scale=COIN_SCALE))
            coin.cur_texture_index = random.randrange(len(coin.textures))

            self.coin_list.append(coin)
            self.all_sprites_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(str(self.time_left), 10, 35, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        self.all_sprites_list.update()
        self.all_sprites_list.update_animation()
        if self.time_left <= timedelta(seconds=0):
            self.time_left = timedelta(seconds=0)
        else:
            self.time_left = timedelta(seconds=TOTAL_TIME_SECONDS) - (datetime.now() - self.start_time)

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.kill()
            self.score += 1
        if len(self.coin_list) == 0 or self.time_left <= timedelta(seconds=0):        
            arcade.draw_text("Score "+str(self.score), SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.ALABAMA_CRIMSON, 14)
            print("posting score " + str(self.score))
            response = requests.post("http://localhost:8080/scores/test/", json={"score": self.score})
            if response.status_code == 200:
                print('Great Success!')
            for sprite in self.all_sprites_list:
                sprite.kill()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()