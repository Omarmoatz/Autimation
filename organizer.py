
import os
import shutil
import pathlib

pathe = 'downlouds'
os.chdir(pathe)

folders=['images','docments','media']

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

for file in os.listdir('.'):
    filename,file_extention = os.path.splitext(file)
    print(filename,'   ',file_extention)

    if file_extention in ['.png','.rar']:
        shutil.move(file,'images')
        print(f'moving file : {file}')

    elif file_extention in ['.docx','.pdf','.txt']:
        shutil.move(file,'docments')
        print(f'moving file : {file}')

    elif file_extention in ['.mp3','.mp4']:
        shutil.move(file,'media')
        print(f'moving file : {file}')  
          


  #  ['.mp3', '.docx', '.pdf', '.mp4', '.rar', '.txt', '.png']























