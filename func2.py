import numpy as np
import pickle
import time
import os
import os.path
import shutil

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    os.rmdir(filepath)

def func2(symbol):
    if len(symbol)!= 1:
        print('input invalid, 1 letter allowed')
        return

    path = '%s:\\diskwippercache\\'%symbol
    if not(os.path.exists(path)):
        os.mkdir(path)    
    T = time.time()

    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '1G %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (16384,16384)), f)
            t2 = time.time()
            print('1G %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('1G files filled')


    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '256M %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (8192,8192)), f)
            t2 = time.time()
            print('256M %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('256M files filled')
        

    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '64M %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (4096,4096)), f)
            t2 = time.time()
            print('64M %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('64M files filled')


    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '16M %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (2048,2048)), f)
            t2 = time.time()
            print('16M %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('64M files filled')


    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '1M %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (512,512)), f)
            t2 = time.time()
            print('1M %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('1M files filled')



    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '256K %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (256,256)), f)
            t2 = time.time()
            print('256K %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('256K files filled')


    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '1K %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (16,16)), f)
            t2 = time.time()
            print('1K %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('1K files filled')

    try:
        i = 0
        while 1:
            t1 = time.time()
            with open(path + '1bit %d.wipercache'%i,'wb') as f:
                pickle.dump(np.random.binomial(1,0.5,size = (1,1)), f)
            t2 = time.time()
            print('1bit %d.wipercache %fs'%(i, (t2-t1)))
            i+=1
    except:
        print('1bit files filled')

    print('progress completed, used time %f'%(time.time()-T))
    del_file(path)
    

