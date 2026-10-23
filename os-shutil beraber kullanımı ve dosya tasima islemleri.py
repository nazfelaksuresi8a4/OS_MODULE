import shutil
import os 

file_name = 'test_file'
lower_file_name = 'lower_test_file'
file_path = os.curdir

joint_file = os.path.join(file_path,file_name)  #dosya yolu ile dosya ismini bir birine / ile bağlar.
lower_file = os.path.join(joint_file,lower_file_name)

if not os.path.exists(joint_file):      #belirtilen yol üzerinde aynı dosyadan bir tane daha yoksa oluştur
    os.mkdir(joint_file)    #dosya oluştur

if not os.path.exists(lower_file):
    os.mkdir(lower_file)    #oluşturulan dosya içinde başka bir dosya oluştur 


ornek_belge_1 = os.path.abspath('belge_ismi_1.txt') #belirtilen isimdeki dosyanın mutlak yolunu bulur
ornek_belge_2 = os.path.abspath('belge_ismi_2.txt')

shutil.move(ornek_belge_1,joint_file)   #belirtilen yoldaki bir dosyayı başka bir klasör içine taşımak için kullanılır 
shutil.move(ornek_belge_2,lower_file)

