# -*- coding: utf-8 -*- 
import os, sys 
import time 
import wmi 

def kscale(old):
     old_num=int(old)
     if old_num < 1024:
          new=str(round(int(old),2))+"B"
     elif old_num>=1024 and old_num<1024*1024:
          new=str(round(int(old)/1024,2))+"KB"
     elif old_num>=1024*1024 and old_num<1024*1024*1024:
          new=str(round(int(old)/1024/1024,2))+"MB"
     else:
          new=str(round(int(old)/1024/1024/1024,2))+"GB"
     return new

     
def get_disk_info(): 
     """ 
     获取物理磁盘信息。 
     """
     tmplist = [] 
     c = wmi.WMI () 
     for physical_disk in c.Win32_DiskDrive (): 
         tmpdict = {} 
         tmpdict["Caption"] = physical_disk.Caption 
         tmpdict["Size"] = int(physical_disk.Size)/1024/1024/1024
         tmplist.append(tmpdict) 
     return tmplist 

def get_fs_info() : 
     """ 
     获取文件系统信息。  
     """
     tmplist = []
     num=1
     c = wmi.WMI () 
     for physical_disk in c.Win32_DiskDrive (): 
         for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
             for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
                 tmpdict = {} 
                 tmpdict["Caption"] = logical_disk.Caption 
                 tmpdict["DiskTotal"] = kscale(logical_disk.Size)
                 #tmpdict["UseSpace"] = kscale(str(int(logical_disk.Size)-int(logical_disk.FreeSpace)))
                 tmplist.append(tmpdict)
     print("当前系统中存在的逻辑盘：")
     print("序号\t盘符\t总容量")
     for i in tmplist:
          print(str(num)+"\t"+i['Caption']+"\t"+i['DiskTotal'])
          num+=1

def check(disk):
     disk=disk+":"
     tmplist = []
     c = wmi.WMI () 
     for physical_disk in c.Win32_DiskDrive (): 
         for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
             for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"):
                  tmplist.append(logical_disk.Caption)
     for i in tmplist:
          if i==disk:
               return True
          else:
               continue
     return False

