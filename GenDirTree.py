# coding=utf-8

import os

# Ҫ������·��
#dir = "C:\\Users\\anheihb03dlj\\Desktop\\ARX_MVSS"
dir = "TIDS"

# ����ļ�·��
#outFilePath = "C:\\Users\\anheihb03dlj\\Desktop\\Ŀ¼�ṹ.txt"
outFilePath = "�����ɡ�Ŀ¼�ṹ.txt"

# �ļ��������
outFile = open(outFilePath, 'w')

# ��¼�к�
lineCount = 0

# �Ƿ�ʹ���к�
useLineCount = True 

# �Ƿ������Դ�ļ�
outputRC = False

# �Ƿ�ȥ���հ���
stripBlankLine = True 

# �Ƿ�ȥ��ע��
# �Ƚ��鷳����Ҫ�жϵ���ע��(//)�Ͷ���ע��(/* */)
#stripComment = False

def WriteSourceFile(filePath):
    # ʹ��ȫ�ֱ���
    global lineCount

    # ��ȡ�ļ� 
    inFile = open(filePath, 'r')

    # ����ѭ����ȡ�ļ�
    for line in inFile:
        # ȥ���հ���
        # �ж�����ǿ��У���д�뵽�ļ��� 
        if stripBlankLine:
            data = line.strip().split()
            if len(data)==0: continue

        # ���ʹ���кţ�������кţ����� "1.  " 
        if useLineCount:
            lineCount += 1
            lcStr = '%d' %lineCount
            outFile.write(lcStr + ".  " + line)
        else:
            outFile.write(line)
    # �ر��ļ�
    inFile.close()

def WalkFilesInChildDir(child_dir, ext):
    for root, dirs, files in os.walk(child_dir):
        for f in files:
            file_ext = os.path.splitext(f)[1][1:]
            # ��չ����׺�Ƚϣ������ִ�Сд
            if cmp(file_ext.upper(),ext.upper()) == 0:
                outFile.write("    |-- " + f +"\n")

for root, dirs, files in os.walk(dir):
    print "��Ŀ¼:", root
    if cmp(root.upper(), dir.upper()) == 0: continue

    outFile.write(os.path.split(root)[1]+"\n")
    # д��ͷ�ļ�
    outFile.write("  ͷ�ļ�\n")
    WalkFilesInChildDir(root, "h")
    # д��Դ�ļ�
    outFile.write("  Դ�ļ�\n")
    WalkFilesInChildDir(root, "c")
    WalkFilesInChildDir(root, "cpp")
    if outputRC:
        # д����Դ�ļ�
        outFile.write("  ��Դ�ļ�\n")
        WalkFilesInChildDir(root, "rc")
        WalkFilesInChildDir(root, "rc2")

outFile.close();
