import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("RGB +1")

# 초기 RGB 값
r, g, b = 0, 0, 0

last_change_time = 0
clock = pygame.time.Clock()
running = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✅ 1초마다 RGB 값 +1
    if current_time - last_change_time >= 200:
        r = min(r + 1, 255)
        g = min(g + 1, 255)
        b = min(b + 1, 255)
        last_change_time = current_time

        # print(f"RGB = ({r}, {g}, {b})")  # 디버깅용

    screen.fill((r, g, b))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
