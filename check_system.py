import shutil
import subprocess

# Kiểm tra xem hệ thống có thấy lệnh ffmpeg không
ffmpeg_path = shutil.which('ffmpeg')

if ffmpeg_path:
    print(f"--- THANH CONG ---")
    print(f"Tim thay FFmpeg tai: {ffmpeg_path}")
    # Chạy thử lệnh lấy version
    version = subprocess.check_output(['ffmpeg', '-version']).decode('utf-8').split('\n')[0]
    print(f"Phien ban: {version}")
else:
    print("--- THAT BAI ---")
    print("Khong tim thay FFmpeg. Hay chay: sudo apt install ffmpeg")
