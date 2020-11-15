# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
This is an attempt to create 2D graphics with SDL.
"""

import sys
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")

sdl2.ext.init()

window = sdl2.ext.Window("Turtle Power!", size=(900, 900))
window.show()


factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("turtle.jpg"))

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)

processor = sdl2.ext.TestEventProcessor()
processor.run(window)

sdl2.ext.quit()
