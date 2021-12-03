import pyperclip
import keyboard
import sys

def quit():
    print("exit..")
    sys.exit(0);

def enml_clip():
    dd = pyperclip.paste()
    line_res = []
    lines = dd.split("\n")
    for line in lines:
        line = line
        if not line.strip():
            continue
        #print("row:"+line)
        if line.endswith(". \r"):
            line_res.append(line[0:-2])
        else:
            line_res.append(line + "\n")
    if len(line_res) == 0:
        return

    start_empty_count = 0
    while line_res[0][start_empty_count] == ' ' or line_res[0][start_empty_count] == '\t':
        start_empty_count += 1
    for i in range(len(line_res)):
        line_res[i] = line_res[i][start_empty_count:]
        #print(line_res[i])

    res = "".join(line_res)
    print(res)
    pyperclip.copy(res)


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+shift+q', quit)
    keyboard.add_hotkey('ctrl+shift+e', enml_clip)
    keyboard.wait()