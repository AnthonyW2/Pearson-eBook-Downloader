#!/usr/bin/env python

# Anthony Wilson - Convert a Pearson eBook to a PDF
# 
# Protected by the MIT License
# 
# 2022-1-27

# This script is used to download the pages of a Pearson eBook as images

# URL example:
# https://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/page0


import sys
import requests
import os


url = ""

#First page to download
START = 0
#Last page to download (set this to a high number to download pages until the end of the book is reached)
END = 5


#Process options from the command line arguments
if len(sys.argv) == 1:
  #Print help information
  print("To use this script, you must supply a valid page URL on the command line.\nFor instructions on how to use this script, see README.md in the Git repo:\nhttps://github.com/AnthonyW2/Pearson-eBook-Downloader")
  
  exit(1)

if len(sys.argv) >= 2:
  url = sys.argv[1]

if len(sys.argv) >= 3:
  START = int(sys.argv[2])

if len(sys.argv) >= 4:
  END = int(sys.argv[3])

if START > END:
  print("ERROR: Starting page is after ending page. Make sure you enter the start and end page numbers in the right order.")
  exit(1)


#Clean up the end of the URL
if "/pages" in url:
  url = url[0:url.find("/pages")] + "/pages/page"
else:
  print("ERROR: Invalid URL provided.")
  print("The URL should be formatted as:\nhttps://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/")
  exit(1)

#Check the URL to make sure it is valid
if "https://" not in url:
  print("ERROR: Invalid URL provided.\nMissing 'https://'")
  print("The URL should be formatted as:\nhttps://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/")
  exit(1)


#Store the name of the directory to save the pages to
dirname = "Book_" + url.split("/")[7]

#Check for the existence of the book directory, and create it if it is not present
if not os.path.isdir(dirname):
  os.mkdir(dirname)
  print("Created book directory")

print("Saving pages to "+os.getcwd()+"/"+dirname+"/\n")


inBounds = True
page = START

print("Starting download")

while inBounds and page <= END:
  
  #Try to download the page
  response = requests.get(url+str(page));
  
  if response.status_code == 200:
    
    #Write the page to a file
    open(dirname+"/page"+str(page)+".png", "wb").write(response.content)
    
    #Overwrite the previously printed line with a "Downloaded page x" message
    print("\033[FDownloaded page "+str(page))
    
  elif response.status_code == 403 or response.status_code == 404:
    
    if page == START:
      print("First page was not found. Is the URL correct?")
      print("The URL should be formatted as:\nhttps://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/")
      exit(1)
      
    else:
      print("Reached the end of the book")
      inBounds = False
    
  else:
    
    print("Connection error "+str(response.status_code)+". Check your connection and the supplied URL, and try again later.")
    print("The URL should be formatted as:\nhttps://______________.cloudfront.net/resources/products/epubs/generated/________-____-____-____-____________/foxit-assets/pages/")
    exit(1)
  
  
  page += 1


print("Your book has finished downloading")




