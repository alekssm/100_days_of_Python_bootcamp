import colorgram

color_list =[]

"""
An image file is needed to be added to the project's folder for this work 
- replace 'image.png' with the name of the file
"""


colors = colorgram.extract('image.png', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    current_color = (r, g, b)
    color_list.append(current_color)
