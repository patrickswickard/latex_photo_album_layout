"""Add albums script"""
import json

# this is just a utility script that was created to make one big file
# out of previously downloaded flickr metadata
def add_albums():
  """Add new albums"""
  with open('all_newest_albums.json','r',encoding='utf-8') as myinfile:
    all_new_albums_hash = json.load(myinfile)
  all_photosets_list = all_new_albums_hash['photosets']['photoset']
  all_albums_with_urls_clone = {}
  for this_photoset in all_photosets_list[1:11]:
    album_title = this_photoset['title']['_content']
    album_id = this_photoset['id']
    #owner = '99753978@N03'
    #username = 'citythatreads'
    special_hash_filename = ('/home/swickape/Pictures/flickr/Downloads/'
                             + album_title
                             + '/album_info.json')
    with open(special_hash_filename,'r',encoding='utf-8') as myinfile:
      special_hash = json.load(myinfile)
    photo_list = special_hash['photoset']['photo']
    all_albums_with_urls_clone[album_id] = {}
    all_albums_with_urls_clone[album_id]['title'] = album_title
    all_albums_with_urls_clone[album_id]['photoset_hash'] = photo_list
  with open('/home/swickape/projects/github/latex_photo_album_layout/allalbumswithurls3.json',
            'r',encoding='utf-8') as myinfile:
    all_old_albums_hash = json.load(myinfile)
  clone_keys = all_albums_with_urls_clone.keys()
  for thiskey in clone_keys:
    all_old_albums_hash[thiskey] = all_albums_with_urls_clone[thiskey]
  with open('all_newest_albums.json','w',encoding='utf-8') as myoutfile:
    myoutfile.write(json.dumps(all_old_albums_hash))

if __name__ == '__main__':
  add_albums()
