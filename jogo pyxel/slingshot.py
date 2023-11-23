import pyxel
import math
from bubble import Bubble, Position


class Slingshot:
    def __init__(self):
        self.is_pulled = False
        self.initial_click_pos = Position(0, 0)
        self.current_mouse_pos = Position(0, 0)

    def start_pull(self, x, y):
        self.is_pulled = True
        self.initial_click_pos = Position(x, y)
        self.current_mouse_pos = Position(x, y)

    def update_pull(self, x, y):
        if self.is_pulled:
            self.current_mouse_pos = Position(x, y)

    def end_pull(self):
        self.is_pulled = False

        # Calculate the velocity based on the distance between initial and current mouse positions
        dx = self.initial_click_pos.x - self.current_mouse_pos.x
        dy = self.initial_click_pos.y - self.current_mouse_pos.y
        velocity = Position(
            dx / 100,
            dy / 100,
        )
        return velocity

    def trajectory(self):
        # Draw a line indicating the trajectory
        pyxel.line(
            self.initial_click_pos.x,
            self.initial_click_pos.y,
            self.current_mouse_pos.x,
            self.current_mouse_pos.y,
            7
        )
