class Denizen:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def draw_to(self, dest):
        dest.blit(self.sprite, (self.x, self.y))


class Player(Denizen):
    def __init__(self, x, y, vel_x, vel_y,
                 accel_x, accel_y, sprite, rect):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.sprite = sprite
        self.rect = rect

    def calculate_position(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def accelerate_x(self, direction, top_speed):
        top_speed *= direction
        accel_factor = 0.4
        self.vel_x = accel_factor * top_speed + (1 - accel_factor) * self.vel_x
        if abs(self.vel_x) < 0.1:
            self.vel_x = 0

    def accelerate_y(self, top_speed):
        accel_factor = 0.1
        self.vel_y = accel_factor * top_speed + (1 - accel_factor) * self.vel_y
        if abs(self.vel_y) < 0.1:
            self.vel_y = 0

    def jump(self):
        self.vel_y = -30
