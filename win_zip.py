
 +# -*- coding:utf-8 -*-
 +
 +import zipfile
 +MyZip = "C:\Users\Administrator\Desktop\MAC.zip"
 +MyZipOBJ = zipfile.ZipFile(MyZip)
 +MyZipOBJ.namelist()
 +
 +for i in MyZipOBJ.namelist():
 +    print i
