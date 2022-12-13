import ctypes.wintypes
import pygame

# initiate pygame
pygame.init()

# make game window
width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# max speed
FPS = 60

paddle_width = 20
paddle_heigth = 100
ball_radius = 7
score_font = pygame.font.SysFont("arial", 50)
winning_score = 10

class Paddle:
    color = (77, 42, 235)
    vel = 4

    def __init__(self, x, y, width, height):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.vel
        else:
            self.y += self.vel

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y

class Ball:
    color = (77, 42, 235)
    max_vel = 5

    def __init__(self, x, y, radius):
        self.x = self.starting_x = x
        self.y = self.starting_y  = y
        self.radius = radius
        self.x_vel = self.max_vel
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y
        self.y_vel = 0
        self.x_vel *= -1

def draw(win, paddles, ball, left_score, right_score):
    win.fill((179, 178, 218))

    left_score_text = score_font.render(f"{left_score}", 1, (77, 42, 235))
    right_score_text = score_font.render(f"{right_score}", 1, (77, 42, 235))
    win.blit(left_score_text, (width // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (width // 4 * 3 - left_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw(window)

    j = 1
    for i in range(10, height, height // 20):
        j += 1
        if j % 2 == 1:
            continue
        pygame.draw.rect(window, (77, 42, 235), (width // 2 - 5, i, 10, height // 20))
    j = 0

    ball.draw(window)
    pygame.display.update()

def collisions(ball, left_paddle, rigth_paddle):
    # ceiling and floor collisions
    if ball.y + ball_radius >= height:
        ball.y_vel *= -1
    elif ball.y - ball_radius <= 0:
        ball.y_vel *= -1

    # paddle collision
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1
    else:
        if ball.y >= rigth_paddle.y and ball.y <= rigth_paddle.y + rigth_paddle.height:
            if ball.x + ball_radius >= rigth_paddle.x:
                ball.x_vel *= -1

                middle_y = rigth_paddle.y + rigth_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (rigth_paddle.height / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1

def paddle_movement(keys, left_paddle, rigth_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.vel >= 0:
        left_paddle.move()
    if keys[pygame.K_s] and left_paddle.y + left_paddle.vel + left_paddle.height <= height:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and rigth_paddle.y - rigth_paddle.vel >= 0:
        rigth_paddle.move()
    if keys[pygame.K_DOWN] and rigth_paddle.y + rigth_paddle.vel + rigth_paddle.height <= height:
        rigth_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock() # max speed

    left_paddle = Paddle(10, height // 2 - paddle_heigth // 2, paddle_width, paddle_heigth)
    right_paddle = Paddle(width - 10 - paddle_width, height // 2 - paddle_heigth // 2, paddle_width, paddle_heigth)
    ball = Ball(width // 2, height // 2, ball_radius)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(window, [left_paddle, right_paddle], ball, left_score, right_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        collisions(ball, left_paddle, right_paddle)
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > width:
            left_score += 1
            ball.reset()

        won = False
        if left_score == winning_score:
            won = True
            winning_text = "Left Player Won!"
        elif right_score == winning_score:
            won = True
            winning_text = "Right Player Won!"

        if won:
            text = score_font.render(winning_text, 1, (77, 42, 235))
            window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()

if __name__ == "__main__":
    main()
