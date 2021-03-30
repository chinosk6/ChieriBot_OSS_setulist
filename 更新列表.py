import alioss

aqwq=alioss.readoss('myname','img/path1',False) #false内网 true公网

aqwq=aqwq + "\n" + alioss.readoss('myname','img/path2',False)

aqwq=aqwq + "\n" + alioss.readoss('myname','img/path3',False)

aqwq=aqwq + "\n" + alioss.readoss('myname','img/path4',False)


with open("C:\\Users\\Y7000\\Desktop\\sdk_v2.6.5\\alioss\\urls.txt","w",encoding='utf-8') as f:
    f.write(aqwq)

print("共更新 "+str(alioss.get_tnm()) +"张图片")


