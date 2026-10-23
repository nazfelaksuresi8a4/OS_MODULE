import os 

file_name = 'test_file'
file_path = os.curdir

joint_file = os.path.join(file_path,file_name)  #dosya yolu ile dosya ismini bir birine / ile bağlar.

os.mkdir(joint_file)    #dizin üzerinde file_name isimli dosya oluşturur 

