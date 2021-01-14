import os

path='./data/labels/train' #path of labels
labels = os.listdir(path)
for x in labels:
    with open(path+'/'+x) as f:
        lines = f.read().splitlines()
        for y in lines:
            if y[:1]!='0':
                print(x)