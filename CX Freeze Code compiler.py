import os
import sys

if len(sys.argv)>1:
    None
else:
    FIle=input("which script do you want to compile:")
    os.system("C:/Python34/Scripts/cx_Freeze "+File)
    print("Finish")
