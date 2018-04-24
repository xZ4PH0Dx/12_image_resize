# Image Resizer
This program resizes your image. To process your image you should pass your a path to a file with blacklisted words as an agrument. Also you have to pass a additional parameters. If you stuck with program abilities you can run it with -h argument.
# How to run
Example of running a script with -h argument passed in.
```bash
$python3 image_resize.py -h
usage: image_resize.py [-h] [-w WIDTH] [-he HEIGHT] [-s SCALE] [-o OUTPUT]
                       input

positional arguments:
  input                 input path

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width
  -he HEIGHT, --height HEIGHT
                        Height
  -s SCALE, --scale SCALE
                        Scale
  -o OUTPUT, --output OUTPUT
                        Output file
```

Example of running a script on a Linux with a Python3 interpreter.
```bash
$python3 image_resize.py -s 2 /home/zap/git/misc/apple_raw.png
File created at /home/zap/git/misc/apple_raw__610X628.png
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
