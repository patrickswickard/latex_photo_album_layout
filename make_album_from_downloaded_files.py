"""This script should create a single book from an album"""
import json
import qrcode
import flickr_photo

# NOTE you will need to replace any line with REPLACEME
# with values appropriate to your system to use this script

def parse_file():
  """This is the main method which creates the book"""
  my_paper_width = 8.5
  my_paper_height = 11.0
  my_top_margin = 0.5
  my_bottom_margin = 0.5
  my_left_margin = 0.5
  my_right_margin = 0.5
  # this file contains json hash keyed on album id
  # entries are an album title and sequential list of photos
  # with id caption and url
  album_code = '72177720310657841'
  #album_code = '72157621908701594' # sample album code
  with open('./cache/' + album_code + '/photoset_info.json', 'r', encoding='utf-8') as myinfile:
    album_hash = json.load(myinfile)
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
      myid = thisphoto_hash['id']
      url = thisphoto_hash['source']
      photo_prefix = this_album.id + '/'
      photo_filename = myid + '.jpg'
      location = photo_prefix + photo_filename
      caption = thisphoto_hash['title']
      #caption = ''
      width = thisphoto_hash['width']
      height = thisphoto_hash['height']
      thisphoto = flickr_photo.Photo(myid,url,location,caption,width,height)
      # bonus info
      thisphoto.album_title = this_album.title
      photo_list.append(thisphoto)
    page_list = get_page_list(photo_list)
    this_section = get_section(this_album,page_list,my_paper_width,my_left_margin,my_right_margin)
    this_section.blank_after_qr = False
    all_sections.append(this_section)
  make_one_multi_section_book(all_sections,
                              paper_width=my_paper_width,
                              paper_height=my_paper_height,
                              top_margin=my_top_margin,
                              bottom_margin=my_bottom_margin,
                              left_margin=my_left_margin,
                              right_margin=my_right_margin)

def make_one_multi_section_book(all_sections,paper_width,paper_height,
                                top_margin,bottom_margin,
                                left_margin,right_margin):
  """This method makes one multi-section book"""
  print(paper_width)
  print(paper_height)
  print(top_margin)
  print(bottom_margin)
  print(left_margin)
  print(right_margin)
  section_list = []
  for this_section in all_sections:
    section_list.append(this_section)
  book_filename = 'downloaded_album_666_2'
  total_pages = 0
  for this_section in section_list:
    print(this_section.title)
    pages_in_section = len(this_section.page_list)
    print("Pages in section: " + str(pages_in_section))
    total_pages += len(this_section.page_list)
    print("Pages in book so far: " + str(total_pages))
  output_filename = 'cache/' + book_filename + '.tex'
  myoutfile = open(output_filename, 'w', encoding='utf-8')
  this_book = flickr_photo.Book(myoutfile)
  this_book.title = ''
  this_book.author = ''
  this_book.date = ''
  this_book.url = ''
  this_book.section_list = section_list
  print('Creating tex file for ' + book_filename)
  this_book.print_book()
  print('Album tex file created, see ' + output_filename)

def make_all_single_section_books(all_sections):
  """Make all single section books"""
  for this_section in all_sections:
    # for now we are restricting books to one section...
    section_list = [this_section]
    output_filename = 'texfiles/' + this_section.title + '.tex'
    myoutfile = open(output_filename, 'w', encoding='utf-8')
    this_book = flickr_photo.Book(myoutfile)
    this_book.title = this_section.title
    this_book.author = this_section.author
    this_book.date = this_section.date
    this_book.url = this_section.url
    this_book.section_list = section_list
    print('Creating tex file for ' + this_section.title)
    this_book.print_book()

def create_qr_code(this_album):
  """Create a qr code corresponding to url for an album"""
  print('Creating qr code for ' + this_album.url)
  qr_img = qrcode.make(this_album.url)
  qr_path = 'qr/' + this_album.id + '.jpg'
  qr_img.save('cache/' + qr_path)
  return qr_path

def get_page_list(photo_list):
  """Get list of pages"""
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

def get_section(this_album,page_list,paper_width,left_margin,right_margin):
  """Get a single section with qr code """
  this_section = flickr_photo.Section()
  qrdimmax = paper_width - left_margin - right_margin
  if qrdimmax < 5.19:
    qrdim = qrdimmax
  else:
    qrdim = 5.19
  this_section.qrdim = qrdim
  for thispage in page_list:
    this_section.add_page(thispage)
  this_section.title = this_album.title
  this_section.author = this_album.author
  this_section.date = this_album.date
  this_section.url = this_album.url
  qr_path = create_qr_code(this_album)
  this_section.qr = qr_path
  return this_section

if __name__ == '__main__':
  parse_file()
