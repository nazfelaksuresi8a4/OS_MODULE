import shutil
import os 

curdir = os.curdir

listdir = os.listdir(curdir)

for file in listdir:
    if os.path.isfile(file):        #hedef dizindeki belirtilen nesnenin bir dosya olup olmadıgını kontrol eder
        print(file + ' Bir dosyadır')

    elif os.path.isdir(file):       #hedef dizindeki belirtilen nesnenin bir klasör olup olmadıgını kontrol eder 
        print(file + ' bir klasördür')

    else:
        print(file + ' Bilinmiyor')
