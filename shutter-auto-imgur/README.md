# shutter-auto-imgur

Since [Shutter](http://shutter-project.org/) doesn't include native support for automatically uploading a screenshot to imgur after it's been taken, I made this workaround using Python, BASH and xclip.
Tested & developed in Linux Mint 18.3.

## Requirements

* BASH
* [xclip](https://github.com/astrand/xclip)
* [Shutter](http://shutter-project.org/)
* Python 3
  * [Requests](http://docs.python-requests.org/en/master/)
* notify-send to show notification once uploaded

## How to use

1. Make sure you have a client-id stored in the text file. Get a client-id by making an imgur account and then going to the account settings.
2. Make sure that Shutter stores the filepath to the screenshot taken in the clipboard after it's been taken. Edit this in Shutter's preferences menu.
3. Add a keyboard shortcut of your liking that opens `main.sh`
