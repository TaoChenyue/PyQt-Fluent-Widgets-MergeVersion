import re
with open("qfluentwidgets/pyqt5/setup.py",'r') as f:
    content=f.read()
with open("qfgenerate/__init__.py","w") as f:
    f.write("__version__ ={}".format(re.findall("version=(.*),",content)[0]))