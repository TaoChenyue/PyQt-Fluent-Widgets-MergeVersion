# PyQt-Fluent-Widgets[merge]

This is a multi branch merged code repository used to solve the problem of package name conflicts between different branches of the [original repository](https://github.com/zhiyiYo/PyQt-Fluent-Widgets.git) in the same virtual environment.

## Modifications

1. Clone different branches and put them into same directory.
2. Import ``qtpy``to determine which QT_API to use.

## Install

```shell
## download wheel or tar.gz in Release
pip install xxx.tar.gz
## or build the package using pdm scripts, virtual environment is recommanded
pip install pdm
pdm install -G:all
pdm run auto_build
pip install dist/xxx.tar.gz
```

## Usage

```powershell
## Set QT_API in terminals 
# powershell
$env:QT_API="pyqt6"
# cmd
set QT_API="pyqt6"
# shell
export QT_API="pyqt6"
...

## Set QT_API in python script(must set before importing qtpy)
import os
os.environ["QT_API"]="pyqt6"

## Then just use the library as normal
```