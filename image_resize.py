from PIL import Image
import sys
import argparse


def open_image(path_to_original):
    return Image.open(path_to_original)


def resize_image(image, width, height):
    return image.resize(width, height)


def save_image(image, path_to_result):
    image.save(path_to_result)


def createParser(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input path')
    parser.add_argument('-w', '--width', help='Width')
    parser.add_argument('-he', '--height', help='Height')
    parser.add_argument('-s', '--scale', help='Scale')
    parser.add_argument('-o', '--output', help='Output file')
    return parser.parse_args()

# def resize_image(path_to_original, path_to_result):
#    pass

# filepath +
# width
# height
# scale
# output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Необходимо указать как минимум путь к файлу')
    args = createParser(sys.argv[1:])


