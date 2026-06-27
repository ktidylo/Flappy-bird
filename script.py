from pygame import *
from random import randint

init()
size = 1200, 800
window = display.set_mode(size)
clock = time.Clock()

player_rect = Rect(150, size[1]//2-100, 100, 100)

def genererate_pipes(count, pipe_width=140, gap=280, min_height=50, max_height=440, distance=650):
    pipes = []
    start_x = size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap, pipe_width, size[1] - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes


pipes = genererate_pipes(150)
score = 0
main_font = font.Font(None, 36)
lose = False
y_vel = 2
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    window.fill("sky blue")
    draw.rect(window, "yellow", player_rect)
    for pipe in pipes:
        pipe.x -= 10
        draw.rect(window, 'green', pipe)
        if pipe.x <= -100:
            pipes.remove(pipe)
            score += 0.5
        if player_rect.colliderect(pipe):
            lose = True
    if len(pipes) < 8:
        pipes += genererate_pipes(150)

    score_text = main_font.render(f"{int(score)}", 1, "black")
    center_text = size[0]//2 - score_text.get_rect().w
    window.blit(score_text, (center_text, 40))

    clock.tick(60)
    display.update()

    keys=key.get_pressed()
    if keys[K_w] and not lose: player_rect.y -=15
    if keys[K_s] and not lose: player_rect.y += 15
    if lose:
        player_rect.y += y_vel
        y_vel *= 1.1
