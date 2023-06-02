def color_invert(rgb):
    return (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])


print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))
