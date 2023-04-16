import json
import qrcode
import re
import requests
import os
import shutil

api_key = 'REPLACEME' #REPLACEME this changes regularly, see e.g. https://www.flickr.com/services/api/explore/flickr.photosets.getPhotos

photoset_id_list = [
  'REPLACEME'
]


all_photo_hash = {}
for this_photoset_id in photoset_id_list:
  api_get_photolist_url = 'https://www.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=' + api_key + '&photoset_id=' + this_photoset_id + '&format=json&nojsoncallback=1'
  print(api_get_photolist_url)
  photolist_api_output = requests.get(api_get_photolist_url)
  photolist_hash = json.loads(photolist_api_output.text)
  photolist_title = photolist_hash['photoset']['title']
  owner_id = photolist_hash['photoset']['owner']
  owner_name = photolist_hash['photoset']['ownername']
  print(photolist_title)
  print(owner_id)
  print(owner_name)
  photo_info_list = photolist_hash['photoset']['photo']
  thisalbum_hash_entry = {}
  thisalbum_hash_entry['title'] = photolist_title
  thisalbum_hash_entry['owner_id'] = owner_id
  thisalbum_hash_entry['owner_name'] = owner_name
  thisalbum_hash_entry['photoset_hash'] = []
  base_path = './cache/' + this_photoset_id
  isExist = os.path.exists(base_path)
  if not isExist:
    os.makedirs(base_path)
  else:
    print('wtf')

  for this_photo_info in photo_info_list:
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
    # we now can leverage the getSizes api method to grab original size photo urls
    api_getsizes_url = 'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=' + api_key + '&photo_id=' + this_photo_id + '&format=json&nojsoncallback=1'
    print(api_getsizes_url)
    getsizes_api_output = requests.get(api_getsizes_url)
    getsizes_hash = json.loads(getsizes_api_output.text)
    this_photo_sizelist = getsizes_hash['sizes']['size']
    for this_size in this_photo_sizelist:
      if this_size['label'] == 'Large':
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
        url_response = requests.get(source, stream=True)
        photo_filename = base_path + '/' + this_photo_id + '.jpg'
        with open(photo_filename, 'wb') as out_file:
          shutil.copyfileobj(url_response.raw, out_file)
  all_photo_hash[this_photoset_id] = thisalbum_hash_entry
  all_info_file = open(base_path + '/photoset_info.json','w')
  all_info_file.write(json.dumps(all_photo_hash))
  all_info_file.close()
