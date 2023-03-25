# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo

def parse_file():
    thisfile = open("photo_urls2.json", 'r')
    thishash = json.load(thisfile)
    thatfile = open('allalbumswithurls2.json', 'r')
    thathash = json.load(thatfile)
    theotherfile = open('all_info_file.json', 'r')
    theotherhash = json.load(theotherfile)
    #print(thishash.keys())
    thatlist = []
    for key in thathash.keys():
      thatlist.append(key)
    thatlist.sort(key = lambda x: thathash[x]['title'])
    for entry in thatlist:
      print(thathash[entry]['title'])
    print('**********')
    album_title = thathash[thatlist[0]]['title']
    print(album_title)
    album_entries = thathash[thatlist[0]]['photoset_hash']
    print(album_entries)
    print(album_entries[0].keys())
    caption = album_entries[0]['title']
    print(caption)
    id = album_entries[0]['id']
    print(id)
    url = thishash[id]
    print(url)
    url2 = album_entries[0]['url']
    print(url2)
    # well crap, I thought I had dimensions in one of these hashes, need to figure out that next...
    print('***********************')
    print('FLICKR ORIGINAL INFO')
    print('***********************')
    original_id = theotherhash[id]['id']
    original_caption = theotherhash[id]['title']
    original_url = theotherhash[id]['url_o']
    width = theotherhash[id]['width_o']
    height = theotherhash[id]['height_o']
    print(original_id)
    print(original_url)
    print(original_caption)
    print(width)
    print(height)
    print(theotherhash[id])
    thisphoto = flickr_photo.Photo(id,original_url,original_caption,width,height)
    print(thisphoto.id)
    print(thisphoto.location)
    print(thisphoto.caption)
    print(thisphoto.width)
    print(thisphoto.height)
    print(thisphoto.orientation)
    thisfile.close()
    thatfile.close()
    theotherfile.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
