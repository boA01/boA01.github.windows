from os import error
import PyPDF2
#加密PDF
def encrypt(old_Path, new_Path):
    """
    :param old_Path: 待加密文件的路径名
    :param new_Path: 加密之后的文件路径名
    """
    with open(old_Path, 'rb') as pdfFile: 
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        # 创建pdfWriter对象用于写出PDF文件
        pdfWriter = PyPDF2.PdfFileWriter()
        # pdf对象加入到pdfWriter对象中
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        # 密码设置为8888
        pdfWriter.encrypt('8888')
        with open(new_Path, 'wb') as resultPDF:
            pdfWriter.write(resultPDF)
            print('加密成功!，')
 
def decrypt(old_Path):
    """
    :param old_Path: 待加密文件的路径名
    :param new_Path: 加密之后的文件路径名
    """
    with open(old_Path, 'rb') as pdfFile:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        # 判断文件是否加密
        if pdfReader.isEncrypted:
            # 判断密码是否正确
            for i in range(10000):
                #生成四位数密码
                pwd=str(i).zfill(4).replace(' ','')
                print(pwd)
                try:
                    pdfReader.decrypt(pwd)
                except:
                    print('密码不对,哼~~~')
                else:
                    print('成功了!密码是：'+pwd)
                    break
        else:
            print("没有密码哦~")
if __name__ == '__main__':
    #给pdf加密
    #encrypt('E:/520快乐.pdf','E:/520快乐2.pdf')
    #给pdf解密,我们尝试 4位数的密码
    decrypt('E:/520快乐.pdf')