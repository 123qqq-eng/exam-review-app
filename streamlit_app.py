import os

import streamlit as st
from streamlit.components.v1 import html as components_html

st.set_page_config(page_title="期末复习助手", page_icon="📚", layout="wide")

app_dir = os.path.dirname(__file__)
html_path = os.path.join(app_dir, "app_template.html")

if not os.path.exists(html_path):
    st.error("页面模板文件不存在，请确认 app_template.html 已生成。")
    st.stop()

with open(html_path, "r", encoding="utf-8") as fh:
    page_html = fh.read()

components_html(page_html, height=2200, scrolling=True)
