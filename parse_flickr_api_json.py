# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo

def parse_file():
    thatfile = open('allalbumswithurls2.json', 'r')
    thathash = json.load(thatfile)
    theotherfile = open('all_info_file.json', 'r')
    theotherhash = json.load(theotherfile)
    thatlist = []
    for key in thathash.keys():
      thatlist.append(key)
    thatlist.sort(key = lambda x: thathash[x]['title'])
    album_number = 7
    #this_album = thatlist[album_number]
    # THIS IS HARD-CODED SO WE JUST DO ONE
    for this_album in thatlist:
      album_title = thathash[this_album]['title']
      print('Creating tex file for ' + album_title)
      filename = album_title + '.tex'
      # THIS IS HARD-CODED SO WE JUST DO ONE
      album_entries = thathash[this_album]['photoset_hash']
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
        thisphoto1 = flickr_photo.Photo(id,location,original_caption,width,height)
        photo_list.append(thisphoto1)
      thatfile.close()
      theotherfile.close()

      book_list = []
      current_page = flickr_photo.Page()
      for thisphoto in photo_list:
        if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
          current_page.add_photo(thisphoto)
        elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
          current_page.add_photo(thisphoto)
        else:
          book_list.append(current_page)
          current_page = flickr_photo.Page()
          current_page.add_photo(thisphoto)
      # add final page
      book_list.append(current_page)

      my_file = open(filename, 'w') 
      my_book = flickr_photo.Book(my_file)

      for thispage in book_list:
          layout = thispage.layout
          photo_list = thispage.photo_list
          my_book.add_page(thispage)
      my_book.print_book()
    # that's all folks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
