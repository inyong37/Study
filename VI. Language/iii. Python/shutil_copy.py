# Author      : Inyong Hwang (inyong1020@gmail.com).
# Date        : 2020-05-04-Mon.
# Description : Test copy
# State       : Progress
# Environment : Python 3.6.8, PyCharm 2018.1 (Professional), Windows Home 10.0.18362.720.
# Input       : PNGNeedList.bin
# Output      : Directory.
# Reference 1 : https://ponyozzang.tistory.com/439
# Reference 2 : https://wikidocs.net/3744
# Reference 3 : https://hyeshinoh.github.io/2018/10/12/python_09_OS%20&%20shutil/

# ./test_dir/src/1/a.png                         -> X
# ./test_dir/src/1/b.txt                         -> ./test_dir/out/1/b.txt
# ./test_dir/src/2/rib_rows_below_normal_16.png  -> ./test_dir/out/2/rib_rows_below_normal_16.png
# ./test_dir/src/3/4/d.png                       -> X

from pickle import load
import os
import shutil

fl = open('PNGNeedList.bin', 'rb')
need_list = load(fl)
fl.close()

src_dir = ''
dst_dir = ''
argv = ['0', 'test_dir\\src', 'test_dir\\out']
for idx, arg in enumerate(argv):
    if idx == 1:
        src_dir = arg
    elif idx == 2:
        dst_dir = arg


def check_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        print(path, ': The directory has been created.')
    else:
        print(path, ': The directory already exists.')


print('{0:-^40}'.format(' Copy Test '))
check_dir(dst_dir)

for root, dirs, files in os.walk(src_dir):
    for file in files:
        dst_path = root.replace('src', 'out')
        if file.endswith('.png'):
            if file in need_list:
                check_dir(dst_path)
                shutil.copy2(os.path.join(root, file), os.path.join(dst_path, file))
            else:
                pass
        else:
            check_dir(dst_path)
            shutil.copy2(os.path.join(root, file), os.path.join(dst_path, file))
