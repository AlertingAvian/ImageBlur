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

import PIL
import PIL.ImageDraw
import matplotlib.pyplot as plt

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

x = None
y = None
image = PIL.Image.open(r'C:\Users\maloneypatrick08\Pictures\pexels-photo-414612.png')

def onclick(event):
    global x,y
    size = 96
    try:
        x,y = (int(round(event.xdata)), int(round(event.ydata)))
        print(x,y)
        color = image.getpixel((x,y))
        new = PIL.Image.new('RGB',(size,size))
        new.paste(color,(0,0,size,size))
        r,g,b = color
        string = str(r) + ', ' + str(g) + ', ' + str(b)
        drw = PIL.ImageDraw.Draw(new)
        if (r+b+g)/3 > 120:
            drw.text((5,5),string,fill=(0,0,0))
        else:
            drw.text((5,5),string,fill=(255,255,255))
        new.show()
    except TypeError:
        print('Outside Plot')
    
        

fig,ax = plt.subplots()
ax.imshow(image, interpolation=None)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()