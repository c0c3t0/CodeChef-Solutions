def color_invert(rgb):
    return (abs(rgb[0]-255), abs(rgb[1]-255), abs(rgb[2]-255))


print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))
