from distutils.core import setup
import py2exe
import os

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files))
    for (root, dirs, files) in os.walk(os.path.normpath(src))]

data_files = []
data_files += tree('./project/Blastdb')
data_files += tree('./project/BlastResult')
data_files += tree('./project/Categories')
data_files += tree('./project/DbAmbigua')
data_files += tree('./project/FinalResult')
data_files += tree('./project/Test')

setup(
    console=['main.py'],
    skip_archive=True,
    data_files= data_files,
    options = {
        'py2exe': {
            'packages': ['Bio', 'numpy'],
            "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
        }
    }
)

