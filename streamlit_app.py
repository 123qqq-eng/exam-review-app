import streamlit as st

# 页面设置
st.set_page_config(page_title="期末急救中心", layout="wide")
st.title("📚 期末考试复习资料库")

# --- 1. 模拟数据库：期末复习资料 ---
# 结构：{科目: {知识点标题: 内容}}
# 你可以把这里的内容换成你真正整理的笔记
final_data = {
    "高等数学": {
        "知识点 1: 多元函数极限": "**定义**：$\lim_{(x,y)\to(x_0,y_0)} f(x,y)$。\n**解法**：沿着不同路径趋近，若极限不同则不存在。\n**例题**：求 $\lim_{x\to 0, y\to 0} \frac{xy}{x^2+y^2}$ ...",
        "知识点 2: 偏导数与全微分": "**偏导**：对 x 求导时把 y 看作常数。\n**全微分**：$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$。",
        "知识点 3: 二重积分": "**直角坐标** $\int\int_D dxdy$ vs **极坐标** $\int\int_D r dr d\theta$。注意画图定限。"
    },
    "线性代数": {
        "知识点 1: 行列式计算": "**降阶法**：利用性质把某一行化为只有一个非零元素。\n**特殊行列式**：对角、三角行列式等于主对角线乘积。",
        "知识点 2: 矩阵与逆": "**求逆公式**：$A^{-1} = \frac{A^*}{|A|}$。\n**初等变换法**：$(A|E) \to (E|A^{-1})$。"
    },
    "有机化学": {
        "知识点 1: 自由基取代": "**条件**：光照或高温。\n**活性**：叔氢 > 仲氢 > 伯氢。",
        "知识点 2: 亲核加成": "**羰基**是缺电子中心。\n**马氏规则**：氢加在含氢多的碳上。"
    },
    "物理化学": {
        "知识点 1: 麦克斯韦关系式": "四大关系式的记忆口诀：\n$PV=RT$ 的偏导循环。",
        "知识点 2: 化学平衡": "**平衡常数** $K_p$ 与 $\Delta G$ 的关系。\n$\Delta G = -RT \ln K$。"
    }
}

# --- 2. 侧边栏导航 ---
st.sidebar.header("选择科目")
subject = st.sidebar.radio("点击进入复习区：", list(final_data.keys()))

# --- 3. 核心功能区：知识点展示与解锁 ---
st.header(f"🔥 {subject} · 期末重点突破")

# 遍历当前科目的知识点
for key, content in final_data[subject].items():

    # 创建折叠面板 (Expander)，标题是知识点
    with st.expander(f"📖 {key}"):

        # 先显示摘要（或者题目）
        st.markdown(f"*{content.split('.')[0]}...*")

        # --- 模拟“锁定”状态 ---
        # 这里用一个简单的按钮代替广告/支付
        lock_button = st.button(f"🔒 点击解锁详细解析与例题", key=f"lock_{key}")

        if lock_button:
            # 模拟解锁成功后的状态
            st.session_state[f"{key}_unlocked"] = True

        # --- 判断是否解锁 ---
        if st.session_state.get(f"{key}_unlocked", False):
            st.success("✅ 解锁成功！祝考试顺利")
            st.markdown(content)  # 显示完整内容
        else:
            # 未解锁时的占位和提示
            st.warning("👆 点击上方按钮解锁解析")
            st.image(
                "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2QzYjQ1ZWEwYjQ1ZWEwYjQ1ZWEwYjQ1ZWEwYjQ1ZWEwYjQ1ZWEwYjQ1ZWEw/3o7TKoWXm3okO1kgHC/giphy.gif",
                width=300)  # 放个搞笑动图占位

# --- 4. 底部广告位模拟 (模拟变现) ---
st.markdown("---")
st.subheader("💰 资源赞助区")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📺 观看 30s 广告解锁全部"):
        st.balloons()  # 放气球庆祝
        st.info("广告功能正在对接中，暂且免费开放！")
        # 实际开发中，这里会调用广告 SDK
with col2:
    if st.button("💳 赞助 9.9 元获取全套 PDF"):
        st.success("感谢支持！加群获取资料。")
with col3:
    st.metric("已帮助", "128", "位学长学姐上岸")