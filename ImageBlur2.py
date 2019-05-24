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

image = PIL.Image.open(r'C:\Users\maloneypatrick08\Pictures\pexels-photo-414612.png')
x_size = image.size[0]
y_size = image.size[1]
blurred_img = PIL.Image.new('RGB',(x_size, y_size))
print(image.size)
print(blurred_img.size)

list = []
for x in range(image.size[0]):
    for y in range(image.size[1]):
        
        look_up = True
        look_down = True
        look_right = True
        look_left = True
        
        if x == 0:
            look_left = False                     
        if x == x_size:
            look_right = False
        if y == 0:
                look_up = False
        if y == y_size:
            look_down = False
        
        if look_up:
            up_r, up_g, up_b = image.getpixel((x,y-1))
        if look_down:
            down_r, down_g, down_b = image.getpixel(x,y+1)
        if look_right:
            right_r, right_g, right_b = image.getpixel(x-1,y)
        if look_left:
            left_r, left_g, left_b = image.getpixel(x+1,y)
            
        c_r, c_g, c_b = image.getpixel((x,y))
                
                
blurred_img.show()
blurred_img.save(str(time.time()) + '.jpg')
        