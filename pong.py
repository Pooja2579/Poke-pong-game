import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
WHITE = (255, 255, 255)
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Poke Pong Game")


player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
player_score = 0
opponent_score = 0


ball_speed = [4, 4]


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += 5

    
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += 3
    elif opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= 3

    
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

   
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

 
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed[0] = -ball_speed[0]

   
    if ball.left <= 0:
        opponent_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
    elif ball.right >= WIDTH:
        player_score += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2

    
    screen.fill((0, 0, 0))
    
    
    font_title = pygame.font.Font(None, 36)
    title_text = font_title.render("Poke Pong Game", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 10))
    
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    
    font_score = pygame.font.Font(None, 36)
    player_text = font_score.render(str(player_score), True, WHITE)
    opponent_text = font_score.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (3 * WIDTH // 4 - player_text.get_width(), 20))

    
    pygame.display.flip()

    
    clock.tick(FPS)
