import os
from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color


current_path = os.path.realpath('.')
original_file = 'test02.jpg'
original_path = current_path + '\\' + original_file
modulated_path = current_path + '\\' + 'modulated_' + original_file

with Drawing() as draw:
    draw.stroke_color = Color('red')
    draw.stroke_width = 2
    draw.fill_color = Color('white')
    draw.line((125, 55), (125, 50))
    draw.line((125, 50), (85, 50))
    draw.stroke_width = 4
    draw.line((85, 50), (105, 70))
    draw.stroke_width = 2
    draw.line((105, 70), (85, 90))
    draw.stroke_width = 4
    draw.line((85, 90), (125, 90))
    draw.stroke_width = 2
    draw.line((125, 90), (125, 85))
    with Image(filename=original_path) as img:
        draw.draw(img)
        img.save(filename=modulated_path)


print('end of line')
