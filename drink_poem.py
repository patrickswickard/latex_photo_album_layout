"""Grabs poems and images from cannibal corpse limericks project and does some parsing"""
import re
import os
from mypoem import Poem

BASEDIR = '/home/swickape/projects/cancorp/'
BASEDIR_IMAGE = '/home/swickape/projects/github/patrickswickard.github.io/images/cancorps/img2/'
WEBDIR_IMAGE = '../images/cancorps/img2/'
dirlist1 = os.listdir(BASEDIR)
dirlist2 = os.listdir(BASEDIR_IMAGE)
dirlist1.sort()
dirlist2.sort()
print(dirlist2)
image_hash = {}
poem_list = []
for thisfilename in dirlist2:
  filename = re.search(r"(\d+)(_.*?\.\w+)",thisfilename)
  if filename:
    filenum = filename.group(1)
    filerest = filename.group(2)
    filename_string = WEBDIR_IMAGE + filenum + filerest
    print(filenum)
    image_hash[filenum] = filename_string
for thisfilename in dirlist1:
  filename = re.search(r"(\d+)(_.*?)(\.txt)",thisfilename)
  if filename:
    #print(filename)
    filenum = filename.group(1)
    filerest1 = filename.group(2)
    filerest2 = filename.group(3)
    filename_string = filenum + filerest1 + filerest2
#    print(filename_string)
    with open(BASEDIR + filename_string,'r',encoding='utf-8') as fd:
      lines = fd.read().splitlines()
      poem_title = lines[0]
      print(poem_title)
      print('HOWDY')
      #print(poem_title)
      thisbody = []
      for thisline in lines[2:]:
        if thisline:
          thisbody.append(thisline)
      this_image = image_hash[filenum]
      this_poem = Poem()
      this_poem.title = poem_title
      this_poem.body = thisbody
      this_poem.image = this_image
      this_webfilename_part = filenum + filerest1 + '.html'
      this_webfilename_full = ('/home/swickape/projects/github/patrickswickard.github.io/cancorps/'
                               + this_webfilename_part)
      print(this_webfilename_full)
      this_poem.webfilename_full = this_webfilename_full
      this_poem.webfilename_part = this_webfilename_part
      #f = open(this_poem.webfilename_full,"w")
      #f.write(this_poem.return_web())
      with open(this_poem.webfilename_full,'w',encoding='utf-8') as myoutfile:
        myoutfile.write(this_poem.return_web())
      poem_list.append(this_poem)

for this_poem in poem_list:
  line = ('<LI><a href="cancorps/'
          + this_poem.webfilename_part
          + '">' + this_poem.title + '</a></LI>')
  print(line)
