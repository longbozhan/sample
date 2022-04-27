import os

"""
根据当前工程目录的名字，改cmake最终生产的bin_name。
"""

def get_bin_name():
    return os.path.basename(os.getcwd())

# CMakeLists.txt
def process_cmake():
    filename = "CMakeLists.txt"
    content = open(filename).read()
    if not content:
        print("file invalid:%s" % (filename))
        return
    with open(filename, "w") as fp:
        pos_start = content.find("set(BIN_NAME ")
        if not pos_start:
            print("cmakefile bin name not found, content:%s" % (content))
            return
        pos_end = content.find("\n", pos_start)
        if not pos_end:
            print("cmake file bin name not found new line, content:%s" % (content))
            return
        #print("start:%s end:%s" % (pos_start, pos_end))
        pat = content[pos_start: pos_end]
        #print("pat:%s" % (pat))
        new_pat = "set(BIN_NAME \"%s\")" % (get_bin_name())
        fp.write(content.replace(pat, new_pat))
        fp.close()
    print("process cmake success")

process_cmake()