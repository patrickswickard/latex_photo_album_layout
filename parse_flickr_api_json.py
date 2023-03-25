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
    #print('**********')
    album_title = thathash[thatlist[0]]['title']
    #print(album_title)
    # THIS IS HARD-CODED SO WE JUST DO ONE
    album_entries = thathash[thatlist[0]]['photoset_hash']
    #print(album_entries)
    photo_list = []
    for thisphoto in album_entries:
      #print(album_entries[0].keys())
      caption = album_entries[0]['title']
      #print(caption)
      #id = album_entries[0]['id']
      id = thisphoto['id']
      #print(id)
      url = thishash[id]
      #print(url)
      url2 = album_entries[0]['url']
      #print(url2)
      # well crap, I thought I had dimensions in one of these hashes, need to figure out that next...
      #print('***********************')
      #print('FLICKR ORIGINAL INFO')
      #print('***********************')
      original_id = theotherhash[id]['id']
      original_caption = theotherhash[id]['title']
      original_url = theotherhash[id]['url_o']
      width = theotherhash[id]['width_o']
      height = theotherhash[id]['height_o']
      #print(original_id)
      #print(original_url)
      #print(original_caption)
      #print(width)
      #print(height)
      #print(theotherhash[id])
      #thisphoto1 = flickr_photo.Photo(id,original_url,original_caption,width,height)
      thisphoto1 = flickr_photo.Photo(id,original_url,original_caption,width,height)
      photo_list.append(thisphoto1)
      #print(thisphoto1.id)
      #print(thisphoto1.location)
      #print(thisphoto1.caption)
      #print(thisphoto1.width)
      #print(thisphoto1.height)
      print(thisphoto1.orientation)
    thisfile.close()
    thatfile.close()
    theotherfile.close()

    print("****************")
    book_list = []
    current_page = flickr_photo.Page()
    for thisphoto in photo_list:
      if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
        current_page.add_photo(thisphoto)
        print(current_page.layout)
        print(current_page.canfit_l())
      elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
        current_page.add_photo(thisphoto)
        print(current_page.layout)
        print(current_page.canfit_p())
      else:
        book_list.append(current_page)
        current_page = flickr_photo.Page()
        current_page.add_photo(thisphoto)
      # add final page
      book_list.append(current_page)

    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    onepage = book_list[0]
    for thisphoto in onepage.photo_list:
      x = 1
      #print(thisphoto.orientation)
    for thispage in book_list:
        print(thispage.layout)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
