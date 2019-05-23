"""
Copyright (C) 2019 Patrick Maloney

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import PIL.Image
import time

image = PIL.Image.open(r'C:\Users\maloneypatrick08\Pictures\the-most-famous-windows-wallpaper-ever-turns-20-505668-2.jpg')
x_size = int(image.size[0]/2)
y_size = int(image.size[1]/2)


blurred_img = PIL.Image.new('RGB',(x_size, y_size))
print(image.size)
print(blurred_img.size)
list = []
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            r,g,b = image.getpixel((x,y))
            list.append((r,g,b))
        
step = 0
for x in range(blurred_img.size[0]):
    for y in range(blurred_img.size[1]):
                blurred_img.putpixel((x,y), list[step])
                step += 1
                
                
blurred_img.show()
blurred_img.save(str(time.time()) + '.jpg')
        