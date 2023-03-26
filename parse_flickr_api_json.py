# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo

def parse_file():
    album_number = 7
    thatfile = open('allalbumswithurls2.json', 'r')
    thathash = json.load(thatfile)
    theotherfile = open('all_info_file.json', 'r')
    theotherhash = json.load(theotherfile)
    thatlist = []
    for key in thathash.keys():
      thatlist.append(key)
    thatlist.sort(key = lambda x: thathash[x]['title'])
    album_title = thathash[thatlist[album_number]]['title']
    # THIS IS HARD-CODED SO WE JUST DO ONE
    album_entries = thathash[thatlist[album_number]]['photoset_hash']
    photo_list = []
    for thisphoto in album_entries:
      caption = thisphoto['title']
      id = thisphoto['id']
      url2 = album_entries[0]['url']
      # well crap, I thought I had dimensions in one of these hashes, need to figure out that next...
      original_id = theotherhash[id]['id']
      original_caption = theotherhash[id]['title']
      original_url = theotherhash[id]['url_o']
      width = theotherhash[id]['width_o']
      height = theotherhash[id]['height_o']
      # cross fingers here
      location = '/home/swickape/Pictures/flickr/Downloads/' + album_title + '/' + id + '.jpg'
      #thisphoto1 = flickr_photo.Photo(id,original_url,original_caption,width,height)
      thisphoto1 = flickr_photo.Photo(id,location,original_caption,width,height)
      photo_list.append(thisphoto1)
      #print(thisphoto1.orientation)
      print(thisphoto1.id)
    thatfile.close()
    theotherfile.close()

    print("****************")
    book_list = []
    current_page = flickr_photo.Page()
    for thisphoto in photo_list:
      if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
        current_page.add_photo(thisphoto)
        print("adding landscape photo")
        print(thisphoto.id)
      elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
        current_page.add_photo(thisphoto)
        print("adding portrait photo")
        print(thisphoto.id)
      else:
        book_list.append(current_page)
        current_page = flickr_photo.Page()
        current_page.add_photo(thisphoto)
        print("about to add something bad probably!!!")
        print(thisphoto.id)
    # add final page
    book_list.append(current_page)

    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    my_file = open("splayout2.tex", 'w') 
    my_book = flickr_photo.Book(my_file)

    for thispage in book_list:
        layout = thispage.layout
        photo_list = thispage.photo_list
        for thisphoto in photo_list:
          print(thisphoto.id)
        my_book.add_page(thispage)
    my_book.print_book()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
