# coding=utf-8

import os

# 要搜索的路径
#dir = "C:\\Users\\anheihb03dlj\\Desktop\\ARX_MVSS"
dir = "GDES"

# 输出文件路径
#outFilePath = "C:\\Users\\anheihb03dlj\\Desktop\\目录结构.txt"
outFilePath = "【生成】目录结构.txt"

# 文件输出对象
outFile = open(outFilePath, 'w')

# 记录行号
lineCount = 0

# 是否使用行号
useLineCount = True 

# 是否输出资源文件
outputRC = False

# 是否去掉空白行
stripBlankLine = True 

# 是否去掉注释
# 比较麻烦，需要判断单行注释(//)和多行注释(/* */)
#stripComment = False

def WriteSourceFile(filePath):
    # 使用全局变量
    global lineCount

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

def IsSpecialFolder(folderName):
    if cmp('Win32',folderName) == 0 or\
    cmp('X64',folderName) == 0 or\
    cmp('Debug',folderName) == 0 or\
    cmp('Release',folderName) == 0 or\
    cmp('win32',folderName) == 0 or\
    cmp('x64',folderName) == 0 or\
    cmp('debug',folderName) == 0 or\
    cmp('release',folderName) == 0:
        return True
    return False

def WalkFilesInChildDir(child_dir, ext):
    for root, dirs, files in os.walk(child_dir):
        for f in files:
            file_ext = os.path.splitext(f)[1][1:]
            # 扩展名后缀比较，不区分大小写
            if cmp(file_ext.upper(),ext.upper()) == 0:
                outFile.write("    |-- " + f +"\n")

for root, dirs, files in os.walk(dir):
    print "根目录:", root
    if cmp(root.upper(), dir.upper()) == 0: continue

    folderName = os.path.split(root)[1]
    if IsSpecialFolder(folderName): continue
    outFile.write(folderName+"\n")
    # 写入头文件
    outFile.write("  头文件\n")
    WalkFilesInChildDir(root, "h")
    # 写入源文件
    outFile.write("  源文件\n")
    WalkFilesInChildDir(root, "c")
    WalkFilesInChildDir(root, "cpp")
    if outputRC:
        # 写入资源文件
        outFile.write("  资源文件\n")
        WalkFilesInChildDir(root, "rc")
        WalkFilesInChildDir(root, "rc2")

outFile.close();
