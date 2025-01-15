game.splash(game.ask_for_number("Enter Password"))
scene.set_background_image(assets.image("""
    myImage1
"""))
mySprite = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.player)
controller.move_sprite(mySprite)