import json
import flickr_photo
#import flickr_photo_oneup
import qrcode
import re

# NOTE you will need to replace any line with REPLACEME with values appropriate to your system to use this script

def parse_file():
    # this file contains json hash keyed on album id
    # entries are an album title and sequential list of photos
    # with id caption and url
    album_code = '72177720310176444' #REPLACEME
    #album_code = '72157621908701594' # sample album code
    album_file = open('./cache/' + album_code + '/photoset_info.json', 'r')
    album_hash = json.load(album_file)
    album_file.close()
    # this file contains a json hash keyed on photo id
    # entries are metadata for individual photos
    # with additional data about datetaken (possibly inaccurate) width and height
    # the owner (author) id can be obtained as well which could allow for
    # constructing some of the hard-coded urls used in the code if desired
    # e.g. owner has id 99753978@N03 
    album_code_list = []
    for key in album_hash.keys():
      album_code_list.append(key)
    # sort by album title
    album_code_list.sort(key = lambda x: album_hash[x]['title'])
    # process albums in alphabetical order by title
    album_list = []
    for this_album_code in album_code_list:
      # owner_id can be extracted from all_info_file if desired and consistent
      owner_id = album_hash[this_album_code]['owner_id']
      owner_name = album_hash[this_album_code]['owner_name']
      this_album = flickr_photo.Album(this_album_code)
      this_album.id = this_album_code
      this_album.author = owner_name
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
          url = thisphoto_hash['source']
          photo_prefix = this_album.id + '/'
          photo_filename = id + '.jpg'
          location = photo_prefix + photo_filename
          caption = thisphoto_hash['title']
          width = thisphoto_hash['width']
          height = thisphoto_hash['height']
          thisphoto = flickr_photo.Photo(id,url,location,caption,width,height)
          # bonus info
          thisphoto.album_title = this_album.title
          photo_list.append(thisphoto)
      page_list = get_page_list(photo_list)
      this_section = get_section(this_album,page_list)
      all_sections.append(this_section)
    #make_all_single_section_books(all_sections)
    my_paper_width = 6.0
    my_paper_height = 9.0
    my_top_margin = 0.5
    my_bottom_margin = 0.5
    my_left_margin = 0.5
    my_right_margin = 0.5
    make_one_multi_section_book(all_sections,paper_width=my_paper_width,paper_height=my_paper_height,top_margin=my_top_margin,bottom_margin=my_bottom_margin,left_margin=my_left_margin,right_margin=my_right_margin)

def make_one_multi_section_book(all_sections,paper_width,paper_height,top_margin,bottom_margin,left_margin,right_margin):
    section_list = []
    for this_section in all_sections:
        section_list.append(this_section)
    book_filename = 'downloaded_album'
    section_list = section_list
    total_pages = 0
    for this_section in section_list:
      print(this_section.title)
      pages_in_section = len(this_section.page_list)
      print("Pages in section: " + str(pages_in_section))
      total_pages += len(this_section.page_list)
      print("Pages in book so far: " + str(total_pages))
    #output_filename = 'texfiles4/' + book_filename + '.tex'
    output_filename = 'cache/' + book_filename + '.tex'
    output_file = open(output_filename, 'w') 
    #this_book = flickr_photo.BookOneup(output_file)
    #this_book = flickr_photo.BookOneup(output_file)
    #this_book = flickr_photo.BookOneup(output_file,paper_width=6.0,paper_height=9.0,top_margin=0.5,bottom_margin=0.5,left_margin=0.5,right_margin=0.5)
    this_book = flickr_photo.BookOneup(output_file,paper_width=paper_width,paper_height=paper_height,top_margin=top_margin,bottom_margin=bottom_margin,left_margin=left_margin,right_margin=right_margin)
    this_book.title = ''
    this_book.author = ''
    this_book.date = ''
    this_book.url = ''
    this_book.section_list = section_list
    print('Creating tex file for ' + book_filename)
    this_book.print_book()
    print('Album tex file created, see ' + output_filename)

def make_all_single_section_books(all_sections,paper_width,paper_height):
    for this_section in all_sections:
      # for now we are restricting books to one section...
      section_list = [this_section]
      output_filename = 'texfiles/' + this_section.title + '.tex'
      output_file = open(output_filename, 'w') 
      this_book = flickr_photo.BookOneup(output_file)
      this_book.title = this_section.title
      this_book.author = this_section.author
      this_book.date = this_section.date
      this_book.url = this_section.url
      this_book.section_list = section_list
      print('Creating tex file for ' + this_section.title)
      this_book.print_book()

def create_qr_code(this_album):
      print('Creating qr code for ' + this_album.url) 
      qr_img = qrcode.make(this_album.url)
      qr_path = 'qr/' + this_album.id + '.jpg'
      qr_img.save('cache/' + qr_path)
      return qr_path

def get_page_list(photo_list):
      page_list = []
      current_page = flickr_photo.PageOneup()
      for thisphoto in photo_list:
        if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
          current_page.add_photo(thisphoto)
        elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
          current_page.add_photo(thisphoto)
        else:
          page_list.append(current_page)
          current_page = flickr_photo.PageOneup()
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
