import os
import shutil
import math
import json

def create_validation(ratio = 0.2):
    cwd = os.getcwd()
    datasetDir = os.path.join(cwd,'Classification_Dataset')
    trainingDir = os.path.join(datasetDir,'training')
    validationDir = os.path.join(datasetDir,'validation')

    if not os.path.exists(validationDir):
        os.makedirs(validationDir)

    print('Creating validation set...')
    for (root, dirs, files) in os.walk(datasetDir):
        if root.endswith('training'):
            for dir in dirs:
                validClassDir = os.path.join(validationDir,dir)
                trainClassDir = os.path.join(trainingDir,dir)
                os.makedirs(validClassDir,exist_ok=True)
                elNumber =len([name for name in os.listdir(trainClassDir) if os.path.isfile(os.path.join(trainClassDir,name))])
                validPart = int(math.floor(elNumber*ratio))
                #print(elNumber, validPart)
                for img in os.listdir(trainClassDir)[:validPart]:
                    #print(img)
                    source = os.path.join(trainClassDir,img)
                    dest = os.path.join(validClassDir,img)
                    shutil.move(source, dest)

    print('Validation set created correctly')


def delete_validation():
    cwd = os.getcwd()
    datasetDir = os.path.join(cwd,'Classification_Dataset')
    trainingDir = os.path.join(datasetDir,'training')
    validationDir = os.path.join(datasetDir,'validation')
    if not os.path.exists(validationDir):
        return
    print('Deleting validation...')
    for (root,dirs,files) in os.walk(datasetDir):
        if root.endswith('validation'):
            for dir in dirs:
                validClassDir = os.path.join(validationDir,dir)
                trainingClassDir = os.path.join(trainingDir,dir)
                for img in os.listdir(validClassDir):
                    #print(img)
                    source = os.path.join(validClassDir,img)
                    dest = os.path.join(trainingClassDir,img)
                    shutil.move(source, dest)
                os.rmdir(validClassDir)
            os.rmdir(validationDir)
    print('Validation set deleted correctly')
