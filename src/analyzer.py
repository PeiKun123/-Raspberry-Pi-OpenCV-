import cv2
import numpy as np
from typing import List, Dict
from config.settings import PROCESSING_CONFIG

class TextAnalyzer:
    def __init__(self):
        self.cfg = PROCESSING_CONFIG

    def detect_regions(self, binary_image: np.ndarray) -> List[Dict]:
        """
        检测文字区域
        返回: 包含位置、大小信息的字典列表
        """
        contours, _ = cv2.findContours(
            binary_image, 
            cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE
        )
        
        regions = []
        min_area = self.cfg["min_text_area"]
        min_dim = self.cfg["min_text_dim"]
        
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            area = w * h
            
            if area > min_area and w > min_dim and h > min_dim:
                regions.append({
                    'position': (x, y),
                    'size': (w, h),
                    'area': area
                })
        
        return regions