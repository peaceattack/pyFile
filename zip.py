# -*- coding:utf-8 -*-

import zipfile
MyZip = "/root/Downloads/MAC.zip"
MyZipOBJ = zipfile.ZipFile(MyZip)
MyZipOBJ.namelist()

for i in MyZipOBJ.namelist():
    print i
