import pyxel
import math
from position import Position

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

MAX_BUBBLE_SPEED = 2.5
NUM_INITIAL_BUBBLES = 10
NUM_EXPLODE_BUBBLES = 15


class Bubble(Position):
    def __init__(self):
        self.radius = 25
        self.fixed = False
        self.gravity = False

        super().__init__(
            pyxel.rndf(10, SCREEN_WIDTH - 10),
            pyxel.rndf(10, SCREEN_HEIGHT - 10),
        )
        self.pos = Position(self.x, self.y)

        self.vel = Position(
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
        )

        self.color = pyxel.rndi(1, 15)

    def collision(self, other):
        # Calculate the vector from self to other
        dx = other.pos.x - self.pos.x
        dy = other.pos.y - self.pos.y

        # Calculate the distance between the centers of the circles
        distance = pyxel.sqrt(dx**2 + dy**2)

        # Calculate the sum of the radii
        min_distance = self.radius + other.radius

        # Check if the circles are colliding
        if distance < min_distance:

            # Calculate the unit normal vector (direction from self to other)
            nx = dx / distance
            ny = dy / distance

            # Calculate the unit tangent vector (perpendicular to the normal)
            tx = -ny
            ty = nx

            # Calculate the relative velocity components along the normal and tangent vectors
            relative_velocity_x = other.vel.x - self.vel.x
            relative_velocity_y = other.vel.y - self.vel.y

            # Calculate the dot product of relative velocity and normal vector
            dot_product = (
                relative_velocity_x * nx + relative_velocity_y * ny
            )

            # Calculate the impulse magnitude using the impulse-momentum theorem
            impulse_magnitude = (2.0 * dot_product) / (
                1 / self.radius + 1 / other.radius
            )

            # Apply impulses to update velocities

            self.vel.x += (impulse_magnitude * nx / self.radius) * 0.85
            self.vel.y += (impulse_magnitude * ny / self.radius) * 0.85

            other.vel.x -= (impulse_magnitude * nx / other.radius) * 0.85
            other.vel.y -= (impulse_magnitude * ny / other.radius) * 0.85

            # Move the circles away to avoid overlap
            overlap = (min_distance - distance) / 2.0
            if not self.fixed or not other.fixed:
                self.pos.x -= overlap * nx
                self.pos.y -= overlap * ny

    def gravitational_field(self, other_bubbles):
        G = 0.5

        for other in other_bubbles:
            if other != self:
                dx = other.pos.x - self.pos.x
                dy = other.pos.y - self.pos.y

                try:
                    distance = max(pyxel.sqrt(dx**2 + dy**2), 1.0)

                    if distance > 0.0001:
                        gravitational_force = G * \
                            (self.radius * other.radius) / (distance**2)

                        gravitational_acceleration_x = gravitational_force * dx / distance
                        gravitational_acceleration_y = gravitational_force * dy / distance

                        self.vel.x += gravitational_acceleration_x
                        self.vel.y += gravitational_acceleration_y

                except ZeroDivisionError:
                    continue

    def update(self, boundaries):
        if not (self.fixed and other.fixed):
            self.pos.x += self.vel.x
            self.pos.y += self.vel.y

            if boundaries:
                if self.vel.x < 0 and self.pos.x < self.radius:
                    self.vel.x *= -1

                if self.vel.x > 0 and self.pos.x > SCREEN_WIDTH - self.radius:
                    self.vel.x *= -1

                if self.vel.y < 0 and self.pos.y < self.radius:
                    self.vel.y *= -1

                if self.vel.y > 0 and self.pos.y > SCREEN_HEIGHT - self.radius:
                    self.vel.y *= -1
