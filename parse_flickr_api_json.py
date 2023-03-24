# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

def print_book():
    thisfile = open("photo_urls2.json", 'r')
    thishash = json.load(thisfile)
    thatfile = open('allalbumswithurls2.json', 'r')
    thathash = json.load(thatfile)
    #print(thishash.keys())
    thatlist = []
    for key in thathash.keys():
      thatlist.append(key)
    for entry in thatlist:
        print(thathash[entry]['title'])
    #print(thatlist)
    thisfile.close()
    thatfile.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_book()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
