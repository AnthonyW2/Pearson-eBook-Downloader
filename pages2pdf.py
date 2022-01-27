#!/usr/bin/env python

# Anthony Wilson - Convert a Pearson eBook to a PDF
# 
# Protected by the MIT License
# 
# 2022-1-27

# This script is used to concatenate the pages downloaded by download.py into a single PDF


import sys
from PIL import Image
import os


imgdir = ""

outputname = "Book.pdf"

#Process options from the command line arguments
if len(sys.argv) == 1:
  #Print help information
  print("To use this script, you must supply the path to a directory containing a set of images.")
  
  options = os.listdir(".")
  print("Options in your current working directory:")
  for option in options:
    if "Book_" in option:
      print(option)
  
  exit(1)

if len(sys.argv) >= 2:
  imgdir = sys.argv[1]

if len(sys.argv) >= 3:
  #Set the name of the output file
  outputname = sys.argv[2]
  if ".pdf" not in outputname:
    outputname = outputname+".pdf"


#Get a list of files in the given directory
imgs = os.listdir(imgdir)

#Define a function to return the number in the filename of the image, so that the pages are sorted correctly
def pageSort(name):
  return int(name.replace("page","").replace(".png",""))

#Sort the images by the number in the filename
imgs.sort(key=pageSort)

imagelist = []

#Convert all the images to RGB mode, ready to be saved to a PDF
for img in imgs:
  if ".png" in img:
    
    image = Image.open(imgdir+"/"+img).convert("RGB")
    imagelist.append(image)


image0 = imagelist.pop(0)

#Save the images into a PDF
image0.save(outputname, save_all=True, append_images=imagelist)




