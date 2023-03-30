# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo
import qrcode
import re

def parse_file():
    album_file = open('allalbumswithurls2.json', 'r')
    album_hash = json.load(album_file)
    all_info_file = open('all_info_file.json', 'r')
    all_info_hash = json.load(all_info_file)
    album_list = []
    for key in album_hash.keys():
      album_list.append(key)
    album_list.sort(key = lambda x: album_hash[x]['title'])
    all_section_list = []
    for this_album in album_list:
      album_id = this_album
      album_url = 'https://www.flickr.com/photos/99753978@N03/albums/' + album_id
      album_title = album_hash[this_album]['title']
      print('Creating tex file for ' + album_title)
      output_filename = 'texfiles/' + album_title + '.tex'
      album_entries = album_hash[this_album]['photoset_hash']
      photo_list = []
      for thisphoto in album_entries:
        caption = thisphoto['title']
        id = thisphoto['id']
        url = thisphoto['url']
        # is it really the case that the width and height are all we grab from all_info_hash?
        width = all_info_hash[id]['width_o']
        height = all_info_hash[id]['height_o']
        # this prefix is unique to environment, currently using pre-downloaded files
        prefix = '/home/swickape/Pictures/flickr/Downloads/' + album_title + '/'
        photo_filename = id + '.jpg'
        location = prefix + photo_filename
        thisphoto = flickr_photo.Photo(id,url,location,caption,width,height)
        # bonus info
        thisphoto.album_title = album_title
        thisphoto.album_url = album_url
        photo_list.append(thisphoto)
      album_file.close()
      all_info_file.close()

      page_list = []
      current_page = flickr_photo.Page()
      for thisphoto in photo_list:
        if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
          current_page.add_photo(thisphoto)
        elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
          current_page.add_photo(thisphoto)
        else:
          page_list.append(current_page)
          current_page = flickr_photo.Page()
          current_page.add_photo(thisphoto)
      # add final page
      page_list.append(current_page)

      output_file = open(output_filename, 'w') 
      this_section = flickr_photo.Section(output_file)

      for thispage in page_list:
          layout = thispage.layout
          photo_list = thispage.photo_list
          this_section.add_page(thispage)
      # commenting this out since I like it better with date in title
      #regex = re.compile(r"(.*?)\s+([12]\d{3}-\d{2}-\d{2})")
      #matches = re.match(regex,album_title)
      #if matches:
      #    album_title = matches[1]
      #    album_date = matches[2]
      #else:
      #    album_title = album_title
      #    album_date = ''
      # hard-coded value for my own purposes
      album_author = 'Patrick Swickard'
      album_date = ''
      this_section.title = album_title
      this_section.author = album_author
      this_section.date = album_date
      this_section.url = album_url
      qr_img = qrcode.make(album_url)
      qr_path = '/home/swickape/Pictures/flickr/Downloads/qr/' + album_id + '.jpg'
      qr_img.save(qr_path)
      this_section.qr = qr_path
#      all_section_list.append(this_section)
#    for this_section in all_section_list:
      #this_section.print_section()
      # trying this with one book one section for now:
      this_book = flickr_photo.Book(output_file)
      book_author = 'Patrick Swickard'
      album_date = ''
      this_book.title = album_title
      this_book.author = album_author
      this_book.date = album_date
      this_book.url = album_url
      this_book.section_list = [this_section]
      this_book.print_book()
    # that's all folks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
