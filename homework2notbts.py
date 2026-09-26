#face filter

import cv2, sys, numpy, os

size = 4 #scaling factor for detection
haar_file = 'haarcascade_frontalface_default.xml' #detect faces
datasets = 'datasets' #where faces will be sTORED

filter = cv2.imread("sprout.png", cv2.IMREAD_UNCHANGED)

print('Identifying Face. Please be in sufficent lighting.')

(images, labels, names, id) = ([], [], {}, 0) #{} = dictionary, seperate folders for different people as subfolders in the folder datasets

for (subdirs, dirs, files) in os.walk(datasets): #everything
    for subdir in dirs:
        names[id] = subdir #subdir = name, index = person
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath +'/' + filename
            label = id
            images.append(cv2.imread(path, 0)) #convert to grayscale, then store
            labels.append(int(label))
        id += 1 #next person (next index)

(width, height) = (130, 100)

(images, labels) = [numpy.array(lis) for lis in [images, labels]]
model = cv2.face.LBPHFaceRecognizer_create() #from datasets folder
model.train(images, labels) #image id and person id (labels)
face_cascade = cv2.CascadeClassifier(haar_file) #locate faces in webcam frames
webcam = cv2.VideoCapture(0)

while True: #all frames continuously processed
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces: #create rect for face detection
       
       
        face = gray[y:y + h, x:x + w] #face cropping region
        face_resize = cv2.resize(face, (width, height)) #resize face for training size
        prediction = model.predict(face_resize)

        filter_width = w
        filter_height = int(filter.shape[0]*filter_width/filter.shape[1])

        filter_rs = cv2.resize(
            filter,
            (filter_width, filter_height)

        )

        #position above face
        tx = x
        ty = y - filter_height + 20

        if ty < 0:
            ty = 0

        #apply filter
        for i in range(filter_height):
            for j in range(filter_width):

                if filter_rs[i, j][3] > 0:
                    im[ty+i, tx+j] = filter_rs[i, j][:3]

        if prediction[1] < 500:
            cv2.putText(
                im,
                '%s -%.0f' % (names[prediction[0]], prediction[1]),
                (x-10, y-10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 0)
            )

        else:
            cv2.putText(
                im,
                'not recognised',
                (x -10, y-10),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 0)
            )

    cv2.imshow('OpenCV', im)

    key = cv2.waitKey(10)

    if key == 27:
        break

webcam.release()

cv2.destroyAllWindows()