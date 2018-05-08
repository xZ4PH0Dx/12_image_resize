from PIL import Image
import os
import sys
import argparse


def get_output_path(args, width, height):
    if args.output:
        return args.output
    basepath, extension = os.path.splitext(args.input)
    output_path = '{}__{}X{}{}'.format(basepath, width, height, extension)
    return output_path


def open_image(path_to_original):
    return Image.open(path_to_original)


def get_image_size(image):
    return image.size


def get_proportions(width, height):
    return round(width / height, 2)


def validate_args(args_scale, args_width, args_height):
    if args_scale:
        if args_width or args_height:
            return None
        return 0
    elif args_width and args_height:
            return 1
    elif args_width or args_height:
        if args_width and not args_height:
            return 2
        else:
            return 3


def get_new_size(validation_res, original_width, original_height,
                 args_scale, args_width, args_height):
    if validation_res == 0:
        new_size = (
            int(args_scale * original_width),
            int(args_scale * original_height))
    elif validation_res == 1:
        new_size = (args_width, args_height)
    elif validation_res in (2, 3):
        if validation_res == 2:
            coefficient = get_proportions(args_width, original_width)
        elif validation_res == 3:
            coefficient = get_proportions(args_height, original_height)
        new_size = (
            int(original_width * coefficient),
            int(original_height * coefficient))
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
    args = create_parser()
    try:
        opened_image = open_image(args.input)
    except OSError:
        sys.exit('Image file not found!')
    original_width, original_height = get_image_size(opened_image)
    validated_args_res = validate_args(args.scale, args.width, args.height)
    new_width, new_height = get_new_size(
        validated_args_res,
        original_width,
        original_height,
        args.scale,
        args.width,
        args.height)
    if not (new_width, new_height):
        sys.exit("You should pass either scale or width\height")
    original_proportion = get_proportions(original_width, original_height)
    new_proportion = get_proportions(new_width, new_height)
    if new_proportion != original_proportion:
        print("New proportions doesn't match original!")
    processed_image = resize_image(
        opened_image,
        new_width,
        new_height
        )
    output_path = get_output_path(args, new_width, new_height)
    save_image(processed_image, output_path)
    print_output_path(output_path)
