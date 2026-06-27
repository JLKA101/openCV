import cv2
import os
from PIL import Image

path = r"C:\Users\ASUS\Documents\openCV\images"

os.chdir(path)

mean_height = 0
mean_width = 0
image_files = []

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        image_files.append(file)

num_of_images = len(image_files)

for file in image_files:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width += width
    mean_height += height
    
mean_width = mean_width//num_of_images
mean_height = mean_height//num_of_images

mean_width = mean_width//2
mean_height = mean_height // 2

print("Average Width: ", mean_width)
print("Average Height: ", mean_height)

for file in image_files:
    img = Image.open(os.path.join(path, file))
    width, height = img.size

    img.Resized = img.resize((mean_width, mean_height), Image.LANCZOS)
    img.Resized.save(file, 'JPEG', quality=95)
    print(file, "is resized.")

video_name = "taehyungdnaera.avi"

frame = cv2.imread(image_files[0])
height, width, layers = frame.shape #layers = colour channels

fourcc = cv2.VideoWriter_fourcc(*'XVID') #encoding video

video = cv2.VideoWriter(video_name, fourcc, 1, (width, height)) #1 frame a second

for image in image_files:
    frame = cv2.imread(image)
    video.write(frame)

video.release()

cv2.destroyAllWindows()

print("Video created successfully!!!!")

cap = cv2.VideoCapture(video_name)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Taehyung Slideshow :P", frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break #when q is pressed output window closes

cap.release()

cv2.destroyAllWindows()