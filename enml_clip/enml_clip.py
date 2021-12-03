import pyperclip
import keyboard
import sys


def quit():
    print("exit..")
    sys.exit(0);


def enml_clip():
    dd = pyperclip.paste()
    lines = dd.split("\n")
    first = True
    first_emtpy_count = 0
    res = ""
    for line in lines:
        if not line.strip():
            continue
        print("row:" + line)
        # line_res.append(line)
        is_num_list = True
        if line.endswith(". \r"):  # 列表数字后面被直接换行了
            line = line[0:-1]
        else:
            line = line + "\n"  # 列表的实际内容
            is_num_list = False

        if first:
            while line[first_emtpy_count] == '\t':
                first_emtpy_count += 1
        if is_num_list or first:
            line = line[first_emtpy_count:]
        res += line
        first = False

    print(res)
    pyperclip.copy(res)


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+shift+q', quit)
    keyboard.add_hotkey('ctrl+shift+e', enml_clip)
    keyboard.wait()
