# 事前に pip install opencv-python==4.6.0.66 でopencvをインストールしてください

import sys
import glob
import cv2

fps = 1.0   # 1フレームあたりのスライド数。1.0で1スライド/1秒、2.0で2スライド/1秒

def image2mp4(image_dir, filename):
    image_files = sorted(glob.glob(f"{image_dir}/*.png"))
    height, width, _ = cv2.imread(image_files[0]).shape[:3]
    video_writer = cv2.VideoWriter(
        f"{image_dir}/{filename}.mp4",
        cv2.VideoWriter_fourcc('m','p','4','v'),
        fps, (width, height))

    for image_file in image_files:
        img = cv2.imread(image_file)
        video_writer.write(img)
    video_writer.release()


if __name__ == "__main__":
    args = sys.argv
    
    image_dir = args[1]
    if len(args) >= 3:
        filename = args[2]
    else:
        filename = "unaslides"

    image2mp4(image_dir, filename)
