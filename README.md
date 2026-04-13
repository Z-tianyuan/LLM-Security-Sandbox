# 🛡️ LLM Security Sandbox (大模型安全攻防与审计沙箱)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-FF4B4B)
![SQLite](https://img.shields.io/badge/SQLite-Local-lightgrey)
![LLM Security](https://img.shields.io/badge/Security-Prompt_Injection-red)

> 🚀 **一个面向企业级场景的大语言模型（LLM）安全攻防演练与批量审计工具。**

## 📖 项目背景

随着大模型在各类业务中的广泛落地，**提示词注入（Prompt Injection）** 和 **大模型幻觉越狱（Jailbreak）** 已成为最核心的安全威胁。

本项目旨在构建一个高度可视化的红蓝对抗沙箱，不仅提供单点漏洞测试环境，更引入了纵深防御机制与自动化审计引擎，极大提升安全研究人员探测大模型边界漏洞的效率。

## ✨ 核心特性 (Features)

* **🛡️ 纵深防御架构 (Dual-Layer WAF)：**
    * **静态过滤层：** 基于正则表达式拦截 `Base64`、`忽略指令` 等传统注入特征。
    * **AI 语义审计层：** 引入前置小模型（Flash）进行恶意意图预判，有效阻断高隐蔽性的“小说嵌套法”、“情境扮演”等高级幻觉诱导攻击。

* **🚀 批量自动化引擎 (Batch Audit Engine)：**
    * 内置基于 `Pandas` 的异步清洗引擎，支持 `.csv` 格式的测试用例高并发输入。
    * 自动进行威胁定级（🔴 高危 / 🟡 中危 / 🟢 拦截 / 🟢 安全）。

* **📊 数据持久化与溯源 (Data Persistence)：**
    * 通过 `SQLite` 实时记录所有攻防日志，为后续 LLM 安全对齐（Alignment）训练提供高质量的负面数据集。
    * 支持一键导出合规安全评估报告。

## 📸 运行截图 (Screenshots)

*图 1：双层智能防火墙成功拦截高级注入攻击*
![防火墙拦截](images/firewall.png)

*图 2：批量自动化审计引擎运行报表*
![审计报表](images/report.png)

## ⚙️ 快速开始 (Quick Start)

**1. 克隆项目**
```bash
git clone [https://github.com/你的用户名/LLM-Security-Sandbox.git](https://github.com/你的用户名/LLM-Security-Sandbox.git)
cd LLM-Security-Sandbox
````

**2. 安装依赖**

```
pip install streamlit openai pandas
```

**3. 启动沙箱**

```
streamlit run ai-沙箱.py
```
_(系统将在浏览器自动打开 `http://localhost:8501`)_
## ⚠️ 免责声明 (Disclaimer)
本项目仅供网络安全及人工智能专业的教育与授权安全测试使用。请勿用于未授权的非法攻击。开发者不对使用该工具造成的任何后果负责。