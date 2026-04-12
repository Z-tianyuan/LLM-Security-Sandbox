from openai import OpenAI

# 1. 配置你的 AI 大脑 (这里以兼容 OpenAI 格式的 API 为例)
# 如果你还没有 API 密钥，可以先去注册一个便宜或免费的（如 DeepSeek, 硅基流动等）
client = OpenAI(
    api_key="96cb627f0be24320a10408625c103cbb.tJ99sSQB5RWOBW0k", 
    base_url="https://open.bigmodel.cn/api/paas/v4/" # 根据你申请的服务商替换 URL
)

# 2. 准备你要分析的“黑客流量” (这段是从你做过的 SQL 注入靶场里提取的典型特征)
malicious_request ="""
GET /post?postId=3 HTTP/2
Host: 0a070006040c9aa9809544cf00b600b9.web-security-academy.net
Cookie: session=xESHWQKgUuMaokhQOcjmPrD4Ybs4pOab
Sec-Ch-Ua: "Not-A.Brand";v="24", "Chromium";v="146"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a070006040c9aa9809544cf00b600b9.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
"""

# 3. 注入灵魂：定义 AI 的角色和任务 (Prompt Engineering)
system_prompt = """
你是一个资深的Web安全专家，精通传统漏洞（如SQLi/XSS）以及复杂的业务逻辑漏洞（如越权IDOR、访问控制缺陷）。
请审查以下 HTTP 请求，并按格式输出报告：
1. 威胁定级 (高危/中危/低危/需要人工复核)
2. 潜在漏洞类型 (请务必综合考虑越权/IDOR、逻辑漏洞、参数遍历等风险)
3. 深度分析:
   - 语法特征：有无明显的恶意 Payload？
   - 逻辑与越权风险：重点分析URL参数（如postId, userId等数字ID）与凭证（如Cookie/Token）的关系。指出这些参数是否容易被遍历？是否存在水平越权或垂直越权的潜在风险？
4. 审计建议 (告诉安全工程师下一步应该在系统里验证什么)
"""

# 4. 发送请求给 AI
# 4. 发送请求给 AI
print("正在呼叫智谱 AI 安全专家，分析流量中...\n")
response = client.chat.completions.create(
    model="glm-4-flash", # <--- 就是这里！改成智谱的模型
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"请分析这段 HTTP 请求：\n{malicious_request}"}
    ],
    temperature=0.3 
)

# 5. 打印结果
print("=== AI 流量分析报告 ===")
print(response.choices[0].message.content)