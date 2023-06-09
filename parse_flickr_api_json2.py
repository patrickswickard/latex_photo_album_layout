# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import flickr_photo
import qrcode
import re
import PIL

def parse_file():
    # this file contains json hash keyed on album id
    # entries are an album title and sequential list of photos
    # with id caption and url
    album_file = open('allalbumswithurls4.json', 'r')
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
    album_list = []
    for this_album_code in album_code_list:
      # owner_id can be extracted from all_info_file if desired and consistent
      owner_id = '99753978@N03'
      this_album = flickr_photo.Album(this_album_code)
      this_album.id = this_album_code
      this_album.author = 'Patrick Swickard'
      this_album.date = ''
      this_album.title = album_hash[this_album_code]['title']
      this_album.url = 'https://www.flickr.com/photos/' + owner_id + '/albums/' + this_album.id
      this_album.album_entries = album_hash[this_album_code]['photoset_hash']
      album_list.append(this_album)
    all_sections = []
    for this_album in album_list:
      # build list of photo objects
      photo_list = []
      for thisphoto_hash in this_album.album_entries:
          id = thisphoto_hash['id']
#          url = thisphoto_hash['url']
          url = ''
          prefix = '/home/swickape/Pictures/flickr/Downloads/' + this_album.title + '/'
          photo_filename = id + '.jpg'
          location = prefix + photo_filename
          caption = thisphoto_hash['title']
          width = 0
          height = 0
          if id in all_info_hash:
            width = all_info_hash[id]['width_o']
            height = all_info_hash[id]['height_o']
          else:
            actual_image = PIL.Image.open(location)
            width = actual_image.width
            height = actual_image.height
          #width = actual_image.width
          #height = actual_image.height
          thisphoto = flickr_photo.Photo(id,url,location,caption,width,height)
          # bonus info
          thisphoto.album_title = this_album.title
          photo_list.append(thisphoto)
      page_list = get_page_list(photo_list)
      this_section = get_section(this_album,page_list)
      all_sections.append(this_section)
    #make_all_single_section_books(all_sections)
    make_one_multi_section_book(all_sections)
    #make_one_big_book_all_text(all_sections)

