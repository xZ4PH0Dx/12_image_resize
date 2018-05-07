from PIL import Image
import os
import sys
import argparse


def get_output_path(args, width, height):
    if args.output:
        return args.output
    basepath = os.path.splitext(args.input)[0]
    extention = os.path.splitext(args.input)[1]
    output_path = (basepath + '__{}X{}' + extention).format(width, height)
    return output_path


def open_image(path_to_original):
    return Image.open(path_to_original)


def get_image_size(image):
    return image.size


def get_proportions(width, height):
    return round(float(width / height), 2)


def get_new_size(args, original_width, original_height):
    if args.scale:
        if args.width or args.height:
            return None
        new_size= (int(args.scale * original_width),
                   int(args.scale * original_height))
    elif args.width and args.height:
        new_size = (args.width, args.height)
    elif args.width or args.height:
        if args.width and not args.height:
            coefficient = get_proportions(args.width, original_width)
        else:
            coefficient = get_proportions(args.height, original_height)
        new_size = (int(original_width * coefficient), int(original_height * coefficient))
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
    args = create_parser(sys.argv[1:])
    input_path = args.input
    try:
        opened_image = open_image(input_path)
    except (OSError, FileNotFoundError):
        sys.exit('Image file not found!')
    original_width, original_height = get_image_size(opened_image)
    new_width, new_height = get_new_size(args, original_width, original_height)
    if not (new_width, new_height):
        sys.exit('You should pass either scale or width\\height')
    original_proportion = get_proportions(original_width, original_height)
    new_proportion = get_proportions(new_width, new_height)
    if new_proportion != original_proportion:
        print('New proportions doesn\'t match original!')
    processed_image = resize_image(
        opened_image,
        new_width,
        new_height
        )
    output_path = get_output_path(args, new_width, new_height)
    save_image(processed_image, output_path)
    print_output_path(output_path)
