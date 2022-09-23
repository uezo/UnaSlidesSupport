import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import *
from pdf2jpg import pdf2jpg
import subprocess
import os
import glob
import cv2

def drop(event):
    print(event.data)
    text.set(event.data)

def pdf2image():
    try:
        pdf_path = text.get().strip('{ }')
        filename = os.path.basename(pdf_path)
        out_path = "./output/"
        _ = pdf2jpg.convert_pdf2jpg(pdf_path, out_path, dpi=300, pages="ALL")

        image_dir = out_path + filename + "_dir"
        filename = filename + "_vid"
        image2mp4(image_dir, filename)

        subprocess.run('explorer {}'.format(os.path.join(cwd, "output")))
        text.set("Done!")
    except Exception as e:
        text.set(e)

def image2mp4(image_dir, filename):
    image_files = sorted(glob.glob(f"{image_dir}/*.jpg"))
    height, width, _ = cv2.imread(image_files[0]).shape[:3]
    video_writer = cv2.VideoWriter(
        f"{image_dir}/{filename}.mp4",
        cv2.VideoWriter_fourcc('m','p','4','v'),
        1.0, (width, height))

    for image_file in image_files:
        img = cv2.imread(image_file)
        video_writer.write(img)
    video_writer.release()

if __name__ == "__main__":
    cwd = os.getcwd()

    # Main window
    root = TkinterDnD.Tk()
    root.geometry("300x300")
    root.title("image2mp4")

    text = tk.StringVar(root)
    text.set("PDFファイルをドラッグアンドドロップしてください")

    # Button to convert
    button = ttk.Button(root, text = 'Convert', command=pdf2image)

    # Label to Drag and Drop
    label = ttk.Label(root, textvariable=text, background = "white", relief="sunken", anchor='center')
    label.drop_target_register(DND_FILES)
    label.dnd_bind("<<Drop>>", drop)

    # Widget placement
    label.pack(fill='both', padx = 30, pady = 20, expand=1)
    button.pack(fill='x', padx = 30, pady = 20, side='bottom')

    root.mainloop()