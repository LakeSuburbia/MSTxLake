import os
os.system("git --version")
#os.system("cd '${0%/*}'")
os.system("cd ..")

os.system("git clone https://github.com/LakeSuburbia/MSTxLake.git || (cd MSTxLake ; git pull)")
os.system("cd MSTxLake")
os.system("open MSTxLake.logicx")