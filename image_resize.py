from PIL import Image
import os
import sys
import argparse


def get_output_path(input_path, suffix):
    basepath = os.path.splitext(input_path)[0]
    extention = os.path.splitext(input_path)[1]
    return basepath + suffix + extention


def open_image(path_to_original):
    return Image.open(path_to_original)


def get_image_size(image):
    return image.size


def get_proportions(width, height):
    return float(width / height)


def resize_image(image, width, height):
    return image.resize((width, height), Image.ANTIALIAS)


def save_image(image, path_to_result):
    image.save(path_to_result)


def print_output_path(output_path):
    print('File created at {}'.format(output_path))


def create_parser(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input path')
    parser.add_argument('-w', '--width', help='Width')
    parser.add_argument('-he', '--height', help='Height')
    parser.add_argument('-s', '--scale', help='Scale')
    parser.add_argument('-o', '--output', help='Output file')
    return parser.parse_args()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('You should put at least ffile path!')
    args = create_parser(sys.argv[1:])
    input_path = args.input
    try:
        opened_image = open_image(input_path)
    except (OSError, FileNotFoundError):
        sys.exit('Image file not found!')
    original_width, original_height = get_image_size(opened_image)
    proportion = get_proportions(original_width, original_height)

    try:
        if args.scale:
            arg_scale = float(args.scale)
            if args.width or args.height:
                sys.exit('You can put either scale or width\height!')
            else:
                width = int(original_width) * arg_scale
                height = int(original_height) * arg_scale

        elif args.width and args.height:
            width = int(args.width)
            height = int(args.height)
            if get_proportions(width, height) != proportion:
                print('Proportions are different!')

        elif args.width and not args.height:
            width = int(args.width)
            height = width * proportion

        elif args.height and not args.width:
            height = int(args.height)
            width = height * proportion

    except ValueError:
        sys.exit('Can\'t recognize the value you passed in')

    if args.output:
        output_path = args.output
    else:
        output_path = get_output_path(
            input_path,
            '__{0}X{1}'.format(int(width), int(height))
            )

    processed_image = resize_image(opened_image, int(width), int(height))

    save_image(processed_image, output_path)
    print_output_path(output_path)
