# AI 学习记录

> 从软件测试工程师转型大模型应用开发工程师的学习仓库。
> 起点：2026-11 · 目标：12 个月内完成转型。

## 这是什么

记录从测试工程师到大模型应用开发的转型过程。主线技术栈是 Python + LangChain/LangGraph + RAG + FastAPI，作品集方向是「测试背景 × AI」——自动化测试 Agent / 用例生成。

当前处于 W1（环境与工程习惯），已完成环境搭建、git 基础、冲突解决与 GitHub 推送。

## 怎么跑

环境要求：Python 3.12+（当前使用 3.15.2）、uv、git。

```powershell
# 1. 克隆仓库
git clone https://github.com/Sycamore550/ai-learning.git
cd ai-learning

# 2. 创建虚拟环境并安装依赖
uv venv
uv pip install pydantic

# 3. 运行示例脚本
python scripts/hello_checker.py
# 预期输出：True
```

> Windows PowerShell 用户注意：不要用 `echo "x" > file` 写文本文件（会写成 UTF-16，git 视为二进制）。改用 `"x" | Set-Content file -Encoding utf8`。

## 目录结构

```text
ai-learning/
├── README.md            # 项目说明（本文件）
├── pyproject.toml       # 项目配置与依赖清单
├── .env.example         # 环境变量示例（后续放 API Key 占位）
├── .python-version      # uv 记录的 Python 版本
├── .gitignore           # 忽略虚拟环境、缓存、密钥
├── src/
│   └── ai_learning/     # 正式代码（后续模块化迁移到这里）
└── scripts/
    └── hello_checker.py # 练习脚本：检查测试用例标题是否合规
```

## 当前进度

### 已完成

- 环境搭建：Python 3.15.2 / uv / git / VS Code
- 虚拟环境与依赖管理：`.venv` + pydantic
- git 基础：add / commit / log / diff / branch / merge，并亲手解决一次合并冲突
- GitHub 远程仓库推送：`Sycamore550/ai-learning`
- README 与目录结构整理

### 计划中

- W2：从脚本到模块——把 `hello_checker` 扩展成带类型注解、配置、日志、CLI 的 `case-checker` 工具
- W3：pytest 测试，覆盖率 ≥ 70%
- W4：用 httpx 调用外部接口（超时、重试、异常处理）
- W5：整合第一个可放简历的完整项目
- W6-W8：数学直觉 + 首次调用国内大模型 API + Prompt 工程 + 用例生成器 v0.1

## 说明

本项目为个人学习记录，所有用例数据均为脱敏或虚构内容，不涉及任何公司业务数据。
