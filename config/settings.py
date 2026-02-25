import os
from pathlib import Path

# 基础路径配置
BASE_DIR = Path(__file__).resolve().parent.parent
SAVE_DIR = Path.home() / "Desktop" / "pictures"

# 确保保存目录存在
SAVE_DIR.mkdir(parents=True, exist_ok=True)

# 图像处理参数
PROCESSING_CONFIG = {
    "gaussian_kernel": (5, 5),
    "median_kernel": 3,
    "clahe_clip_limit": 2.0,
    "clahe_tile_grid": (8, 8),
    "adaptive_thresh_block_size": 15,
    "adaptive_thresh_c": 4,
    "morph_kernel_size": (2, 2),
    "min_text_area": 50,
    "min_text_dim": 5
}

# 相机命令配置
CAMERA_CMD_TEMPLATE = "libcamera-still -t 0 --timelapse 100 -o {output_path} --immediate"