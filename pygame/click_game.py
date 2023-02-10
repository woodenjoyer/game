rock = Actor("rock")
rock.topright = 0, 10

WIDTH = 500
HEIGHT = rock.height + 200


def draw():
    screen.clear()
    rock.draw()


def update():
    rock.left += 2
    if rock.left > WIDTH:
        rock.right = 0


def on_mouse_down(pos):
    if rock.collidepoint(pos):
        sounds.eep.play()
        rock.image = "rock_hurt"


def on_mouse_down(pos):
    if rock.collidepoint(pos):
        print("Eek!")
    else:
        print("You Missed Me!")


def on_mouse_down(pos):
    if rock.collidepoint(pos):
        set_rock_hurt()


def set_rock_hurt():
    rock.image = "rock_hurt"
    sounds.eep.play()


def set_rock_normal():
    rock.image = "rock"

def set_rock_hurt():
    rock.image = "rock_hurt"
    sounds.eep.play()
    clock.schedule_unique(set_rock_normal, 1.0)
