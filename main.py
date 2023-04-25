import arcade

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Python Pixel Pursuit"

# Character constants
PLAYER_SCALE = 0.5
PLAYER_START_X = 100
PLAYER_START_Y = 150

class PythonPixelPursuit(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player = None
        self.physics_engine = None

    def setup(self):
        # Set up the player
        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", PLAYER_SCALE)
        self.player.center_x = PLAYER_START_X
        self.player.center_y = PLAYER_START_Y

        # Set up the physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, [], gravity_constant=200)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 12
        elif key == arcade.key.LEFT:
            self.player.change_x = -4
        elif key == arcade.key.RIGHT:
            self.player.change_x = 4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    game = PythonPixelPursuit()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
