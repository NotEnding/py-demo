###总结命令
```
# 打包成.exe
pyinstaller -F ChooseWhatToEat.py 
# 不带控制台的打包
pyinstaller -F -w ChooseWhatToEat.py 
# 打包指定exe图标打包
pyinstaller -F -i favicon.ico ChooseWhatToEat.py 
```
