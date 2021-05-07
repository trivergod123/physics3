let first = sprites.createProjectileFromSide(assets.image`First`, 20, 0)
let second = sprites.createProjectileFromSide(assets.image`Second`, 20, 0)
first.y = 35
second.y = 60
first.ax = 2
game.onUpdate(function () {
    first.say("vx: " + ("" + Math.ceil(first.vx)))
    second.say("vx: " + ("" + second.vx))
})
game.onUpdateInterval(1000, function () {
    second.vx += 2
})
