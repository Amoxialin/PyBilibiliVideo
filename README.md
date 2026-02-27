# 🚀 Bilibili-Video-Crawler (分布式多媒体数据采集与自动化处理系统)

## 📖 项目简介
本项目是一个针对复杂流媒体平台（以 Bilibili 为例）开发的自动化视频数据并发采集与处理工具。有效解决了音视频分离传输的抓取难题，并实现了从网络请求、数据解析到本地无损合成的端到端自动化流水线。

## ✨ 核心亮点 (Features)
* **对抗反爬机制：** 深度剖析平台抓包接口，通过自定义 Headers（伪装 `User-Agent` 与绕过 `Referer` 校验），成功实现稳定抓取。
* **DASH 视频流解析：** 针对 Bilibili 的音视频分离传输特性，动态解析 JSON 数据，精准提取独立的 audio 和 video 二进制流地址。
* **自动化音画无损合成：** 摒弃繁琐的手动操作，利用 Python 的 `subprocess` 模块调用系统级 `FFmpeg` 指令，实现音视频文件的自动化无损合并，并在完成后自动清理冗余临时文件。

## 🛠️ 技术栈 (Tech Stack)
* **开发语言：** Python 3.x
* **核心库：** `Requests` (网络请求), `JSON` (数据解析), `subprocess` (系统调用)
* **外部工具：** `FFmpeg` (音视频处理)

## 🚀 快速开始 (Quick Start)
1. 确保本地已安装 Python 3.8+ 及完整配置了 FFmpeg 环境变量。
2. 克隆本项目到本地：
   `git clone https://github.com/你的GitHub用户名/Bilibili-Video-Crawler.git`
3. 安装依赖（如果使用了第三方库）：
   `pip install -r requirements.txt`
4. 运行脚本：
   `python main.py`

## 💡 难点与故障复盘
* **难点：** 抓取高画质视频时遭遇 403 拦截。
* **解决方案：** 经过抓包分析，发现平台对请求来源有严格校验，通过在 Headers 中动态补全对应视频的防盗链（Referer）参数，成功解决该拦截。

