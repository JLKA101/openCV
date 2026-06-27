import cv2
import os
from tkinter import *
from PIL import Image, ImageTk

path = r"C:\Users\ASUS\Documents\openCV\images"

images_files = []

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        images_files.append(file)

current_image = 0

root = Tk()
root.title("Photo Gallery with OpenCV :D")

def load_image():
    global photo 
    
    img_path = os.path.join(path, images_files[current_image])
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(img)
    img = img.resize((500, 400))

    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo

def next_image():
    global current_image

    current_image += 1

    if current_image >= len(images_files):
        current_image = 0
    load_image()
def prev_image():
    global current_image

    current_image -= 1

    if current_image < 0:
        current_image = len(images_files) - 1

    load_image()

def grayscale():
    global photo
    img_path = os.path.join(path, images_files[current_image])

    img = cv2.imread(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    img = Image.fromarray(gray)
    img = img.resize((500, 400))

    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo

label = Label(root)
label.pack()

load_image()

prev_btn = Button(root, text="Previous", command=prev_image)
prev_btn.pack(side=LEFT, padx=10, pady=10)

next_btn = Button(root, text="Next", command=next_image)
next_btn.pack(side=LEFT, padx=10, pady=10)

gray_btn = Button(root, text="Grayscale Filter", command=grayscale)
gray_btn.pack(side=RIGHT, padx=10, pady=10)

root.mainloop()