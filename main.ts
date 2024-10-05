controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`fire works`, Mr_saver, 100, 0)
    info.changeScoreBy(-1)
    if (info.score() < 0) {
        projectile.setImage(assets.image`Nothing`)
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Mr_saver,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . . . 5 f 5 f 5 . . . . . . 
        . . . . . 5 5 5 5 5 . . . . . . 
        . . . . . 5 f 5 f 5 . . . . . . 
        . . . . . . f f f . . . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . f f f f f f f . . . . . . 
        . . . . 5 f f f f f 5 . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . . . 5 . . . 5 . . . . . . 
        . . . . 5 . . . . . 5 . . . . . 
        `],
    500,
    true
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Mr_saver,
    [img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . . . 5 f 5 f 5 . . . . . . 
        . . . . . 5 5 5 5 5 . . . . . . 
        . . . . . 5 f 5 f 5 . . . . . . 
        . . . . . . f f f . . . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . . . f f f f f f f . . . . 
        . . . . 5 f f f f . 5 . . . . . 
        . . . . . . . 5 . . . . . . . . 
        . . . . . . 5 5 5 . . . . . . . 
        . . . . . 5 . . . 5 . . . . . . 
        . . . . 5 . . . . . 5 . . . . . 
        `],
    500,
    true
    )
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.gameOver(false)
})
let projectile: Sprite = null
let Mr_saver: Sprite = null
info.setScore(10)
tiles.setCurrentTilemap(tilemap`level5`)
game.setGameOverScoringType(game.ScoringType.None)
Mr_saver = sprites.create(assets.image`Mr saver`, SpriteKind.Player)
controller.moveSprite(Mr_saver)
Mr_saver.setStayInScreen(true)
let Zombie = sprites.create(assets.image`Zombie`, SpriteKind.Enemy)
Mr_saver.setPosition(randint(-100, 100), randint(-100, 100))
Zombie.follow(Mr_saver, 50)
