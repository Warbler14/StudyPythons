import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("1초마다 색상 변경")

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 255, 255),
]

color_index = 0
last_change_time = 0   # 마지막 색 변경 시점(ms)

clock = pygame.time.Clock()
running = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✅ 1초(1000ms)마다 색상 변경
    if current_time - last_change_time >= 1000:
        color_index = (color_index + 1) % len(colors)
        last_change_time = current_time

    screen.fill(colors[color_index])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
