def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        fire works
    """), Mr_saver, 100, 0)
    info.change_score_by(-1)
    if info.score() < 0:
        projectile.set_image(assets.image("""
            Nothing
        """))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_left_pressed():
    animation.run_image_animation(Mr_saver,
        [img("""
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
        """)],
        500,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(Mr_saver,
        [img("""
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
        """)],
        500,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    game.game_over(True)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
Mr_saver: Sprite = None
info.set_score(10)
tiles.set_current_tilemap(tilemap("""
    level5
"""))
game.set_game_over_scoring_type(game.ScoringType.NONE)
Mr_saver = sprites.create(assets.image("""
    Mr saver
"""), SpriteKind.player)
controller.move_sprite(Mr_saver)
Mr_saver.set_stay_in_screen(True)
Zombie = sprites.create(assets.image("""
    Zombie
"""), SpriteKind.enemy)
Mr_saver.set_position(randint(-100, 100), randint(-100, 100))
Zombie.follow(Mr_saver, 50)