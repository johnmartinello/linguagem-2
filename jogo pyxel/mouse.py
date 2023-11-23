import pyxel
import math
from bubble import Bubble, Position

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

MAX_BUBBLE_SPEED = 1.5
NUM_INITIAL_BUBBLES = 10
NUM_EXPLODE_BUBBLES = 15


class Mouse:
    def __init__(self):
        self.radius = 25
        self.color = pyxel.rndi(1, 15)

    def draw(self):
        pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, self.radius, self.color)

    def middle_click(self):
        self.color = pyxel.rndi(1, 15)

    def x2_click(self, bubbles):
        num_bubbles = len(bubbles)
        for i in range(num_bubbles):
            bubble = bubbles[i]
            dx = bubble.pos.x - pyxel.mouse_x
            dy = bubble.pos.y - pyxel.mouse_y

            if dx * dx + dy * dy < bubble.radius * bubble.radius:
                bubbles[i].is_exploded = True
                new_radius = pyxel.sqrt(
                    bubble.radius * bubble.radius / NUM_EXPLODE_BUBBLES)

                for j in range(NUM_EXPLODE_BUBBLES):
                    angle = 360 * j / NUM_EXPLODE_BUBBLES

                    new_bubble = Bubble()
                    new_bubble.radius = new_radius
                    new_bubble.pos.x = bubble.pos.x + (
                        bubble.radius + new_radius
                    ) * pyxel.cos(angle)
                    new_bubble.pos.y = bubble.pos.y + (
                        bubble.radius + new_radius
                    ) * pyxel.sin(angle)
                    new_bubble.vel.x = pyxel.cos(angle) * MAX_BUBBLE_SPEED
                    new_bubble.vel.y = pyxel.sin(angle) * MAX_BUBBLE_SPEED
                    bubbles.append(new_bubble)

                del bubbles[i]
                break

    def x1_click(self, bubbles):
        num_bubbles = len(bubbles)

        for i in range(num_bubbles):
            bubble = bubbles[i]
            dx = bubble.pos.x - pyxel.mouse_x
            dy = bubble.pos.y - pyxel.mouse_y

            distance = math.sqrt(dx**2 + dy**2)

            if distance <= bubble.radius:
                bubbles.remove(bubbles[i])
                break
