import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
        base = "Win32GUI"

exectables = [cx_Freeze.Executable("trial.py", base=base)]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"Packages":["tkinter","matplotlib"]}},
    version = "0.01",
    description = "Sea of BTC trading application",
    executables = executables
    )
