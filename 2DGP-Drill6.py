from pico2d import *
from random import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            running = False

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')
hand = load_image('hand_arrow.png')

running = True
x = 800/2
y = 600/2
hx = randint(1, 800)
hy = randint(1, 600)
dx = (hx - x) / 25
dy = (hy - y) / 25
frame = 0

threshold = 5

while running:
    ground.clip_draw(0, 0, 1280, 1024, 800/2, 600/2, 800, 600)
    if dx > 0:
        character.clip_draw(frame * 100, 0, 100, 100, x, y, 100, 100)
    else :
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y, 100, 100)
    hand.clip_draw(0, 0, 50, 52, hx, hy, 50, 52)
    update_canvas()
    frame = (frame + 1) % 8
    if abs(x - hx) < threshold and abs(y - hy) < threshold:
        hx = randint(1, 800)
        hy = randint(1, 600)
        dx = (hx - x) / 25
        dy = (hy - y) / 25
    x += dx
    y += dy
    handle_events()
    delay(0.05)

close_canvas()