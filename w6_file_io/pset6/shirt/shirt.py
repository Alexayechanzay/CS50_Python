import sys
from PIL import Image, ImageOps

image = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    valid_extensions = (".jpg", ".jpeg", ".png")
    if sys.argv[1].endswith(valid_extensions) and sys.argv[2].endswith(valid_extensions):
        try:
            # open the img
            image.append(Image.open(sys.argv[1]))
        except FileNotFoundError:
            sys.exit("File does not exist")

        # Open shirt and store the size of the shirt
        shirt = Image.open('shirt.png')
        size = shirt.size()

        # resize or crop the plain img to align with shirt
        image[0] = ImageOps.fit(image[0], size)

        # paste the shirt img to plain img
        image[0].paste(shirt, (0, 0), shirt)

        # save the edited img to desired output img file
        image[0].save(sys.argv[2])
    else:
        sys.exit("Invalid extension")
