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
    # process albums in alphabetical order by title
    for this_album_code in album_code_list:
      this_album = flickr_photo.Album(this_album_code)
      # hard-coded params
      album_author = 'Patrick Swickard'
      album_date = ''
      # owner_id can be extracted from all_info_file if desired and consistent
      owner_id = '99753978@N03'
      # params extracted from album_hash
      album_id = this_album_code
      album_title = album_hash[this_album_code]['title']
      album_url = 'https://www.flickr.com/photos/' + owner_id + '/albums/' + album_id
      album_entries = album_hash[this_album_code]['photoset_hash']
      # build list of photo objects
      photo_list = []
      for thisphoto_hash in album_entries:
          id = thisphoto_hash['id']
          url = thisphoto_hash['url']
          prefix = '/home/swickape/Pictures/flickr/Downloads/' + album_title + '/'
          photo_filename = id + '.jpg'
          location = prefix + photo_filename
          caption = thisphoto_hash['title']
          width = all_info_hash[id]['width_o']
          height = all_info_hash[id]['height_o']
          thisphoto = flickr_photo.Photo(id,url,location,caption,width,height)
          thisphoto.album_title = album_title
          # bonus info
          photo_list.append(thisphoto)
      page_list = get_page_list(photo_list)
      this_section = get_section(album_title,album_author,album_date,album_url,album_id,page_list)
      # for now we are restricting books to one section...
      section_list = [this_section]
      this_book = get_book(album_title,album_author,album_date,album_url,album_id,this_album_code,section_list)
      print('Creating tex file for ' + album_title)
      this_book.print_book()

def create_qr_code(album_url,album_id):
      print('Creating qr code for ' + album_url) 
      qr_img = qrcode.make(album_url)
      qr_path = '/home/swickape/Pictures/flickr/Downloads/qr/' + album_id + '.jpg'
      qr_img.save(qr_path)
      return qr_path

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

def get_section(album_title,album_author,album_date,album_url,album_id,page_list):
      this_section = flickr_photo.Section()
      for thispage in page_list:
          layout = thispage.layout
          photo_list = thispage.photo_list
          this_section.add_page(thispage)
      this_section.title = album_title
      this_section.author = album_author
      this_section.date = album_date
      this_section.url = album_url
      qr_path = create_qr_code(album_url,album_id)
      this_section.qr = qr_path
      return this_section

def get_book(album_title,album_author,album_date,album_url,album_id,this_album_code,section_list):
      output_filename = 'texfiles/' + album_title + '.tex'
      output_file = open(output_filename, 'w') 
      this_book = flickr_photo.Book(output_file)
      this_book.title = album_title
      this_book.author = album_author
      this_book.date = album_date
      this_book.url = album_url
      this_book.section_list = section_list
      return this_book

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
