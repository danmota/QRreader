# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:29:00 2017

@author: Daniel Mota
"""

import win32api
import os
import time

def pdf_to_jpg(pdfPath, pages):
    # print pdf using jpg printer
    # 'pages' is the number of pages in the pdf
    filepath = pdfPath.rsplit('/', 1)[0]
    filename = pdfPath.rsplit('/', 1)[1]

    #print pdf to jpg using jpg printer
    tempprinter = "ImagePrinter Pro"
    printer = '"%s"' % tempprinter
    win32api.ShellExecute(0, "printto", filename, printer,  ".",  0)

    # Add time delay to ensure pdf finishes printing to file first
    fileFound = False
    if pages > 1:
        jpgName = filename.split('.')[0] + '_' + str(pages - 1) + '.jpg'
    else:
        jpgName = filename.split('.')[0] + '.jpg'
    jpgPath = filepath + '/' + jpgName
    waitTime = 30
    for i in range(waitTime):
        if os.path.isfile(jpgPath):
            fileFound = True
            break
        else:
            #pass
            time.sleep(1)

    # print Error if the file was never found
    if not fileFound:
        print "ERROR: " + jpgName + " wasn't found after " + str(waitTime)\
              + " seconds"

    return jpgPath

pdf_to_jpg("C://Users//Daniel Mota//OneDrive//Python//QRreader//Scan_0002.pdf",1)