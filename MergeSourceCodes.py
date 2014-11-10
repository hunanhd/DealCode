# coding=utf-8

import os

# Ҫ������·��
#dir = "C:\\Users\\anheihb03dlj\\Desktop\\ARX_MVSS"
source_code_dir = ".\TIDS"
# ����
#���´���Ҳ�ǵ�Ч��
#source_code_dir = "ARX_MVSS"

# ����ļ�·��
#outFilePath = "C:\\Users\\anheihb03dlj\\Desktop\\�����ɡ��ϲ�Դ����.txt"
outFilePath = "�����ɡ��ϲ�Դ����.txt"

# �Ƿ�ʹ���к�
useLineCount = True 

# �Ƿ������Դ�ļ�
outputRC = False

# �Ƿ�ȥ���հ���
stripBlankLine = True 

# �Ƿ�ȥ��ע��
# �Ƚ��鷳����Ҫ�жϵ���ע��(//)�Ͷ���ע��(/* */)
#stripComment = False

def WriteSourceFile(outFile, filePath):
    # ��¼����
    lineCount = 0

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


def WalkFilesInChildDir(outFile, child_dir, ext):
    for root, dirs, files in os.walk(child_dir):
        for f in files:
            file_ext = os.path.splitext(f)[1][1:]
            # ��չ����׺�Ƚϣ������ִ�Сд
            if cmp(file_ext.upper(),ext.upper()) == 0:
                outFile.write("\n==> " + os.path.split(child_dir)[1] + "/" + f +"\n")
                # д���ļ�
                WriteSourceFile(outFile, os.path.join(root, f))
        outFile.write("\n")

def WalkFiles(outFile, dir):
    for root, dirs, files in os.walk(dir):
        print "��Ŀ¼:", root
        if cmp(root.upper(), dir.upper()) == 0: continue

        outFile.write("Ŀ¼["+ os.path.split(root)[1]+"]�µ�����Դ����\n")
        # д��ͷ�ļ�
        WalkFilesInChildDir(outFile, root, "h")
        # д��Դ�ļ�
        WalkFilesInChildDir(outFile, root, "c")
        WalkFilesInChildDir(outFile, root, "cpp")
        if outputRC:
            # д����Դ�ļ�
            WalkFilesInChildDir(outFile, root, "rc")
            WalkFilesInChildDir(outFile, root, "rc2")

# �ļ��������
outFile = open(outFilePath, 'w')
WalkFiles(outFile, source_code_dir)
outFile.close()
