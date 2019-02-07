class Denizen:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite

    def draw_to(self, dest):
        dest.blit(self.sprite, (self.x, self.y))

    def calculate_position(self, x_direction, terminal):
        self.accelerate_x(x_direction)
        self.accelerate_y(terminal)
        self.x += self.vel_x
        self.y += self.vel_y

    def accelerate_x(self, direction):
        top_speed = self.run_speed * direction
        accel_factor = 0.1
        self.vel_x = accel_factor * top_speed + (1 - accel_factor) * self.vel_x
        if abs(self.vel_x) < 0.1:
            self.vel_x = 0

    def accelerate_y(self, top_speed):
        accel_factor = 0.07
        self.vel_y = accel_factor * top_speed + (1 - accel_factor) * self.vel_y
        if abs(self.vel_y) < 0.1:
            self.vel_y = 0


class Player(Denizen):
    def __init__(self, x, y, vel_x, vel_y, run_speed, terminal,
                 accel_x, accel_y, jumping, sprite, rect):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.run_speed = run_speed
        self.terminal = terminal
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.jumping = jumping
        self.sprite = sprite
        self.rect = rect

    def jump(self, ground):
        if self.y + self.rect.height == ground:
            self.vel_y = -25
            self.jumping = True

    def is_falling(self, ground):
        if self.y + self.rect.height >= ground:
            self.y = ground - self.rect.height
            self.vel_y = 0
            self.jumping = False
            terminal = 0
        else:
            terminal = self.terminal
        return terminal
