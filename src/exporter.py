import csv
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import List, Dict
from config.settings import SAVE_DIR

class ResultExporter:
    def __init__(self):
        self.save_dir = SAVE_DIR

    def save_to_csv(self, regions: List[Dict]) -> str:
        """将分析结果保存为 CSV"""
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.save_dir / f'text_analysis_{timestamp_str}.csv'
        
        with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['检测时间', '区域编号', 'X位置', 'Y位置', '宽度', '高度', '面积'])
            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for idx, region in enumerate(regions, 1):
                writer.writerow([
                    current_time,
                    idx,
                    region['position'][0],
                    region['position'][1],
                    region['size'][0],
                    region['size'][1],
                    region['area']
                ])
        
        print(f"📊 分析结果已保存至: {filename}")
        return str(filename)

    def save_visualization(self, result_img: np.ndarray) -> str:
        """保存可视化结果图片"""
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.save_dir / f'processed_{timestamp_str}.jpg'
        cv2.imwrite(str(filename), result_img)
        print(f"🖼️ 处理后的图像已保存至: {filename}")
        return str(filename)