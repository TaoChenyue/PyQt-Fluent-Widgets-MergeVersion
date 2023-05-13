git checkout -b forbuild
pdm run qf_all
pdm run generate
pdm build
rm -rf ./qframelesswindow
rm -rf ./qfluentwidgets
git clean -df
git checkout qtpy
git branch -D forbuild