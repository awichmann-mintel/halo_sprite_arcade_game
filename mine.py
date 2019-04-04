import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player = arcade.AnimatedWalkingSprite()
        character_scale = 0.75
        self.player.stand_right_textures.append(arcade.load_texture("spartan/spartan_running.jpg", scale=character_scale))
        

    def on_draw(self):
        self.player.draw()

game = MyGame()
arcade.run()