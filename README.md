# disk_scrub-Windows
A disk data erasure program based on Windows system

## 1、目录结构及说明

### 1、目录结构

```
disk_scrub(Windows)
|_ dll
  |_	Test
  |_ x86
    |_ func1.dll
  |_ x64
    |_ func1.dll
|_ 说明
  |_ pitcure
  |_Readme.md
|_ __pycache__
|_ disk_info.py
|_ func2.py
|_ func3.py
|_ scrub.py
```

### 2、说明

由于本程序在功能一的实现上使用了C语言编写的接口，所以需要调用C语言生动的dll动态链接库，存放在./dll文件夹中。dll文件夹中包含三个文件夹，分别是Test、x86和x64。其中Test是C语言工程文件，负责生成func1.dll动态链接库。剩下两个文件夹中是我已经生成好的dll文件，分别是32位和64位的文件。

**注意：根据您使用的python是32位或64位选择调用哪个动态库！！在源码scrub.py文件中的第9行进行修改！！**

## 2、安装说明

程序基于python3.7进行编写。使用前需要安装python3.7。
程序import了一些外部库，分别是：`numpy、shutil、wmi、pywin32、dialog`等。需要提前进行安装，命令如下：

```
pip install numpy
pip install pytest-shutil
pip install WMI
pip install pywin32
pip install pythondialog
```

**如有其他依赖库没有安装，请自行安装**

## 3、使用说明

程序主函数位于scrub.py文件中，使用该程序先进入程序根文件夹通过命令`python scrub.py`即可启动运行，启动后效果如下：

![运行界面](./picture/1.png ''运行界面'')

共有三种功能：

```
1、物理盘或逻辑盘数据擦除
2、逻辑盘剩余空间数据擦除
3、目录及文件数据擦除
```

输入序号即可选择功能。
第一种功能：

![功能一](./picture/2.png ''功能一'')

第二种功能：

![功能二](./picture/3.png ''功能二'')

第三种功能：

![功能三](./picture/4.png ''功能三'')
