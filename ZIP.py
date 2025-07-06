import zipfile
import os

folder = "C:/Users/Katherine/Downloads/Python/Automate/Capital Quizzes"
zip = zipfile.ZipFile('./zipped.zip', 'w')

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.zip'):
            continue
        filepath = os.path.join(foldername, filename)
        arcname = os.path.relpath(filepath, folder)
        zip.write(filepath, arcname)
zip.close()


