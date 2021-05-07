first = sprites.create(assets.image("""
First
"""), SpriteKind.player)
second = sprites.create(assets.image("""
Second
"""), SpriteKind.player)
first.x += -80
second.x += -80
first.y += -10
second.y += 10
first.vx = 30

def on_on_update():
    first.say("x: " + str(Math.ceil(first.x)))
    second.say("x: " + str(second.x))
game.on_update(on_on_update)

def on_update_interval():
    second.x += 30
game.on_update_interval(1000, on_update_interval)

