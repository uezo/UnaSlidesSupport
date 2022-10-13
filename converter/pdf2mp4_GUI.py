import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import *
from pdf2jpg import pdf2jpg
import subprocess
import os
import glob
import cv2
from pathlib import Path

def drop(event):
    text.set(event.data)

def pdf2mp4():
    pdf_path = text.get().strip('{ }')
    pdf_name = os.path.basename(pdf_path)
    output_dir = "./output/" + pdf_name + "_dir"
    video_name = pdf_name + "_vid"

    pdf2image(pdf_path)
    image2mp4(output_dir, video_name)
    remove_garbage(output_dir)
    return

def pdf2image(pdf_path):
    try:
        _ = pdf2jpg.convert_pdf2jpg(pdf_path, "./output/", dpi=300, pages="ALL")
        subprocess.run('explorer {}'.format(os.path.join(cwd, "output")))
        text.set("Done!")

    except Exception as e:
        text.set(e)

def image2mp4(output_dir, video_name):
    image_files = sorted(glob.glob(f"{output_dir}/*.jpg"))
    height, width, _ = cv2.imread(image_files[0]).shape[:3]
    video_writer = cv2.VideoWriter(
        f"{output_dir}/{video_name}.mp4",
        cv2.VideoWriter_fourcc('m','p','4','v'),
        1.0, (width, height))

    for image_file in image_files:
        img = cv2.imread(image_file)
        video_writer.write(img)
    video_writer.release()

def remove_garbage(output_dir):
    images = glob.glob(output_dir+'/*.jpg')
    for image in images:
        if os.path.isfile(image):
            os.remove(image)

if __name__ == "__main__":
    cwd = Path(__file__).resolve().parent
    os.chdir(cwd)

    # Main window
    main_window = TkinterDnD.Tk()
    main_window.geometry("300x300")
    main_window.title("image2mp4")

    # Button to convert
    button = ttk.Button(main_window, text = 'Convert', command=pdf2mp4)

    # Label to Drag and Drop
    text = tk.StringVar(main_window)
    text.set("PDFファイルをドラッグアンドドロップしてください\n（※日本語ファイル名不可）")
    label = ttk.Label(main_window, textvariable=text, background = "white", relief="sunken", anchor='center')
    label.drop_target_register(DND_FILES)
    label.dnd_bind("<<Drop>>", drop)

    # Widget placement
    label.pack(fill='both', padx = 30, pady = 20, expand=1)
    button.pack(fill='x', padx = 30, pady = 20, side='bottom')

    main_window.mainloop()