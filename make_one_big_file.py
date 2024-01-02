"""Make one big file out of previously loaded data"""
import json

# this is just a utility script that was created
# to make one big file out of previously downloaded flickr metadata
def make_one_big_file():
  """Make one big file out of previously loaded data"""
  bighash = {}
  filenamelist = []
  for i in range(1,65):
    if i < 10:
      # this won't work out of context due to hard-coded prefix
      filename = "/home/swickape/Pictures/flickr/photos/0" + str(i) + ".txt"
    else:
      # this won't work out of context due to hard-coded prefix
      filename = "/home/swickape/Pictures/flickr/photos/" + str(i) + ".txt"
    filenamelist.append(filename)
  for thisfilename in filenamelist:
    with open(thisfilename, 'r', encoding='utf-8') as myinfile:
#    thisfile = open(thisfilename, 'r')
      thishash = json.load(myinfile)
    photolist = thishash['photos']['photo']
    for photo in photolist:
      thisid = photo['id']
      bighash[thisid] = photo
#    thisfile.close()
  with open('all_info_file.json','w',encoding='utf-8') as myoutfile:
    myoutfile.write(json.dumps(bighash))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  make_one_big_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