def make_one_multi_section_book(all_sections):
    section_list = []
    for this_section in all_sections:
        section_list.append(this_section)
    #book_filename = 'ctr_001'
    #section_list = section_list[0:5]
    #book_filename = 'ctr_002'
    #section_list = section_list[5:8]
    #book_filename = 'ctr_003'
    #section_list = section_list[8:10]
    #book_filename = '_ctr_004'
    #section_list = section_list[10:14]
    #book_filename = 'ctr_005'
    #section_list = section_list[14:18]
    #book_filename = 'ctr_006'
    #section_list = section_list[18:23]
    #book_filename = 'ctr_007'
    #section_list = section_list[23:27]
    #book_filename = 'ctr_008'
    #section_list = section_list[27:31]
    #book_filename = 'ctr_009'
    #section_list = section_list[31:35]
    #book_filename = 'ctr_010'
    #section_list = section_list[35:38]
    #book_filename = 'ctr_011'
    #section_list = section_list[38:44]
    #book_filename = 'ctr_012'
    #section_list = section_list[44:51]
    #book_filename = 'ctr_013'
    #section_list = section_list[51:56]
    #book_filename = 'ctr_014'
    #section_list = section_list[56:59]
    #book_filename = 'ctr_015'
    #section_list = section_list[59:64]
    #book_filename = 'ctr_016'
    #section_list = section_list[64:67]
    #book_filename = 'ctr_017'
    #section_list = section_list[67:69]
    #book_filename = 'ctr_018'
    #section_list = section_list[69:73]
    #book_filename = 'ctr_019'
    #section_list = section_list[73:76]
    #book_filename = 'ctr_020'
    #section_list = section_list[76:103]
    #book_filename = 'ctr_021'
    #section_list = section_list[103:115]
    #book_filename = 'ctr_022'
    #section_list = section_list[115:131]
    #book_filename = 'ctr_023'
    #section_list = section_list[131:142]
    #book_filename = 'ctr_024'
    #section_list = section_list[142:156]
    #book_filename = 'ctr_025'
    #section_list = section_list[156:170]
    #book_filename = 'ctr_027'
    #section_list = section_list[178:190]
    #book_filename = 'ctr_028'
    #section_list = section_list[191:205]
    #book_filename = 'ctr_029'
    #section_list = section_list[205:207]
    #book_filename = 'ctr_030'
    #section_list = section_list[207:212]
    #book_filename = 'ctr_031'
    #section_list = section_list[212:218]
    #book_filename = 'ctr_032'
    #section_list = section_list[218:222]
    #book_filename = 'ctr_033'
    #section_list = section_list[222:230]
    #book_filename = 'ctr_034'
    #section_list = section_list[230:242]
    #book_filename = 'ctr_035'
    #section_list = section_list[242:251]
    #book_filename = 'ctr_036'
    #section_list = section_list[251:260]
    #book_filename = 'ctr_037'
    #section_list = section_list[260:268]
    #book_filename = 'ctr_038'
    #section_list = section_list[268:274]
    #book_filename = 'ctr_039'
    #section_list = section_list[274:278]
    #book_filename = 'ctr_040'
    #section_list = section_list[278:281]
    #book_filename = 'ctr_041'
    #section_list = section_list[281:284]
    #book_filename = 'ctr_042'
    #section_list = section_list[284:290]
    #book_filename = 'ctr_043'
    #section_list = section_list[290:295]
    #book_filename = 'ctr_044'
    #section_list = section_list[295:298]
    #book_filename = 'ctr_045'
    #section_list = section_list[299:304]
    #book_filename = 'ctr_046'
    #section_list = section_list[304:308]
    #book_filename = 'ctr_047'
    #section_list = section_list[308:315]
    #book_filename = 'ctr_048'
    #section_list = section_list[315:322]
    #book_filename = 'ctr_049'
    #section_list = section_list[322:327]
    book_filename = 'ctr_050'
    section_list = section_list[333:343]
    total_pages = 0
    for this_section in section_list:
      print(this_section.title)
      pages_in_section = len(this_section.page_list)
      print("Pages in section: " + str(pages_in_section))
      total_pages += len(this_section.page_list)
      print("Pages in book so far: " + str(total_pages))
    output_filename = 'texfiles2/' + book_filename + '.tex'
    output_file = open(output_filename, 'w') 
    this_book = flickr_photo.Book(output_file)
    this_book.title = ''
    this_book.author = ''
    this_book.date = ''
    this_book.url = ''
    this_book.section_list = section_list
    print('Creating tex file for ' + book_filename)
    this_book.print_book()

def make_all_single_section_books(all_sections):
    for this_section in all_sections:
      # for now we are restricting books to one section...
      section_list = [this_section]
      output_filename = 'texfiles/' + this_section.title + '.tex'
      output_file = open(output_filename, 'w') 
      this_book = flickr_photo.Book(output_file)
      this_book.title = this_section.title
      this_book.author = this_section.author
      this_book.date = this_section.date
      this_book.url = this_section.url
      this_book.section_list = section_list
      print('Creating tex file for ' + this_section.title)
      this_book.print_book()

def make_one_big_book_all_text(all_sections):
    section_list = []
    for this_section in all_sections:
        section_list.append(this_section)
    book_filename = 'everything3'
    output_filename = 'texfiles3/' + book_filename + '.tex'
    output_file = open(output_filename, 'w') 
    this_book = flickr_photo.Book(output_file)
    this_book.title = ''
    this_book.author = ''
    this_book.date = ''
    this_book.url = ''
    this_book.section_list = section_list
    print('Creating tex file for ' + book_filename)
    this_book.print_book_caption_only()

def create_qr_code(this_album):
      print('Creating qr code for ' + this_album.url) 
      qr_img = qrcode.make(this_album.url)
      qr_path = '/home/swickape/Pictures/flickr/Downloads/qr/' + this_album.id + '.jpg'
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

def get_section(this_album,page_list):
      this_section = flickr_photo.Section()
      for thispage in page_list:
          layout = thispage.layout
          photo_list = thispage.photo_list
          this_section.add_page(thispage)
      this_section.title = this_album.title
      this_section.author = this_album.author
      this_section.date = this_album.date
      this_section.url = this_album.url
      qr_path = create_qr_code(this_album)
      this_section.qr = qr_path
      return this_section

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
