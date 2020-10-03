import os
import shutil
import cv2
import numpy as np
import urllib.request

def prepare_pos_images():
    if not os.path.exists("pos"):
        os.mkdir("pos")
    else:
        print("Pos Exists. Deleting Directory")
        shutil.rmtree("pos")
        os.mkdir("pos")

    img_num = 0
    for f in os.listdir('training-synthetic'):
        try:
            print(f)
            img = cv2.imread('training-synthetic/'+f,cv2.IMREAD_GRAYSCALE)
            resized_img = cv2.resize(img,(100,100))
            cv2.imwrite("pos/"+str(img_num)+".jpg",resized_img)
            img_num += 1
        except Exception as e:
            print(str(e))

# prepare_pos_images()

def prepare_neg_images():
    if not os.path.exists("neg"):
        os.mkdir("neg")
    # else:
    #     print("Neg Exists. Deleting Directory")
    #     shutil.rmtree("neg")
    #     os.mkdir("neg")

    # neg_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03183080'
    # neg_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03563967'
    # neg_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04576211'
    neg_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n01905661'


    urls = urllib.request.urlopen(neg_link).read().decode()

    img_num = 1520

    for i in urls.split("\n"):
        try:
            print(i)
            dir = '/content/drive/My Drive/:p Sem ki naiya hai Ram ke bharose!!/ES331: Probability and Random Processes/Assignment2_Udit/neg/'
            urllib.request.urlretrieve(i,dir+str(img_num)+".jpg")
            img = cv2.imread(dir+str(img_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            resized_img = cv2.resize(img,(100,100))
            cv2.imwrite(dir+str(img_num)+".jpg",resized_img)
            img_num+=1
        except Exception as e:
            print(str(e))
prepare_neg_images()