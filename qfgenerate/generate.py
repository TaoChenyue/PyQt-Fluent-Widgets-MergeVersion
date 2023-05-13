from pathlib import Path
from typing import Dict


NOW_DIR=Path(__file__).parent
BASE_DIR=NOW_DIR.parent
LIB_LIST={"qframelesswindow":["qframelesswindow"],"qfluentwidgets":["qfluentwidgets","tools"]}
QT_LIST=["pyqt6","pyside2","pyside6","pyqt5"]

# grep each py script
file_list:Dict[str,Dict] ={}
for qt in QT_LIST:
    for lib in LIB_LIST:
        for mod in LIB_LIST[lib]:
            qf_dir = BASE_DIR/lib/qt/mod
            files = qf_dir.rglob("*.py")
            for file in files:
                rl_path=file.relative_to(BASE_DIR/lib/qt)
                file_key=str(rl_path)
                if file_key not in file_list:
                    file_list[file_key]={}
                file_list[file_key][qt]={
                        "lib":lib,
                        "name":rl_path.stem
                }
# get template
with open(str(NOW_DIR/"template.py"),"r") as f:
    template=f.read()
# generate template for each module
for k,v in file_list.items():
    fill_contents=[]
    for qt in QT_LIST:
        if qt in v.keys():
            module_tree= [qt]+k.split("\\")
            module_tree[-1]=v[qt]["name"]
            if module_tree[-1]=='__init__':
                module_tree.pop()
            fill_contents.append("from {}.{} import *".format(v[qt]["lib"],'.'.join(module_tree)))
        else:
            fill_contents.append("pass")
    Path(k).parent.mkdir(parents=True,exist_ok=True)
    with open(k,'w') as f:
        f.write(template.format(*fill_contents))
        
# add version
with open("qfluentwidgets/__init__.py","a+") as f:
    f.write("\nfrom qfgenerate import __version__")