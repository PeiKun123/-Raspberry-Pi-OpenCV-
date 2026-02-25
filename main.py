import matplotlib.pyplot as plt
import cv2
import numpy as np
from src.camera import CameraController
from src.processor import ImageProcessor
from src.analyzer import TextAnalyzer
from src.exporter import ResultExporter

def visualize_results(original, enhanced, result_img, ssim_score):
    """使用 Matplotlib 展示结果"""
    plt.figure(figsize=(15, 5))
    
    # 子图 1: 原始图像
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title('原始图像')
    plt.axis('off')
    
    # 子图 2: 增强图像
    plt.subplot(132)
    plt.imshow(enhanced, cmap='gray')
    plt.title(f'增强后的图像 (SSIM: {ssim_score:.3f})')
    plt.axis('off')
    
    # 子图 3: 识别结果
    plt.subplot(133)
    plt.imshow(cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB))
    plt.title('文字识别结果')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    print("🚀 启动智能视觉分析系统...")
    
    # 初始化模块
    camera = CameraController()
    processor = ImageProcessor()
    analyzer = TextAnalyzer()
    exporter = ResultExporter()
    
    # 1. 拍摄
    img_path = camera.capture_image()
    if not img_path:
        print("❌ 未获取到图像，程序退出。")
        return

    # 2. 读取与处理
    original = cv2.imread(img_path)
    if original is None:
        print("❌ 无法读取图像文件。")
        return

    enhanced, processed = processor.preprocess(original)
    ssim_score = processor.calculate_ssim(original, enhanced)
    print(f"📈 SSIM Index: {ssim_score:.4f}")
    
    # 3. 分析
    regions = analyzer.detect_regions(processed)
    print(f"🔍 检测到 {len(regions)} 个潜在文字区域。")
    
    # 4. 绘制结果框
    result_img = np.ones_like(processed) * 255
    result_img = cv2.bitwise_and(result_img, processed)
    result_img = cv2.cvtColor(result_img, cv2.COLOR_GRAY2BGR)
    
    for region in regions:
        x, y = region['position']
        w, h = region['size']
        cv2.rectangle(result_img, (x, y), (x+w, y+h), (0, 128, 0), 2)
    
    # 5. 导出与展示
    exporter.save_to_csv(regions)
    exporter.save_visualization(result_img)
    
    # 显示界面 (阻塞直到用户关闭)
    visualize_results(original, enhanced, result_img, ssim_score)
    
    print("✅ 任务完成。")

if __name__ == "__main__":
    main()