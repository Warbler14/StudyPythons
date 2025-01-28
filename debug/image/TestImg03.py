import os
from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color


with Drawing() as draw:
    draw.stroke_color = Color('black')
    draw.stroke_width = 2
    draw.fill_color = Color('white')
    draw.arc((25, 25),  # Stating point
             (75, 75),  # Ending point
             (135, -45))  # From bottom left around to top right
    with Image(width=100,
               height=100,
               background=Color('lightgray')) as img:
        draw.draw(img)
        img.save(filename='draw-arc.gif')


print('end of line')
