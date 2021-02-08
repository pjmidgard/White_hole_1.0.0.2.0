_author__ = 'Made by Jurijus Pacalovas'
print(_author__)
import os
import shutil
os.system('White_hole_1.0.0.2.0.reg')
newpath = r'C:\Users\Public\Documents\White_hole' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
shutil.copyfile('White_hole_1.0.0.2.0.ico', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.ico')
shutil.copyfile('White_hole_1.0.0.2.0.exe', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.exe')
shutil.copyfile('White_hole_Start_1.0.0.2.0.exe', 'C:\\Users\\Public\\Documents\\White_hole\\White_hole_Start_1.0.0.2.0.exe')
os.system('White_hole_Start_1.0.0.2.0.exe')
