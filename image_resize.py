from PIL import Image
import argparse


def open_image(path_to_original):
    return Image.open(path_to_original)


def resize_image(image, width, height):
    return image.resize(width, height)


def save_image(image, path_to_result):
    image.save(path_to_result)


# def resize_image(path_to_original, path_to_result):
#    pass

# filepath +
# width
# height
# scale
# output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', required=True, help='input path')
    parser.add_argument('-w', help='Width')
    parser.add_argument('-h', help='Height')
    parser.add_argument('-s', help='Scale')
    parser.add_argument('-o', help='Output file')
    p = parser.parse_args()
