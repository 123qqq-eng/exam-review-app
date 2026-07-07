import os
import streamlit as st
from streamlit.components.v1 import html as components_html

# 1. 设置页面配置
st.set_page_config(page_title="期末复习助手", page_icon="📑", layout="wide")

# 2. 添加侧边栏选择器
st.sidebar.title("导航菜单")
# 创建一个单选框，选项是你想要显示的两个页面名称
page_choice = st.sidebar.radio(
    "请选择要查看的页面：",
    ("Final Review (复习)", "Forum (论坛)")
)

# 3. 定义获取文件路径的逻辑
app_dir = os.path.dirname(__file__)

if page_choice == "Final Review (复习)":
    # 对应第一个文件名
    target_file = "final-review-website.html" 
else:
    # 对应第二个文件名
    target_file = "forum.html" 

html_path = os.path.join(app_dir, target_file)

# 4. 检查文件是否存在并显示
if not os.path.exists(html_path):
    st.error(f"错误：找不到文件 {target_file}，请确认已上传该文件。")
else:
    # 读取选中的 HTML 文件内容
    with open(html_path, "r", encoding="utf-8") as fh:
        page_html = fh.read()
    
    # 使用 components_html 渲染页面
    # height=2200 是页面高度，如果内容很长，可以调大这个数值，或者保留 scrolling=True
    components_html(page_html, height=2500, scrolling=True)
