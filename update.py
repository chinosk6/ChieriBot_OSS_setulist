# -*- coding: utf-8 -*-
import oss2

def is_write(name):
    namelist=['jpg','png','bmp','jpeg','gif','jiff']
    if name.lower() in namelist:
        return True
    else:
        return False

def readoss(abucket,apath,公网): #我就是喜欢中文变量(逃
    '''
    Bucket名,路径,是否使用公网地址
    '''
    auth = oss2.Auth('AccessKey ID', 'AccessKey Secret')
    bucket = oss2.Bucket(auth, 'http://oss-cn-shanghai.aliyuncs.com', abucket)
    global readurl
    readurl=''
    # 列举apath文件夹下的文件与子文件夹名称，不列举子文件夹下的文件。如果不需要返回owenr信息可以不设置fetch_owner参数。
    for obj in oss2.ObjectIteratorV2(bucket, prefix = apath+'/', delimiter = '/', fetch_owner=False):
        # 通过is_prefix方法判断obj是否为文件夹。
        if obj.is_prefix():  # 判断obj为文件夹。
            print('directory: ' + obj.key)
        else:                # 判断obj为文件。

            if 公网==True:
                geturl='https://'+abucket+ '.oss-cn-shanghai.aliyuncs.com/'+obj.key #公网访问
            else:
                geturl='https://'+abucket+'.oss-cn-shanghai-internal.aliyuncs.com/'+obj.key  #内网访问

            if is_write(geturl[-3:])==True or is_write(geturl[-4:])==True:
                geturl=geturl+'\n'
                readurl=readurl + geturl

            geturl=''
                #readurl=readurl+'\n'+'https://'+abucket+ '.oss-cn-shanghai.aliyuncs.com/'+obj.key #公网访问
            print('file: ' + obj.key)

            #print('file owner display name: ' + obj.owner.display_name)
            #print('file owner id: ' + obj.owner.id)

    print(readurl)
    return readurl[:-1] #去除末尾换行符

aqwq=readoss('MyBucket','imgup/images',True) #false内网 true公网

with open("C:\\Users\\Y7000\\Desktop\\sdk_v2.6.5\\alioss\\test.txt","w",encoding='utf-8') as f:
    f.write(aqwq)

print("操作结束")
