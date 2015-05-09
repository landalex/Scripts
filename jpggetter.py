# Recursively finds files in the sourcePath adhering to filtertext, and copies them to the
# destPath in the format i.jpg
import sys
import os
import fnmatch
import string
import shutil

sourcePath = sys.argv[1]
destPath = sys.argv[2]

matches = []
filtertext = '*.jpg'
for root, dirnames, filenames in os.walk(sourcePath):
	for filename in fnmatch.filter(filenames, filtertext):
		matches.append(os.path.join(root, filename))
print matches
i = 0
for filename in matches:
	newname = destPath + str(i) + ".jpg"
	i = i + 1
	shutil.copy2(filename, newname)