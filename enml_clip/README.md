# 介绍
复杂印象笔记的内容后，粘贴到微信输入框（或者网页的不带格式的textarea），格式会错乱（特别是针对带有列表的）
。因此开发了一个小工具，目前只支持在windows上运行，后续打算放到网页上做成在线工具。
# 运行
* 双击build目录下的enml_clip.exe
* 复制一段印象笔记内容
* 快捷键ctrl+shift+e
* 如果想改源码，打包，可以这样：
```bash
pip install pyinstaller
pyinstaller --console --onefile enml_clip.py
```
