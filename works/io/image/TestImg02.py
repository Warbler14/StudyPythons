
import os
from wand.image import Image


current_path = os.path.realpath('.')
original_file = 'test01.jpg'
original_path = current_path + '\\' + original_file
modulated_path = current_path + '\\' + 'modulated_' + original_file

print(current_path)
print(original_file)
print(original_path)
print(modulated_path)

brightness = 50.0
saturation = 50.0
hue = 100.0

with Image(filename=original_path) as image:
    with image.clone() as clone:
        clone.modulate(brightness, saturation, hue)
        clone.flip()
        # clone.flop()
        clone.rotate(135)
        clone.save(filename=modulated_path)
