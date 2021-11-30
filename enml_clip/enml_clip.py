import pyperclip
import keyboard
import sys

def quit():
    sys.exit(0);

def enml_clip():
    dd = pyperclip.paste()
    res = ""
    lines = dd.split("\n")
    for line in lines:
        line = line
        if not line.strip():
            continue
        if line.endswith(" \r"):
            res += line[0:-2]
        else:
            res += line + "\n"
    print(res)
    pyperclip.copy(res)


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+shift+q', quit)
    keyboard.add_hotkey('ctrl+shift+e', enml_clip)
    keyboard.wait()