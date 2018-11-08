import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["1", "2", "3", "4", "5", "6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23",
            "24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44",
            "45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65",
            "66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86",
            "87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106",
            "107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124",
            "125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142",
            "143","144","145","146","147","148","149","150","151","152","153","154","155","156","157","158","159","160",
            "161","162","163","164","165","166"]  # 自行车检测


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    # if os.path.exists('E:/food-xml/%' % (image_id)):
        list_file_train = open('D:/8/1/txt/train.txt', 'a+', encoding='utf-8')
        list_file_train.write('F:/darknet-master/darknet-master/build/darknet/x64/data/obj/%s.jpg\n' % (str(image_id)))
        list_file_train.close()


        in_file = open('D:/8/1/xml/%s.xml' % (image_id), encoding='utf-8')
        out_file = open('D:/8/1/txt/%s.txt' % (image_id), 'a', encoding='utf-8')  # 生成txt格式文件
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')




#  list_file_val = open('boat_val.txt', 'w')

path1 = "D:/8/1/xml"
filelist = os.listdir(path1)
for files in filelist:
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    convert_annotation(filename0)
  # 只生成训练集，自己根据自己情况决定

# for image_id in image_ids_val:

#    list_file_val.write('/home/*****/darknet/boat_detect/images/%s.jpg\n'%(image_id))
#    convert_annotation(image_id)
# list_file_val.close()
