# 🛡️ LLM Security Sandbox (企业级大模型安全攻防与多模型竞技沙箱)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![SQLite](https://img.shields.io/badge/SQLite-Local-lightgrey)
![LLM Security](https://img.shields.io/badge/Security-Prompt_Injection-red)
![Model Arena](https://img.shields.io/badge/Feature-Model_Arena-purple)

> 🚀 **一个面向企业级场景的 LLM 提示词注入（Prompt Injection）与越狱（Jailbreak）自动化攻防演练工作台。**

## 📖 项目背景

随着大模型在各类业务中的广泛落地，大模型幻觉与提示词注入已成为最核心的安全威胁。
本项目旨在构建一个高度可视化的红蓝对抗沙箱，不仅提供“纵深防御”的 WAF 拦截环境，更引入了 **“多模型鲁棒性基准测试（Model Arena）”** 与 **“自动化批量审计引擎”**，极大提升安全研究人员探测大模型边界漏洞与对齐策略（Alignment）的效率。

## ✨ 核心特性 (Core Features)

* **⚔️ 多模型并发竞技场 (Model Arena)：**
    * 支持同时下发相同 Payload 至多个不同参数量/推理能力的大模型（如轻量级 Flash 与 具备深度思考能力的推理模型）。
    * 直观对比弱模型的“情境幻觉”与强模型的“底层意图识别（Intent Alignment）”差异。
* **🛡️ 纵深防御架构 (Dual-Layer WAF) 与“上帝模式”：**
    * **静态过滤层：** 基于正则表达式拦截 `Base64`、`忽略指令` 等传统注入特征。
    * **AI 语义审计层：** 引入前置预审小模型进行恶意意图预判，有效阻断高隐蔽性的“小说嵌套法”等高级诱导攻击。
    * **物理开关：** 支持一键关闭 WAF，让攻击载荷直击底层核心模型，进行极速原生防御力探测。
* **🚀 批量自动化引擎 (Batch Audit Engine)：**
    * 内置基于 `Pandas` 的异步清洗引擎，支持 `.csv` 格式的测试用例高并发输入。
    * 自动进行威胁定级（🔴 高危 / 🟡 中危 / 🟢 拦截 / 🟢 安全）。
* **📊 数据持久化与溯源 (Data Persistence)：**
    * 通过 `SQLite` 实时记录所有攻防日志，为后续 LLM 安全对齐训练提供高质量的负面数据集（Negative Samples）。
    * 支持一键导出 CSV 格式的合规安全评估报告。

## 📸 运行截图 (Screenshots)

*(💡 提示：在你的电脑上截取最新 V4 版本的运行图，放到 `images` 文件夹下替换以下图片)*

<p align="center">
  <img src="images/firewall.png" width="90%" />
  <br>
  <b>图 1：多模型竞技场 —— WAF 关闭状态下，强弱模型的原生防御力对比</b>
</p>

<p align="center">
  <img src="images/report.png" width="90%" />
  <br>
  <b>图 2：批量自动化审计引擎运行报表</b>
</p>

## ⚙️ 快速开始 (Quick Start)

**1. 克隆项目**
```bash
git clone [https://github.com/你的用户名/LLM-Security-Sandbox.git](https://github.com/你的用户名/LLM-Security-Sandbox.git)
cd LLM-Security-Sandbox

2. 安装依赖
pip install streamlit openai pandas

3. 启动沙箱
streamlit run ai-沙箱.py
(系统将在浏览器自动打开 http://localhost:8501)

⚠️ 免责声明 (Disclaimer)
本项目仅供网络安全及人工智能专业的教育与授权安全测试使用。请勿用于未授权的非法攻击。开发者不对使用该工具造成的任何后果负责。