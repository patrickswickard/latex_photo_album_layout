"""Download a photo set from Flickr by id"""
import time
import os
import shutil
import json
import requests

# REPLACEME this changes regularly, see e.g.
# https://www.flickr.com/services/api/explore/flickr.photosets.getPhotos
API_KEY = '33bf6adea0647101a54a3379521c55f5'

photoset_id_list = [
  #'CHANGEME'
  #'72177720311316693'
  #'72177720310176444'
  #'72177720310546202'
  #'72177720310604095'
  #'72177720310657841' #dickjr
  #'72177720314043112' #houses
  #'72177720314181850' #strips
  #'72177720314471684' #angry kevin
  #'72177720314473955' #faces 1
  #'72177720314495494' #faces 2
  '72177720314497835' #wc_en
  #'72177720314493202' #wc_fr
  #'72177720312512993'
]

all_photo_hash = {}

def get_photoset_info(this_photoset_id):
  """Get info about this photoset from flickr and do too much stuff"""
  #base_path = './cache/' + this_photoset_id
  # this url grabs metadata about the photoset from Flickr
  # including things like title, owner_id, owner_name
  # and the actual list of photos in the photoset
  api_get_photolist_url = ('https://www.flickr.com/services/rest/?method='
                           + 'flickr.photosets.getPhotos&api_key=' + API_KEY
                           + '&photoset_id=' + this_photoset_id
                           + '&format=json&nojsoncallback=1')
  print(api_get_photolist_url)
  photolist_api_output = requests.get(api_get_photolist_url)
  print(photolist_api_output.text)
  photolist_hash = json.loads(photolist_api_output.text)
  return photolist_hash

def get_all_photo_hash(photolist_hash,this_photoset_id):
  """Do other stuff"""
  base_path = './cache/' + this_photoset_id
  photolist_title = photolist_hash['photoset']['title']
  owner_id = photolist_hash['photoset']['owner']
  owner_name = photolist_hash['photoset']['ownername']
  print(photolist_title)
  print(owner_id)
  print(owner_name)
  # this is the list of photos in the photoset
  photo_info_list = photolist_hash['photoset']['photo']
  # here we make our own hash for the photoset including the title
  # owner_id owner_name and an (empty) list we add to later
  thisalbum_hash_entry = {}
  thisalbum_hash_entry['title'] = photolist_title
  thisalbum_hash_entry['owner_id'] = owner_id
  thisalbum_hash_entry['owner_name'] = owner_name
  thisalbum_hash_entry['photoset_hash'] = []

  # for each photo in the photoset we need to grab information about that photo
  # including id server title
  # additionally so we know size and orientation of photo we need to do a query
  # against a different API for each photo in the list
  # note that this can be tricky for very large photosets
  for this_photo_info in photo_info_list:
    get_photo_info(this_photo_info,base_path,thisalbum_hash_entry)
  all_photo_hash[this_photoset_id] = thisalbum_hash_entry
  return all_photo_hash
  #dump_all_photo_json_to_cache_dir(this_photoset_id,all_photo_hash)

def dump_all_photo_json_to_cache_dir(this_photoset_id,this_all_photo_hash):
  """Write the all values json file to the cache directory"""
  base_path = './cache/' + this_photoset_id
  with open(base_path + '/photoset_info.json', 'w', encoding='utf-8') as myoutfile:
    myoutfile.write(json.dumps(this_all_photo_hash))

def get_photo_info(this_photo_info,base_path,thisalbum_hash_entry):
  """Get photo info and download photo ultimately I guess"""
  print("easy now...")
  time.sleep(1)
  this_photo_info_hash = {}
  this_photo_id = this_photo_info['id']
  this_photo_server = this_photo_info['server']
  this_photo_title = this_photo_info['title']
  print(this_photo_id)
  print(this_photo_server)
  print(this_photo_title)
  this_photo_info_hash['id'] = this_photo_id
  this_photo_info_hash['server'] = this_photo_server
  this_photo_info_hash['title'] = this_photo_title
  this_photo_sizelist = get_photo_size_info(this_photo_id)
  # weird hack here - Flickr is inconsistent with which sizes
  # are available  We prefer Original if available
  # but may be forced to take Large
  # or quit if neither are available
  preferred_size = ''
  for this_size in this_photo_sizelist:
    if this_size['label'] == 'Original':
      preferred_size = 'Original'
  if not preferred_size:
    for this_size in this_photo_sizelist:
      if this_size['label'] == 'Large':
        preferred_size = 'Large'
  if not preferred_size:
    print('Oops, no preferred sizes found!')
    #break
  for this_size in this_photo_sizelist:
    if this_size['label'] == preferred_size:
      width = this_size['width']
      height = this_size['height']
      source = this_size['source']
      print(width)
      print(height)
      print(source)
      this_photo_info_hash['width'] = width
      this_photo_info_hash['height'] = height
      this_photo_info_hash['source'] = source
      thisalbum_hash_entry['photoset_hash'].append(this_photo_info_hash)
      # this grabs a photo from its url and saves it with a name we choose
      # based on the photo_id value
      photo_filename = base_path + '/' + this_photo_id + '.jpg'
      download_photo_from_web(source,photo_filename)

def get_photo_size_info(this_photo_id):
  """Given a photo id download the photo size info from Flickr with API"""
  # we now can leverage the getSizes api method to grab original size photo urls
  # and then ultimately use those urls to download the photoset
  api_getsizes_url = ('https://www.flickr.com/services/rest/'
                      + '?method=flickr.photos.getSizes&api_key=' + API_KEY
                      + '&photo_id=' + this_photo_id
                      + '&format=json&nojsoncallback=1')
  print(api_getsizes_url)
  getsizes_api_output = requests.get(api_getsizes_url)
  getsizes_hash = json.loads(getsizes_api_output.text)
  this_photo_sizelist = getsizes_hash['sizes']['size']
  return this_photo_sizelist

def download_photo_from_web(source,photo_filename):
  """Given a source url and filename download a photo from web in binary format"""
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

def make_directory_for_photoset(photoset_id):
  """make a directory in cache to download photos to or confirm it exists"""
  base_path = './cache/' + photoset_id
  is_exist = os.path.exists(base_path)
  if not is_exist:
    os.makedirs(base_path)

for my_photoset_id in photoset_id_list:
  make_directory_for_photoset(my_photoset_id)
  my_photolist_hash = get_photoset_info(my_photoset_id)
  my_all_photo_hash = get_all_photo_hash(my_photolist_hash,my_photoset_id)
  dump_all_photo_json_to_cache_dir(my_photoset_id,my_all_photo_hash)
