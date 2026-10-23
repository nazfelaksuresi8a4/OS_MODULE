import shutil
import os 

current_directory = os.curdir       #mevcut dizini verir
    
directory_file_list = os.listdir(current_directory) #belirtilen dizindeki tüm dosyaları / klasörleri sıralar

print(directory_file_list)      #yazıdr
