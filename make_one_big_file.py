# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

def make_one_big_file():
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
      thisfile = open(thisfilename, 'r')
      thishash = json.load(thisfile)
      photolist = thishash['photos']['photo']
      for photo in photolist:
          id = photo['id']
          bighash[id] = photo
      thisfile.close()
    all_info_file = open('all_info_file.json','w')
    all_info_file.write(json.dumps(bighash))
    all_info_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_one_big_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
