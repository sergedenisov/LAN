import arcade


lanm = open("landia.txt", "r")
print(lanm.readline())
class LANGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)


        self.placeholder = arcade.Sprite("texture/house.gif",  0.15)
        self.wall1 = arcade.Sprite("texture/house.gif", 0.5)
        self.background = arcade.Sprite("texture/layer0.png", 1)
        self.messagebox = arcade.Sprite("texture/layer1_messages.png", 1)
        self.icon1 = arcade.Sprite("texture/placeholder.jpg", 0.25)
        self.wall2 = arcade.Sprite("texture/placeholder.jpg", 1)

        self.x = 400
        self.y = 300
        self.sx = 10
        self.sy = 20

        self.send = 0
        self.i = 0

        self.window = 0


    def textwrite(self, length, file):

            if self.send == 1:
                arcade.draw_text(file.read(), 220, 580- self.i *20, arcade.color.WHITE, 14, width=200, align="center")
                self.i+=1
                print(file.readline())
                self.send = 0

    def window0(self):
        self.messagebox.set_position(487, 300)
        self.wall1.set_position(487, 300)
        self.wall2.set_position(10000, 10000)
        #self.placeholder.set_position(500, 300)
        #print('window 0')
    def window1(self):
        self.messagebox.set_position(487, 300)

        self.wall2.set_position(487, 300)
        self.wall1.set_position(10000, 10000)
        #self.placeholder.set_position(100, 100)
        #print('window 0')

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.background.set_position(400, 300)
        self.messagebox.draw()

        self.icon1.draw()
        self.icon1.set_position(30, 538)
        arcade.draw_text("Messaging test", 20, 540, arcade.color.WHITE, 14, width=200, align="center")

        self.placeholder.draw()
        self.placeholder.set_position(30, 480)
        arcade.draw_text("Window test", 20, 470, arcade.color.WHITE, 14, width=200, align="center")
        self.wall1.draw()
        self.wall2.draw()



    def on_update(self, delta_time: float):
        if self.window == 0:
            self.window0()
        if self.window == 1:
            self.window1()

        self.textwrite(3,open("landia.txt", "r"))





    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(x,', ', y)
        if 32<x<157 and 508<y<568:
            print('got1')
            self.window = 1
        if 32<x<157 and 448<y<508:
            print('got2')
            self.window = 0
        if 750<x<790 and 20<y<60:
            self.send = 1
            print('send')






LANGameWindow(800, 600, 'LAn')

arcade.run()