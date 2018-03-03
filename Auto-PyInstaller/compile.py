from os import system, getcwd, remove
from shutil import rmtree

print("Enter the filename (example: myprogram.py)")
filename = str(input("Full filename: "))
extras = str(input("Extra modules (--noconsole --onefile): "))

command = 'start /wait cmd /c pyinstaller "%s\\%s" --specpath "%s" %s' %(getcwd(), filename, getcwd(), extras)

system(command)

rmtree(getcwd() + "\\build")
remove(getcwd() + "\\" + filename.split(".")[0] + ".spec")
