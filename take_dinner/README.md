## 总结命令

```python
# 打包成 .exe 可执行文件
pyinstaller -F ChooseWhatToEat.py

# 打包成不带控制台 .exe 可执行文件
pyinstaller -F -w ChooseWhatToEat.py

# 指定 .exe icon 图标打包
pyinstaller -F -i favicon.ico ChooseWhatToEat.py 
```

