#!/usr/bin/env bash
shutter -s -e --disable_systray # Make sure Shutter stores filepath to image in clipboard

path_to_image_file=`xclip -selection clipboard -o` # Copy from clipboard
path_to_script="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # current working directory
path_to_script+="/upload.py"

imgur_link=`python3.5 $path_to_script $path_to_image_file`
echo $imgur_link | xclip -selection clipboard # Copy to clipboard
notify-send $imgur_link