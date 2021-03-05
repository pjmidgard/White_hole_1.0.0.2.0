import os
import getpass
USER_NAME = getpass.getuser()


def add_to_startup(file_path="C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.exe"):
    if file_path == "C:\\Users\\Public\\Documents\\White_hole\\White_hole_1.0.0.2.0.exe":
        print("ok")
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
add_to_startup()
import subprocess, json

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId | ConvertTo-Json}\"")
j = json.loads(out)
for dev in j:
    print(dev['Status'], dev['Class'], dev['FriendlyName'], dev['InstanceId'] )
    os.system('F:\\Whitehole\\White_hole_1.0.0.2.0.exe')
    os.system('D:\\Whitehole\\White_hole_1.0.0.2.0.exe')
    os.system('E:\\Whitehole\\White_hole_1.0.0.2.0.exe')
import win32file
for d in ('E'):
    dname='%c:\\' % (d)
    dt=win32file.GetDriveType(dname)
    if dt == win32file.DRIVE_CDROM:
        print('%s is CD ROM' % (dname))
        os.system('E:\\Whitehole\\White_hole_1.0.0.2.0.exe')
