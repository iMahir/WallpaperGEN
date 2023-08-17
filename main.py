from PIL import Image, ImageDraw, ImageColor

# image dimensions
width = 1440
height = 2560

# color of the image - #HEX or color name
color = "teal"


def generate_gradient_image(input_color):
    base_color = ImageColor.getcolor(input_color, "RGB")

    # black background
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)

    # gradient colors
    dark_color = (0, 0, 0)

    # generate the gradient
    for y in range(height):

        # lighten the color - from top to bottom
        progress = y / height
        r = dark_color[0] + (base_color[0] - dark_color[0]) * progress
        g = dark_color[1] + (base_color[1] - dark_color[1]) * progress
        b = dark_color[2] + (base_color[2] - dark_color[2]) * progress

        rgb_color = (int(r), int(g), int(b))

        # draw color line
        draw.line((0, y, width, y), fill=rgb_color)

    # generate image
    image.save(f"{color}_wallpaper.png")


generate_gradient_image(color)
