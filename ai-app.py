import streamlit as st
from openai import OpenAI

# 页面配置
st.set_page_config(page_title="AI 安全分析专家", layout="wide")
st.title("🛡️ AI 辅助网络安全分析助手")

# 侧边栏配置
with st.sidebar:
    st.header("API 设置")
    api_key = st.text_input("输入智谱 API Key", type="password")
    model = st.selectbox("选择模型", ["glm-4-flash", "glm-4"])
    
# 主界面
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 输入流量/日志")
    raw_input = st.text_area("粘贴 HTTP 请求包或日志内容", height=400, placeholder="GET /post?postId=3 HTTP/2...")
    
    analyze_btn = st.button("🚀 开始 AI 深度分析", use_container_width=True)

with col2:
    st.subheader("📊 AI 分析报告")
    if analyze_btn:
        if not api_key:
            st.error("请先在左侧填入 API Key！")
        elif not raw_input:
            st.warning("请先粘贴需要分析的内容！")
        else:
            with st.spinner("安全专家正在审阅流量..."):
                try:
                    client = OpenAI(api_key=api_key, base_url="https://open.bigmodel.cn/api/paas/v4/")
                    
                    system_prompt = """
                    你是一个资深的Web安全专家。请分析用户提供的HTTP请求。
                    1. 给出威胁定级。
                    2. 识别潜在漏洞类型（包含SQLi, XSS, SSRF, 逻辑越权IDOR等）。
                    3. 给出详细的原理分析和人工验证建议。
                    """
                    
                    response = client.chat.completions.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": raw_input}
                        ]
                    )
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"分析出错: {e}")
    else:
        st.info("在左侧粘贴流量并点击开始分析。")