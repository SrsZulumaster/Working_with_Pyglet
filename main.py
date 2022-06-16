import pyglet
from pyglet import *
from pyglet.gl import glClearColor


class MyWindow(pyglet.window.Window):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_size(width, height)
        # set background color
        background_colour = [255, 255, 255, 0]
        glClearColor(*background_colour)

    # on_draw updates the window every "tick", is necessary to display everything on the window
    def on_draw(self):
        window.clear()

    def on_key_press(self, symbol, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def update(self, *args):
        pass

    def on_resize(self, width, height):
        pass
        # self.set_size(width, height)


framerate = 30
# define window size
window = MyWindow(700, 700)
pyglet.clock.schedule_interval(window.update, 1 / framerate)
pyglet.app.run()    # This line starts the Window
