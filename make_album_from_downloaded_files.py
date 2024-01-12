"""This script should create a single book from an album"""
import json
import qrcode
import flickr_photo

# NOTE you will need to replace any line with REPLACEME
# with values appropriate to your system to use this script

ONEUP_FORMAT = True
PAPER_WIDTH = 8.5
PAPER_HEIGHT = 11.0
TOP_MARGIN = 0.5
BOTTOM_MARGIN = 0.5
LEFT_MARGIN = 0.5
RIGHT_MARGIN = 0.5
# four lines of 10pt or 12pt font fit in 0.5in
TEXT_HEIGHT = 0.5
LANDSCAPE_WIDTH = PAPER_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
PORTRAIT_WIDTH = PAPER_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
LANDSCAPE_HEIGHT = PAPER_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN - TEXT_HEIGHT
PORTRAIT_HEIGHT = PAPER_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN - TEXT_HEIGHT
# if you run the script for downloading all files from a flickr photoset
# then the files will be in a directory in ./cache/ corresponding to an album code
# and metadata about those images will be in a file in cache
# called photoset_info.json
# this file contains json hash keyed on album id
# entries are an album title and sequential list of photos
# with id caption and url
if ONEUP_FORMAT:
  ALBUM_CODE = '72177720312512993' #REPLACEME
else:
  ALBUM_CODE = '72177720310657841' #REPLACEME
# OTHER ALBUM CODES
#album_code = '72177720310657841' #REPLACEME
#album_code = '72177720311316693' #REPLACEME
#album_code = '72177720310604095' #REPLACEME
#album_code = '72177720310546202' #REPLACEME
#album_code = '72177720310176444' #REPLACEME
#album_code = '72157621908701594' # sample album code
if ONEUP_FORMAT:
  BOOK_FILENAME = 'DFTM_REVISED_AGAIN_SUCKA2'
else:
  BOOK_FILENAME = 'downloaded_album_666_2'

def create_book_from_downloaded_album():
  """This is the main method which creates the book"""
  with open('./cache/' + ALBUM_CODE + '/photoset_info.json', 'r', encoding='utf-8') as myinfile:
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
    this_album = get_album_info(album_hash,this_album_code)
    album_list.append(this_album)
  all_sections = []
  for this_album in album_list:
    # build list of photo objects
    photo_list = []
    for thisphoto_hash in this_album.album_entries:
      thisphoto = get_photo_info(thisphoto_hash,this_album)
      photo_list.append(thisphoto)
    page_list = get_page_list(photo_list)
    this_section = get_section(this_album,page_list)
    all_sections.append(this_section)
  make_one_multi_section_book(all_sections)

def get_photo_info(thisphoto_hash,this_album):
  """Get photo info from photo hash"""
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
  return thisphoto

def get_section(this_album,page_list):
  """Get a single section with qr code """
  this_section = flickr_photo.Section()
  qrdimmax = PAPER_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
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
  if ONEUP_FORMAT:
    this_section.blank_after_qr = True
  else:
    this_section.blank_after_qr = False
  return this_section

def get_album_info(album_hash,this_album_code):
  """Get album info from album hash"""
  # owner_id can be extracted from all_info_file if desired and consistent
  this_album = flickr_photo.Album(this_album_code)
  this_album.id = this_album_code
  this_album.author = album_hash[this_album_code]['owner_name']
  this_album.owner_id = album_hash[this_album_code]['owner_id']
  this_album.date = ''
  this_album.title = album_hash[this_album_code]['title']
  this_album.url = ('https://www.flickr.com/photos/'
                    + this_album.owner_id
                    + '/albums/'
                    + this_album.id)
  this_album.album_entries = album_hash[this_album_code]['photoset_hash']
  return this_album

def make_one_multi_section_book(all_sections):
  """This method makes one multi-section book"""
  section_list = []
  for this_section in all_sections:
    section_list.append(this_section)
  total_pages = 0
  for this_section in section_list:
    print(this_section.title)
    pages_in_section = len(this_section.page_list)
    print("Pages in section: " + str(pages_in_section))
    total_pages += len(this_section.page_list)
    print("Pages in book so far: " + str(total_pages))
  output_filename = 'cache/' + BOOK_FILENAME + '.tex'
  with open(output_filename, 'w', encoding='utf-8') as myoutfile:
    if ONEUP_FORMAT:
      paper_dimensions={
        'paper_width':PAPER_WIDTH,
        'paper_height':PAPER_HEIGHT,
        'top_margin':TOP_MARGIN,
        'bottom_margin':BOTTOM_MARGIN,
        'left_margin':LEFT_MARGIN,
        'right_margin':RIGHT_MARGIN,
      }
      this_book = flickr_photo.BookOneup(myoutfile,paper_dimensions,ONEUP_FORMAT)
    else:
      paper_dimensions={}
      this_book = flickr_photo.Book(myoutfile,paper_dimensions,ONEUP_FORMAT)
    this_book.title = ''
    this_book.author = ''
    this_book.date = ''
    this_book.url = ''
    this_book.section_list = section_list
    print('Creating tex file for ' + BOOK_FILENAME)
    this_book.print_book()
    print('Album tex file created, see ' + output_filename)

def make_all_single_section_books(all_sections):
  """Make all single section books"""
  for this_section in all_sections:
    # for now we are restricting books to one section...
    section_list = [this_section]
    output_filename = 'texfiles/' + this_section.title + '.tex'
    with open(output_filename, 'w', encoding='utf-8') as myoutfile:
      if ONEUP_FORMAT:
        paper_dimensions = {'paper_width':PAPER_WIDTH,
                            'paper_height':PAPER_HEIGHT,
                            'top_margin':TOP_MARGIN,
                            'bottom_margin':BOTTOM_MARGIN,
                            'left_margin':LEFT_MARGIN,
                            'right_margin':RIGHT_MARGIN,
                           }
        this_book = flickr_photo.BookOneup(myoutfile,paper_dimensions,ONEUP_FORMAT)
      else:
        paper_dimensions={}
        this_book = flickr_photo.Book(myoutfile,paper_dimensions,ONEUP_FORMAT)
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
  print('Using: LW ' + str(LANDSCAPE_WIDTH)
        + ' LH ' + str(LANDSCAPE_HEIGHT)
        + ' PW ' + str(PORTRAIT_WIDTH)
        + ' PH ' + str(PORTRAIT_HEIGHT))
  page_list = []
  if ONEUP_FORMAT:
    current_page = flickr_photo.PageOneup(landscape_width=LANDSCAPE_WIDTH,
                                          landscape_height=LANDSCAPE_HEIGHT,
                                          portrait_width=PORTRAIT_WIDTH,
                                          portrait_height=PORTRAIT_HEIGHT)
  else:
    current_page = flickr_photo.Page()
  for thisphoto in photo_list:
    if (thisphoto.orientation == 'L') and (current_page.canfit_l()):
      current_page.add_photo(thisphoto)
    elif (thisphoto.orientation == 'P') and (current_page.canfit_p()):
      current_page.add_photo(thisphoto)
    else:
      page_list.append(current_page)
      if ONEUP_FORMAT:
        current_page = flickr_photo.PageOneup(landscape_width=LANDSCAPE_WIDTH,
                                              landscape_height=LANDSCAPE_HEIGHT,
                                              portrait_width=PORTRAIT_WIDTH,
                                              portrait_height=PORTRAIT_HEIGHT)
      else:
        current_page = flickr_photo.Page()
      current_page.add_photo(thisphoto)
  # add final page
  page_list.append(current_page)
  return page_list

if __name__ == '__main__':
  create_book_from_downloaded_album()
