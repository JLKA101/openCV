import cv2
import os
from PIL import Image

path = r"C:\Users\ASUS\Documents\openCV\images2"

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
resized_path = os.path.join(path, "resized_images")

if not os.path.exists(resized_path):
    os.mkdir(resized_path )
for file in image_files:
    img = Image.open(os.path.join(path, file))
    width, height = img.size

    img.Resized = img.resize((mean_width, mean_height), Image.LANCZOS)
    img.Resized.save(os.path.join(resized_path, file), 'JPEG', quality=95)
    print(file, "is resized.")

video_name = "bts_through_the_years.mp4"

# frame = cv2.imread(image_files[0])
# height, width, layers = frame.shape #layers = colour channels

fourcc = cv2.VideoWriter_fourcc(*'mp4v') #encoding video

video = cv2.VideoWriter(video_name, fourcc, 1, (mean_width, mean_height)) #1 frame a second

if not video.isOpened():
    print("Video Writer Failed.")
    exit()

for i, image in enumerate(image_files):
    frame = cv2.imread(os.path.join(path, image))
    if frame is None:
        print("Could not read: ", image)
        continue
    frame = cv2.resize(frame, (mean_width, mean_height))

    if i ==0 :
        cv2.putText(frame, "BTS", (170, 180), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 6, cv2.LINE_AA)

        cv2.putText(frame, "Through The Years", (40, 260), cv2.FONT_HERSHEY_COMPLEX, 1, (220, 220, 220), 2, cv2.LINE_AA)

    video.write(frame)

video.release()

cv2.destroyAllWindows()

print("Video created successfully!!")

cap = cv2.VideoCapture(video_name)

if not cap.isOpened():
    print("Unable to open video")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to read frame.")
        break

    cv2.imshow("BTS Slideshow :3", frame)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break #when q is pressed output window closes

cap.release()

cv2.destroyAllWindows()