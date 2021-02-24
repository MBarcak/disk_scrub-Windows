import os
from ctypes import *

import func2 as f2
import func3 as f3
import disk_info

def func1():
    lib = CDLL("./dll/x64/func1.dll")
    print("警告:谨慎选择当前系统盘(如C盘)，否则会导致系统崩溃!")
    disk=input("输入要擦除的磁盘盘符(如输入F):")
    ok=disk_info.check(disk)  #检查输入的盘符是否存在
    if ok is False:
        print("您输入的盘符不存在,返回!")
        return
    c=input("确认要擦除"+disk+"盘上的数据吗[Y/N]?:")
    if c=='n' or c=='N':
        return
    elif c=='Y' or c=='y':
        lib.func1(disk)
    return

def func2():
    disk=input("输入要擦除的逻辑盘盘符(如输入F):")
    ok=disk_info.check(disk)  #检查输入的盘符是否存在
    if ok is False:
        print("您输入的盘符不存在,返回!")
        return
    c=input("确认要擦除"+disk+"盘的剩余空间数据吗[Y/N]?:")
    if c=='n' or c=='N':
        return
    elif c=='Y' or c=='y':
        f2.func2(disk)
        return
    else:
        print("输入错误,取消!")
        return

def func3_dir(rootDir):
    num=0
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        fpath,fname=os.path.split(path)  #分割文件名和目录名
        #print(path)
        if os.path.isdir(path): 
            func3_run(path)
        if os.path.isfile(path):
            f3.func3(path)
            newFilename=fpath+"\disk_scrub"+str(num)
            os.rename(path,newFilename)
            os.remove(newFilename)
            #print(num)
            num+=1
    os.rmdir(rootDir)
    return

def func3_file(rootFile):
    fpath,fname=os.path.split(rootFile)  #分割文件名和目录名
    f3.func3(rootFile)
    newFilename=fpath+"\disk_scrub.0"
    os.rename(rootFile,newFilename)
    os.remove(newFilename)
    return
    
def func3():
    root=input("输入要擦除的文件或目录:")
    if os.path.exists(root) is False:
        print("文件或目录不存在!")
        return
    else:
        c=input("确认要擦除“"+root+"”目录或文件的数据吗[Y/N]?:")
        if c=='n' or c=='N':
            return
        elif c=='Y' or c=='y':
            if os.path.isdir(root):  #目录
                func3_dir(root)
            else:                    #文件
                func3_file(root)
            return
        else:
            print("输入错误,取消!")
            return

def main():
    while(True):
        print("======磁盘擦除工具======")
        print("==========目录==========")
        print("1、物理盘或逻辑盘数据擦除")
        print("2、逻辑盘剩余空间数据擦除")
        print("3、目录及文件数据擦除")
        print("0、退出")
        choose_num=int(input("输入序号:"))

        if choose_num==1:
            disk_info.get_fs_info()
            func1()
        elif choose_num==2:
            disk_info.get_fs_info()
            func2()
        elif choose_num==3:
            func3()
        elif choose_num==0:
            exit(0)
        else:
            print("输入错误!")

if __name__=="__main__":
    main()
