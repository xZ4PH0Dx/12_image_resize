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


def createParser(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input path')
    parser.add_argument('-w', '--width', help='Width')
    parser.add_argument('-he', '--height', help='Height')
    parser.add_argument('-s', '--scale', help='Scale')
    parser.add_argument('-o', '--output', help='Output file')
    return parser.parse_args()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Необходимо указать как минимум путь к файлу!')
    args = createParser(sys.argv[1:])
    input_path = args.input
    try:
        opened_image = open_image(input_path)
    except (OSError, FileNotFoundError):
        sys.exit('Не найден файл с изображением!')
    original_width, original_height = get_image_size(opened_image)
    arg_width = args.width
    arg_height = args.height
    arg_scale = args.scale
    proportion = get_proportions(original_width, original_height)

    try:
        if arg_scale:
            arg_scale = float(arg_scale)
            if arg_width or arg_height:
                sys.exit('Укажите либо масштаб либо высоту и\или ширину!')
            else:
                width = int(original_width) * arg_scale
                height = int(original_height) * arg_scale

        elif arg_width and arg_height:
            width = int(arg_width)
            height = int(arg_height)
            if get_proportions(width, height) != proportion:
                print('Пропорции отличны от оригинала!')

        elif arg_width and not arg_height:
            width = int(arg_width)
            height = width * proportion

        elif arg_height and not arg_width:
            height = int(arg_height)
            width = height * proportion

    except ValueError:
        sys.exit('Не удалось распознать параметры!')

    width = int(width)
    height = int(height)

    if args.output:
        output_path = args.output
    else:
        output_path = get_output_path(
            input_path,
            '__{0}X{1}'.format(width, height))

    processed_image = resize_image(opened_image, width, height)

    save_image(processed_image, output_path)

    print('Файл доступен по пути {}'.format(output_path))
