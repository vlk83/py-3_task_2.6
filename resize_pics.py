import glob
import os.path
import subprocess

if not os.path.exists('Result'):
    os.mkdir('Result')


## 1
## самый простой способ, но не нашел как сохранить исходные имена файлов:
## subprocess.Popen('convert Source/* -resize 200 Result/output.jpg')


## 2
files = glob.glob('Source/*')
for file in files:
    resized_file = file.replace('Source\\', 'Result\\').replace('.', '_resized_200px.')
    subprocess.Popen(['convert', file, '-resize', '200', resized_file])







