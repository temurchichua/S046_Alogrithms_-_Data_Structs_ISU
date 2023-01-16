def change_color(image: list, x: int, y: int, new_color) -> None:
    """
    Inplace repaint color at x, y coordinates

    :param image: initial image
    :param x: x coordinate
    :param y: y coordinate
    :param new_color: color to change to
    """
    # find current color at index x, y
    old_color = image[x][y]

    # create queue of pixels to process
    Q = [(x, y)]

    # while the queue is not empty
    while Q:
        # get the next pixel from the queue
        x, y = Q.pop(0)
        # change the color of the pixel to the new color
        if image[x][y] == old_color:
            image[x][y] = newColor
            # add the north, east, south, west pixels to the queue if they are within the image bounds
            if x > 0:
                Q.append((x - 1, y))
            if x < len(image) - 1:
                Q.append((x + 1, y))
            if y > 0:
                Q.append((x, y - 1))
            if y < len(image[0]) - 1:
                Q.append((x, y + 1))


# Input:
image = [[1, 1, 1, 1, 1, 1, 1, 1],  # The values in the given 2D image indicate colors of the pixels
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 0, 0, 1, 1, 0, 1, 1],
         [1, 2, 2, 2, 2, 0, 1, 0],
         [1, 1, 1, 2, 2, 0, 1, 0],
         [1, 1, 1, 2, 2, 2, 2, 0],
         [1, 1, 1, 1, 1, 2, 1, 1],
         [1, 1, 1, 1, 1, 2, 2, 1]]

x, y = 4, 4  # x and y are coordinates of the brush
newColor = 3  # The color that should replace the previous color on image[x][y] and all surrounding pixels with same
# color
