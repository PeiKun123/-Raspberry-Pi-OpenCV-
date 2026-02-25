# 📸 Smart Vision Analyzer (智能视觉分析系统)

基于 OpenCV 和 scikit-image 的轻量级图像预处理与文字区域检测工具。专为树莓派或 Linux 环境设计，支持 `libcamera` 硬件调用，具备自动降噪、对比度增强 (CLAHE)、自适应阈值分割及结果可视化功能。

## ✨ 主要功能

- **📷 硬件集成**: 自动调用 `libcamera-still` 进行图像捕获。
- **🎨 图像增强**: 
  - 高斯模糊与中值滤波双重降噪。
  - CLAHE (限制对比度自适应直方图均衡化) 提升细节。
  - 自适应阈值二值化适应不同光照。
- **🔍 智能分析**: 基于轮廓检测自动定位文字/物体区域。
- **📊 质量评估**: 计算 SSIM (结构相似性) 指数评估增强效果。
- **💾 数据导出**: 自动生成 CSV 分析报告及带标注的结果图片。

## 📂 项目结构

```text
smart-vision-analyzer/
├── config/             # 配置文件 (路径、算法参数)
├── src/                # 核心源代码
│   ├── camera.py       # 相机控制
│   ├── processor.py    # 图像处理算法
│   ├── analyzer.py     # 区域分析逻辑
│   └── exporter.py     # 数据导出
├── tests/              # 单元测试
├── main.py             # 程序入口
├── requirements.txt    # 依赖列表
└── README.md           # 项目文档


安装指南
前置要求
Python 3.8+
Linux 环境 (推荐 Raspberry Pi OS)
已安装 libcamera-tools
# 1. 克隆项目
git clone https://github.com/yourusername/smart-vision-analyzer.git
cd smart-vision-analyzer

# 2. 创建虚拟环境 (推荐)
python3 -m venv venv
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. (仅限树莓派) 确保安装 libcamera
sudo apt update
sudo apt install libcamera-tools


程序启动后会自动打开相机预览。
按 Ctrl+C 触发拍照并退出预览。
系统自动处理图像，并在桌面 ~/Desktop/pictures 目录下保存：
原始截图
处理后的标注图
CSV 分析数据
弹出窗口展示对比结果及 SSIM 评分。
