import sys
import os
import glob
import string
from datetime import date

sourcePath = sys.argv[1]
destPath = sys.argv[2]

fileList = glob.glob(sourcePath + "*.md")

today = date.today()

for file in fileList:
	with open(file, 'r') as oldFile:
		fileData = oldFile.read()
		filePath = os.path.basename(file)
		fileName = filePath[:filePath.rfind(".")]
		fileName.replace(" ", "-")

		newPath = destPath + str(today.year) + "-" + str(today.month)\
		 + "-" + str(today.day) + "-" + filePath

		with open(newPath, 'wb') as newFile:
			frontMatter = "---\ntitle: " + fileName + "\n---\n"
			newFile.write(frontMatter)
			newFile.write(fileData)
	
			print "filePath = " + filePath
			print "fileName = " + fileName
			print "newPath = " + newPath
			print "frontMatter = " + frontMatter	
