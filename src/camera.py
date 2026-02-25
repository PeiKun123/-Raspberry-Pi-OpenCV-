import subprocess
import os
from datetime import datetime
from pathlib import Path
from config.settings import SAVE_DIR, CAMERA_CMD_TEMPLATE

class CameraController:
    def __init__(self):
        self.save_dir = SAVE_DIR

    def capture_image(self) -> str | None:
        """
        调用 libcamera 拍摄图像
        返回: 图片路径，失败返回 None
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capture_{timestamp}.jpg"
        output_path = self.save_dir / filename

        cmd = CAMERA_CMD_TEMPLATE.format(output_path=output_path)
        
        print("📷 准备拍摄，按 Ctrl+C 拍照并退出预览...")
        try:
            subprocess.run(cmd, shell=True, check=True)
            
            if output_path.exists():
                print(f"✅ 图像已保存至: {output_path}")
                return str(output_path)
            else:
                print("❌ 拍摄失败：文件未生成")
                return None
                
        except subprocess.CalledProcessError:
            # libcamera 被中断时可能会抛出此错误，检查文件是否存在
            if output_path.exists():
                print(f"✅ 图像已保存至: {output_path}")
                return str(output_path)
            return None
        except KeyboardInterrupt:
            if output_path.exists():
                print(f"✅ 图像已保存至: {output_path}")
                return str(output_path)
            return None
        except Exception as e:
            print(f"❌ 发生未知错误: {e}")
            return None