import pyxel
from position import Position
from mouse import Mouse
from bubble import Bubble
from slingshot import Slingshot

import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

MAX_BUBBLE_SPEED = 2.5
NUM_INITIAL_BUBBLES = 10
NUM_EXPLODE_BUBBLES = 15


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT,
                   title="Pyxel Bubbles", fps=240, display_scale=1, capture_scale=1)
        pyxel.mouse(False)

        self.is_exploded = False
        self.collision = False
        self.bubbles = [Bubble() for i in range(NUM_INITIAL_BUBBLES)]
        self.mouse = Mouse()
        self.slingshot = Slingshot()
        self.gravity = False
        self.time = True
        self.boundaries = True

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        try:
            if self.gravity:
                for bubble in self.bubbles:
                    bubble.gravitational_field(self.bubbles)
        except IndexError:
            velocity = Position(1, 1)

            new_bubble = Bubble()
            new_bubble.pos.x = pyxel.mouse_x
            new_bubble.pos.y = pyxel.mouse_y
            new_bubble.vel = velocity
            new_bubble.color = self.mouse.color
            self.bubbles.append(new_bubble)

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if not self.slingshot.is_pulled:
                self.slingshot.start_pull(pyxel.mouse_x, pyxel.mouse_y)

            else:
                self.slingshot.update_pull(pyxel.mouse_x, pyxel.mouse_y)
                self.slingshot.trajectory()

        elif self.slingshot.is_pulled:
            velocity = self.slingshot.end_pull()

            new_bubble = Bubble()
            new_bubble.pos.x = pyxel.mouse_x
            new_bubble.pos.y = pyxel.mouse_y
            new_bubble.vel = velocity
            new_bubble.color = self.mouse.color
            self.bubbles.append(new_bubble)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_MIDDLE):
            self.mouse.middle_click()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_X2):
            self.mouse.x2_click(self.bubbles)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_X1):
            self.mouse.x1_click(self.bubbles)

        if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
            if not self.is_dragging:
                # Check if the mouse is over any bubble
                for bubble in self.bubbles:
                    dx = pyxel.mouse_x - bubble.pos.x
                    dy = pyxel.mouse_y - bubble.pos.y
                    distance = math.sqrt(dx**2 + dy**2)

                    if distance < bubble.radius:
                        self.selected_bubble = bubble
                        self.drag_start_pos = Position(
                            pyxel.mouse_x, pyxel.mouse_y)
                        self.is_dragging = True
                        break

            elif self.selected_bubble:
                # Calculate the distance between the current mouse position and the start position
                dx = pyxel.mouse_x - self.drag_start_pos.x
                dy = pyxel.mouse_y - self.drag_start_pos.y
                distance = math.sqrt(dx**2 + dy**2)

                # Adjust the size of the selected bubble based on the mouse drag distance
                self.selected_bubble.radius = max(
                    5, self.selected_bubble.radius + distance * 0.01)

                # Update the start position for the next frame
                self.drag_start_pos = Position(pyxel.mouse_x, pyxel.mouse_y)

        else:
            self.is_dragging = False
            self.selected_bubble = None

        if pyxel.btnp(pyxel.KEY_F):
            if self.boundaries:
                self.boundaries = False
            else:
                self.boundaries = True

        if pyxel.btnp(pyxel.KEY_G):
            if self.time:
                self.time = False
            else:
                self.time = True

        if pyxel.btnp(pyxel.KEY_H):
            if self.gravity:
                self.gravity = False
            else:
                self.gravity = True

        if pyxel.btnp(pyxel.KEY_J):
            if self.collision:
                self.collision = False
            else:
                self.collision = True

        if pyxel.btnp(pyxel.KEY_K):

            num_bubbles = len(self.bubbles)

            for i in range(num_bubbles):
                bubble = self.bubbles[i]
                dx = bubble.pos.x - pyxel.mouse_x
                dy = bubble.pos.y - pyxel.mouse_y

                distance = math.sqrt(dx**2 + dy**2)

                if distance <= bubble.radius:
                    if bubble.fixed:
                        bubble.fixed = False
                    else:
                        bubble.fixed = True

        num_bubbles = len(self.bubbles)

        for i in range(num_bubbles - 1, -1, -1):
            bi = self.bubbles[i]

            if bi.fixed:
                continue

            if self.time:
                bi.update(self.boundaries)

            if not self.collision:
                for j in range(i - 1, -1, -1):
                    bj = self.bubbles[j]
                    dx = bi.pos.x - bj.pos.x
                    dy = bi.pos.y - bj.pos.y
                    total_radius = bi.radius + bj.radius

                    if dx * dx + dy * dy < total_radius * total_radius:
                        new_bubble = Bubble()
                        new_bubble.radius = pyxel.sqrt(
                            bi.radius * bi.radius + bj.radius * bj.radius)
                        new_bubble.pos.x = (
                            bi.pos.x * bi.radius + bj.pos.x * bj.radius) / total_radius
                        new_bubble.pos.y = (
                            bi.pos.y * bi.radius + bj.pos.y * bj.radius) / total_radius
                        new_bubble.vel.x = (
                            bi.vel.x * bi.radius + bj.vel.x * bj.radius) / total_radius
                        new_bubble.vel.y = (
                            bi.vel.y * bi.radius + bj.vel.y * bj.radius) / total_radius
                        if bj.fixed:
                            new_bubble.fixed = True
                        self.bubbles.append(new_bubble)

                        del self.bubbles[i]
                        del self.bubbles[j]
                        num_bubbles -= 1
                        break
            else:
                for j in range(i - 1, -1, -1):
                    bj = self.bubbles[j]

                    bi.collision(bj)

    def draw(self):
        pyxel.cls(0)

        pyxel.text(6, SCREEN_HEIGHT-100, "Mouse left - Create new ball", 7)
        pyxel.text(6, SCREEN_HEIGHT-90, "Mouse middle - Change ball color", 7)
        pyxel.text(6, SCREEN_HEIGHT-80, "Mouse 1 - Delete ball", 7)
        pyxel.text(6, SCREEN_HEIGHT-70, "Mouse 2 - Explode ball", 7)
        pyxel.text(6, SCREEN_HEIGHT-40, "F - Wall boundaries ON/OFF", 7)
        pyxel.text(6, SCREEN_HEIGHT-40, "G - Time ON/OFF", 7)
        pyxel.text(6, SCREEN_HEIGHT-30, "H - Gravity ON/OFF", 7)
        pyxel.text(6, SCREEN_HEIGHT-20, "J - Collision ON/OFF", 7)
        pyxel.text(6, SCREEN_HEIGHT-10, "K - Fixate ball", 7)

        self.mouse.draw()

        for bubble in self.bubbles:
            pyxel.circ(bubble.pos.x, bubble.pos.y, bubble.radius, bubble.color)

        if self.slingshot.is_pulled:
            self.slingshot.trajectory()

        if self.collision:
            pyxel.text(SCREEN_WIDTH - 100, 6, "Collision: ON", 11)
        else:
            pyxel.text(SCREEN_WIDTH - 100, 6, "Collision: OFF", 8)

        if self.gravity:
            pyxel.text(SCREEN_WIDTH - 100, 18, "Gravity: ON", 11)
        else:
            pyxel.text(SCREEN_WIDTH - 100, 18, "Gravity: OFF", 8)

        if self.boundaries:
            pyxel.text(SCREEN_WIDTH - 100, 30, "Wall boundaries: ON", 11)
        else:
            pyxel.text(SCREEN_WIDTH - 100, 30, "Wall boundaries: OFF", 8)

        if self.time:
            pyxel.text(SCREEN_WIDTH - 100, 42, "Time: ON", 11)
        else:
            pyxel.text(SCREEN_WIDTH - 100, 42, "Time: OFF", 8)


App()
