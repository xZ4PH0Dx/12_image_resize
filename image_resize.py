from PIL import Image
import os
import sys
import argparse


def get_output_path(args, width, height):
    if args.output:
        return args.output
    basepath = os.path.splitext(args.input)[0]
    extention = os.path.splitext(args.input)[1]
    return (basepath + '__{}X{}' + extention).format(width, height)


def open_image(path_to_original):
    return Image.open(path_to_original)


def get_image_size(image):
    return image.size


def get_proportions(width, height):
    return float(width / height)


def get_new_size(args, original_width, original_height):
    new_size = {'width': None, 'height': None}
    if args.scale:
        if args.width or args.height:
            sys.exit('You should pass either scale or width\\height')
        width = args.scale * original_width
        height = args.scale * original_height
    elif args.width and args.height:
        width = args.width
        height = args.height
        original_proportions = get_proportions(original_width, original_height)
        if get_proportions(width, height) != original_proportions:
            print('Proportions are different!')
    elif args.width and not args.height:
        coefficient = get_proportions(args.width, original_width)
        width = original_width * coefficient
        height = original_height * coefficient
    elif args.height and not args.width:
        coefficient = get_proportions(args.height, original_height)
        height = original_height * coefficient
        width = original_width * coefficient
    new_size['width'] = int(width)
    new_size['height'] = int(height)
    return new_size


def resize_image(image, width, height):
    return image.resize((width, height), Image.ANTIALIAS)


def save_image(image, path_to_result):
    image.save(path_to_result)


def print_output_path(output_path):
    print('File created at {}'.format(output_path))


def create_parser(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input path', type=str)
    parser.add_argument('-w', '--width', help='Width', type=int)
    parser.add_argument('-he', '--height', help='Height', type=int)
    parser.add_argument('-s', '--scale', help='Scale', type=float)
    parser.add_argument('-o', '--output', help='Output file', type=str)
    return parser.parse_args()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('You should put at least file path!')
    args = create_parser(sys.argv[1:])
    input_path = args.input
    try:
        opened_image = open_image(input_path)
    except (OSError, FileNotFoundError):
        sys.exit('Image file not found!')
    original_width, original_height = get_image_size(opened_image)
    proportion = get_proportions(original_width, original_height)
    new_size = get_new_size(args, original_width, original_height)
    processed_image = resize_image(
        opened_image,
        new_size['width'],
        new_size['height']
        )
    output_path = get_output_path(args, new_size['width'], new_size['height'])
    save_image(processed_image, output_path)
    print_output_path(output_path)
