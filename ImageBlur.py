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

image = PIL.Image.open(r'C:\Users\maloneypatrick08\Pictures\fjords.jpg')
x_size = int(image.size[0] / 2)
y_size = int(image.size[1] / 2)


blurred_img = PIL.Image.new('RGB',(x_size, y_size))
new_x = 0
new_y = 0
print(image[0,0])
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
                #red, green, blue = image[x,y]
                #blurred_img[new_x,new_y] = red, green, blue
                new_x += 2
                new_y += 2
                
blurred_img.show()
        