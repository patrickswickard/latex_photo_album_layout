# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo
import qrcode
import re

def parse_file():
    # this file contains json hash keyed on album id
    # entries are an album title and sequential list of photos
    # with id caption and url
    album_file = open('allalbumswithurls2.json', 'r')
    album_hash = json.load(album_file)
    album_file.close()
    # this file contains a json hash keyed on photo id
    # entries are metadata for individual photos
    # with additional data about datetaken (possibly inaccurate) width and height
    # the owner (author) id can be obtained as well which could allow for
    # constructing some of the hard-coded urls used in the code if desired
    # e.g. owner has id 99753978@N03 
    all_info_file = open('all_info_file.json', 'r')
    all_info_hash = json.load(all_info_file)
    all_info_file.close()
    album_code_list = []
    for key in album_hash.keys():
      album_code_list.append(key)
    # sort by album title
    album_code_list.sort(key = lambda x: album_hash[x]['title'])
    # album_code_list now contains a bunch of album codes sorted in alphabetical order by album title
    # from here we dutifully march through every album we parsed out into this list
    # and as currently written we create one section per album with photos laid out in order
    # and then we create a book containing exactly one section based on that album
    for this_album_code in album_code_list:
      album_id = this_album_code
      owner_id = '99753978@N03'
      album_url = 'https://www.flickr.com/photos/' + owner_id + '/albums/' + album_id
      album_title = album_hash[this_album_code]['title']
      album_entries = album_hash[this_album_code]['photoset_hash']
      #photo_list = get_photo_list(this_album_code,album_hash,all_info_hash)
      photo_list = get_photo_list(this_album_code,album_hash,all_info_hash)
      page_list = get_page_list(photo_list)
      this_section = get_section(album_title,album_url,album_id,page_list)
      this_book = get_book(album_title,album_url,album_id,this_album_code,this_section)

def create_qr_code(album_url,album_id):
      print('Creating qr code for ' + album_url) 
      qr_img = qrcode.make(album_url)
      qr_path = '/home/swickape/Pictures/flickr/Downloads/qr/' + album_id + '.jpg'
      qr_img.save(qr_path)
      return qr_path

def get_photo(thisphoto_hash,all_info_hash,album_title):
    caption = thisphoto_hash['title']
    id = thisphoto_hash['id']
    url = thisphoto_hash['url']
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
    #thisphoto.album_url = album_url
    return thisphoto

# this uses album_hash to get album_title and album_entries
# this uses all_info_hash to get width and height
def get_photo_list(this_album_code,album_hash,all_info_hash):
      album_id = this_album_code
      owner_id = '99753978@N03'
      album_url = 'https://www.flickr.com/photos/' + owner_id + '/albums/' + album_id
      #album_url = 'https://www.flickr.com/photos/99753978@N03/albums/' + album_id
      album_title = album_hash[this_album_code]['title']
      album_entries = album_hash[this_album_code]['photoset_hash']
      photo_list = []
      for thisphoto_hash in album_entries:
        thisphoto = get_photo(thisphoto_hash,all_info_hash,album_title)
        photo_list.append(thisphoto)
      return photo_list

def get_page_list(photo_list):
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
      return page_list

def get_section(album_title,album_url,album_id,page_list):
      this_section = flickr_photo.Section()
      for thispage in page_list:
          layout = thispage.layout
          photo_list = thispage.photo_list
          this_section.add_page(thispage)
      album_author = 'Patrick Swickard'
      album_date = ''
      this_section.title = album_title
      this_section.author = album_author
      this_section.date = album_date
      this_section.url = album_url
      qr_path = create_qr_code(album_url,album_id)
      this_section.qr = qr_path
      return this_section

def get_book(album_title,album_url,album_id,this_album_code,this_section):
      output_filename = 'texfiles/' + album_title + '.tex'
      output_file = open(output_filename, 'w') 
      this_book = flickr_photo.Book(output_file)
      book_author = 'Patrick Swickard'
      album_author = 'Patrick Swickard'
      album_date = ''
      this_book.title = album_title
      this_book.author = album_author
      this_book.date = album_date
      this_book.url = album_url
      # trying this with one book one section for now:
      this_book.section_list = [this_section]

      print('Creating tex file for ' + album_title)
      this_book.print_book()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
