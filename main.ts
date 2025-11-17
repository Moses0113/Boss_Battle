//  by Mo Chit Moses in 2022
//  Last update on the 22nd of November 2024
//  v.0.0.2
//  Boss Battle
let WaitTimePlayer = 400
let WaitTimeE = 400
namespace SpriteKind {
    export const PlayerShot = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Enemy, SpriteKind.PlayerShot, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    pause(1000)
    info.changeScoreBy(50)
    pause(1000)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    shootBulletFromSprite(mySprite, 100, 0)
})
info.onScore(1000, function on_on_score() {
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    info.changeLifeBy(-1)
    pause(1000)
})
info.onLifeZero(function on_life_zero() {
    game.gameOver(false)
})
//  Call this function to shoot a bullet from sourceSprite.
//  Sprite kind and image are set according to the whether the source is player or enemy.
//  The angle is in degrees (0 to 360, counted clockwise). 0 is upwards, 90 is leftwards.
function shootBulletFromSprite(sourceSprite: Sprite, speed: number, angle: number) {
    
    projectile = sprites.createProjectileFromSprite(img`
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
        `, sourceSprite, speed * Math.sin(angle / 57.3), speed * -1 * Math.cos(angle / 57.3))
    if (sourceSprite.kind() == SpriteKind.Player) {
        projectile.setKind(SpriteKind.PlayerShot)
        projectile.setImage(img`
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
        `)
        pause(WaitTimePlayer)
    } else {
        projectile.setKind(SpriteKind.Projectile)
        projectile.setImage(img`
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
        `)
        pause(WaitTimeE)
    }
    
}

let projectile : Sprite = null
let mySprite : Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setPosition(80, 105)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
controller.moveSprite(mySprite)
let boss = sprites.create(img`
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
    `, SpriteKind.Enemy)
boss.setPosition(80, 29)
info.setLife(5)
info.setScore(0)
let MAX = 12
game.onUpdateInterval(2000, function on_update_interval() {
    boss.setPosition(randint(0, 150), 29)
})
forever(function on_forever() {
    for (let index = 0; index < 10; index++) {
        shootBulletFromSprite(boss, randint(-100, 100), randint(-100, 100))
    }
    pause(1000)
})
