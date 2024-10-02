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
x = 800//2
y = 600//2
dx, dy = 0, 0
hx = randint(1, 800)
hy = randint(1, 600)
frame = 0

while running:
    ground.clip_draw(0, 0, 1280, 1024, 800//2, 600//2, 800, 600)
    character.clip_draw(frame*100, 100, x, y, 100, 100)
    hand.clip_draw(0, 0, 50, 52, hx, hy, 40, 40)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()