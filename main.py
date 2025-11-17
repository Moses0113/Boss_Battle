# by Mo Chit Moses in 2022
# Second update on the 22nd of November 2024
# Latest update on the 17th of November 2025 
# v.0.0.2
# Boss Battle

WaitTimePlayer = 400
WaitTimeE = 400

@namespace
class SpriteKind:
    PlayerShot = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    pause(1000)
    info.change_score_by(50)
    pause(1000)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.PlayerShot, on_on_overlap)

def on_a_pressed():
    shootBulletFromSprite(mySprite, 100, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_score():
    game.game_over(True)
info.on_score(1000, on_on_score)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

# Call this function to shoot a bullet from sourceSprite.
# Sprite kind and image are set according to the whether the source is player or enemy.
# The angle is in degrees (0 to 360, counted clockwise). 0 is upwards, 90 is leftwards.
def shootBulletFromSprite(sourceSprite: Sprite, speed: number, angle: number):
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        sourceSprite,
        speed * Math.sin(angle / 57.3),
        speed * -1 * Math.cos(angle / 57.3))
    if sourceSprite.kind() == SpriteKind.player:
        projectile.set_kind(SpriteKind.PlayerShot)
        projectile.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . e e . . . . . . . 
                        . . . . . . e 5 1 e . . . . . . 
                        . . . . . e 5 5 5 5 e . . . . . 
                        . . . . . e 4 5 5 5 e . . . . . 
                        . . . . . . e 4 4 e . . . . . . 
                        . . . . . . . e e . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
        pause(WaitTimePlayer)
    else:
        projectile.set_kind(SpriteKind.projectile)
        projectile.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 8 8 . . . . . . . 
                        . . . . . . 8 9 1 8 . . . . . . 
                        . . . . . 8 9 9 9 9 8 . . . . . 
                        . . . . . 8 6 9 9 9 8 . . . . . 
                        . . . . . . 8 6 6 8 . . . . . . 
                        . . . . . . . 8 8 . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
        pause(WaitTimeE)
projectile: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(80, 105)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.move_sprite(mySprite)
boss = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
boss.set_position(80, 29)
info.set_life(5)                #No. of life
info.set_score(0)
MAX = 12

def on_update_interval():
    boss.set_position(randint(0, 150), 29)
game.on_update_interval(2000, on_update_interval)

def on_forever():
    for index in range(10):
        shootBulletFromSprite(boss, randint(-100, 100), randint(-100, 100))
    pause(1000)
forever(on_forever)
