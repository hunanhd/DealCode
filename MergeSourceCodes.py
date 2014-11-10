# coding=utf-8

import os

# 要搜索的路径
#dir = "C:\\Users\\anheihb03dlj\\Desktop\\ARX_MVSS"
source_code_dir = ".\TIDS"
# 或者
#如下代码也是等效的
#source_code_dir = "ARX_MVSS"

# 输出文件路径
#outFilePath = "C:\\Users\\anheihb03dlj\\Desktop\\【生成】合并源代码.txt"
outFilePath = "【生成】合并源代码.txt"

# 是否使用行号
useLineCount = True 

# 是否输出资源文件
outputRC = False

# 是否去掉空白行
stripBlankLine = True 

# 是否去掉注释
# 比较麻烦，需要判断单行注释(//)和多行注释(/* */)
#stripComment = False

def WriteSourceFile(outFile, filePath):
    # 记录行数
    lineCount = 0

    # 读取文件 
    inFile = open(filePath, 'r')

    # 按行循环读取文件
    for line in inFile:
        # 去掉空白行
        # 判断如果是空行，则不写入到文件中 
        if stripBlankLine:
            data = line.strip().split()
            if len(data)==0: continue

        # 如果使用行号，则添加行号，例如 "1.  " 
        if useLineCount:
            lineCount += 1
            lcStr = '%d' %lineCount
            outFile.write(lcStr + ".  " + line)
        else:
            outFile.write(line)
    # 关闭文件
    inFile.close()


def WalkFilesInChildDir(outFile, child_dir, ext):
    for root, dirs, files in os.walk(child_dir):
        for f in files:
            file_ext = os.path.splitext(f)[1][1:]
            # 扩展名后缀比较，不区分大小写
            if cmp(file_ext.upper(),ext.upper()) == 0:
                outFile.write("\n==> " + os.path.split(child_dir)[1] + "/" + f +"\n")
                # 写入文件
                WriteSourceFile(outFile, os.path.join(root, f))
        outFile.write("\n")

def WalkFiles(outFile, dir):
    for root, dirs, files in os.walk(dir):
        print "根目录:", root
        if cmp(root.upper(), dir.upper()) == 0: continue

        outFile.write("目录["+ os.path.split(root)[1]+"]下的所有源代码\n")
        # 写入头文件
        WalkFilesInChildDir(outFile, root, "h")
        # 写入源文件
        WalkFilesInChildDir(outFile, root, "c")
        WalkFilesInChildDir(outFile, root, "cpp")
        if outputRC:
            # 写入资源文件
            WalkFilesInChildDir(outFile, root, "rc")
            WalkFilesInChildDir(outFile, root, "rc2")

# 文件输出对象
outFile = open(outFilePath, 'w')
WalkFiles(outFile, source_code_dir)
outFile.close()
