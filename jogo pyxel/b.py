import pyxel

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MAX_BUBBLE_SPEED = 2.5
NUM_INITIAL_BUBBLES = 10
NUM_EXPLODE_BUBBLES = 15


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bubble:
    def __init__(self):
        self.size = pyxel.rndf(10, 50)

        self.pos = Position(
            pyxel.rndf(self.size, SCREEN_WIDTH - self.size),
            pyxel.rndf(self.size, SCREEN_HEIGHT - self.size),
        )

        self.vel = Position(
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
        )

        self.color = pyxel.rndi(1, 15)

    def update(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        if self.vel.x < 0 and self.pos.x < self.size:
            self.vel.x *= -1

        if self.vel.x > 0 and self.pos.x > SCREEN_WIDTH - self.size:
            self.vel.x *= -1

        if self.vel.y < 0 and self.pos.y < self.size:
            self.vel.y *= -1

        if self.vel.y > 0 and self.pos.y > SCREEN_HEIGHT - self.size:
            self.vel.y *= -1


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT,
                   title="Pyxel Bubbles", capture_scale=1)
        pyxel.mouse(True)

        self.is_exploded = False
        self.bubbles = [Bubble() for _ in range(NUM_INITIAL_BUBBLES)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        num_bubbles = len(self.bubbles)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for i in range(num_bubbles):
                bubble = self.bubbles[i]
                dx = bubble.pos.x - pyxel.mouse_x
                dy = bubble.pos.y - pyxel.mouse_y

                if dx * dx + dy * dy < bubble.size * bubble.size:
                    self.is_exploded = True
                    new_size = pyxel.sqrt(
                        bubble.size * bubble.size / NUM_EXPLODE_BUBBLES)

                    for j in range(NUM_EXPLODE_BUBBLES):
                        angle = 360 * j / NUM_EXPLODE_BUBBLES

                        new_bubble = Bubble()
                        new_bubble.size = new_size
                        new_bubble.pos.x = bubble.pos.x + (
                            bubble.size + new_size
                        ) * pyxel.cos(angle)
                        new_bubble.pos.y = bubble.pos.y + (
                            bubble.size + new_size
                        ) * pyxel.sin(angle)
                        new_bubble.vel.x = pyxel.cos(angle) * MAX_BUBBLE_SPEED
                        new_bubble.vel.y = pyxel.sin(angle) * MAX_BUBBLE_SPEED
                        self.bubbles.append(new_bubble)

                    del self.bubbles[i]
                    break

        for i in range(num_bubbles - 1, -1, -1):
            bi = self.bubbles[i]
            bi.update()

            for j in range(i - 1, -1, -1):
                bj = self.bubbles[j]
                dx = bi.pos.x - bj.pos.x
                dy = bi.pos.y - bj.pos.y
                total_size = bi.size + bj.size

                if dx * dx + dy * dy < total_size * total_size:
                    new_bubble = Bubble()
                    new_bubble.size = pyxel.sqrt(
                        bi.size * bi.size + bj.size * bj.size)
                    new_bubble.pos.x = (
                        bi.pos.x * bi.size + bj.pos.x * bj.size) / total_size
                    new_bubble.pos.y = (
                        bi.pos.y * bi.size + bj.pos.y * bj.size) / total_size
                    new_bubble.vel.x = (
                        bi.vel.x * bi.size + bj.vel.x * bj.size) / total_size
                    new_bubble.vel.y = (
                        bi.vel.y * bi.size + bj.vel.y * bj.size) / total_size
                    self.bubbles.append(new_bubble)

                    del self.bubbles[i]
                    del self.bubbles[j]
                    num_bubbles -= 1
                    break

    def draw(self):
        pyxel.cls(0)

        for bubble in self.bubbles:
            pyxel.circ(bubble.pos.x, bubble.pos.y, bubble.size, bubble.color)


App()
