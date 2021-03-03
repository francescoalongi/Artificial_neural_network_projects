import os
import json


def DatasetSplitJSON():
    cwd = os.getcwd()
    datasetDir = os.path.join(cwd,'Classification_Dataset')
    trainingDir = os.path.join(datasetDir,'training')
    validationDir = os.path.join(datasetDir,'validation')
    data = {}
    for (root,dirs,files) in os.walk(datasetDir):
        if root.endswith('training'):
            dirsContent = {}
            for dir in dirs:
                trainClassDir = os.path.join(trainingDir,dir)
                dirsContent[dir] = [[name for name in os.listdir(trainClassDir) if os.path.isfile(os.path.join(trainClassDir,name))]]
            data['training'] = dirsContent
        
        if root.endswith('validation'):
            dirsContent = {}
            for dir in dirs:
                validClassDir = os.path.join(validationDir,dir)
                dirsContent[dir] = [[name for name in os.listdir(validClassDir) if os.path.isfile(os.path.join(validClassDir,name))]]
            data['validation'] = dirsContent

    with open('dataset_split.json','w') as outfile:
        json.dump(data,outfile,indent=3)    