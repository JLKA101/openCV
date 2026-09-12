#facial recognition

import cv2, sys, numpy, os

size = 4 #scaling factor for detection
haar_file = 'haarcascade_frontalface_default.xml' #detect faces
datasets = 'datasets' #where faces will be stored

print('Recognising Face. Please be in sufficent lighting.')

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

(images, labels) = [numpy.array(lis) for ]