import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from config.settings import PROCESSING_CONFIG

class ImageProcessor:
    def __init__(self):
        self.cfg = PROCESSING_CONFIG

    def preprocess(self, image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """
        执行完整的图像预处理流程
        返回: (增强后的灰度图, 二值化处理图)
        """
        # 1. 转灰度
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 2. 降噪 (高斯 + 中值)
        denoised = cv2.GaussianBlur(gray, self.cfg["gaussian_kernel"], 0)
        denoised = cv2.medianBlur(denoised, self.cfg["median_kernel"])
        
        # 3. CLAHE 对比度增强
        clahe = cv2.createCLAHE(
            clipLimit=self.cfg["clahe_clip_limit"], 
            tileGridSize=self.cfg["clahe_tile_grid"]
        )
        enhanced = clahe.apply(denoised)
        
        # 4. 自适应阈值二值化
        processed = cv2.adaptiveThreshold(
            enhanced,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            self.cfg["adaptive_thresh_block_size"],
            self.cfg["adaptive_thresh_c"]
        )
        
        # 5. 形态学操作去噪
        kernel = np.ones(self.cfg["morph_kernel_size"], np.uint8)
        processed = cv2.morphologyEx(processed, cv2.MORPH_OPEN, kernel)
        processed = cv2.morphologyEx(processed, cv2.MORPH_CLOSE, kernel)
        processed = cv2.medianBlur(processed, self.cfg["median_kernel"])
        
        return enhanced, processed

    def calculate_ssim(self, original_bgr: np.ndarray, enhanced_gray: np.ndarray) -> float:
        """计算原始图与增强图的 SSIM 指数"""
        original_gray = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2GRAY)
        return ssim(original_gray, enhanced_gray)