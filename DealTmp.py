#-*- coding:utf-8 -*- 
import sys
import os
delete_dir_num=0 #记录删除的目录数
delete_file_num=0 #记录删除的文件夹数
def check_dir(cur_dir,level):
 global delete_dir_num
 global delete_file_num
 #获取文件列表
 subdir_list = os.listdir(cur_dir)
 for sub_dir in subdir_list:
  #拼接路径+文件
  full_sub_dir = os.path.join(cur_dir,sub_dir)
  if os.path.isdir(full_sub_dir):   #文件夹处理
   check_dir(full_sub_dir,level+1)
  else:         #文件处理
   file_size = os.path.getsize(full_sub_dir)
   #若文件为空
   if file_size==0:
    os.remove(full_sub_dir)
    delete_file_num = delete_file_num+1
    print("delete file:"+full_sub_dir)
 try:
  #尝试删除目录，该函数的特点是若文件夹不为空会报错
  os.rmdir(cur_dir)
  delete_dir_num = delete_dir_num+1
  print("delete dir:"+cur_dir)
 except:
  pass
  
#print("please input the directory(default is current directory):")
#curDir=input()
#获取当前目录
#if curDir.strip()=='':
curDir = os.getcwd()
check_dir(curDir,0)
print("total delete file:" + str(delete_file_num))
print("total delete directory:" + str(delete_dir_num))