import arcade


class LANGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)

        self.placeholder = arcade.Sprite("texture/placeholder.jpg", 0.60)

        self.x = 400
        self.y = 300
        self.sx = 200
        self.sy = 200
    def on_draw(self):
        arcade.start_render()

        self.placeholder.draw()
    def on_update(self, delta_time: float):
        if self.x < 0+75 or self.x > 800-75:
            self.sx *= -1
        if self.y < 0+75 or self.y > 600-75:
            self.sy *= -1
        self.x += self.sx * delta_time
        self.y += self.sy * delta_time
        self.placeholder.set_position(self.x, self.y)


LANGameWindow(800, 600, 'LAn')

arcade.run()
