import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)


def extractcolor():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        newcol = (r, g, b)
        rgb_colors.append(newcol)


extractcolor()
