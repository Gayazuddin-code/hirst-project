import colorgram

colors = colorgram.extract("hirst.jpg", 35)
color_list = list()


def avaliable_colors():
    for i in range(len(colors)):
        color = colors[i]
        rgb = color.rgb
        r = rgb.r
        g = rgb.g
        b = rgb.b
        color_list.append((r, g, b))
    return color_list
