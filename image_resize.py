from PIL import Image
import os
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

def get_output_path(input_path, suffix):
    basepath = os.path.splitext(input_path)[0]
    extention = os.path.splitext(input_path)[1]
    return basepath + suffix + extention


def get_param_value(param_name):
    if args.param_name:
        return args.param_name
    else:
        return None

# filepath +
# width
# height
# scale
# output

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Необходимо указать как минимум путь к файлу')
    args = createParser(sys.argv[1:])
    input_path = args.input
    width = get_param_value(width)
    if args.output:
        output_path = args.output
    else:
        output_path = get_output_path(input_path, '__{0}X{1}'.format(width,height))
    print(width)