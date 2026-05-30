# ketang-test

这是一个静态作品集项目（演示用），包含用于教育类案例展示的页面与素材。下面是快速本地预览与开发说明：

快速预览

1. 确保已安装 Python（项目内含虚拟环境）。
2. 在项目根目录运行本地静态服务器：

```powershell
cd "c:\Users\Administrator\Desktop\测试\ketang-test"
.venv\Scripts\python.exe -m http.server 8000
```

3. 在浏览器打开 http://localhost:8000 查看页面（`index.html` 为入口）。

常用命令

- 生成封面图：`.venv\Scripts\python.exe generate_covers.py`
- 生成 logo 缩略图：`.venv\Scripts\python.exe create_thumbs.py`
- 提交并推送：`git add . && git commit -m "msg" && git push`

若需我继续优化页面、补充图集或接入真实素材，请告诉我具体优先项。 