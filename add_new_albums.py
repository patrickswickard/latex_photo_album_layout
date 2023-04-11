# This )is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

# this is just a utility script that was created to make one big file out of previously downloaded flickr metadata
def add_albums():
    bighash = {}
    all_new_albums_file = open('all_new_albums.json','r')
    all_new_albums_hash = json.load(all_new_albums_file)
    all_new_albums_file.close()
    all_photosets_list = all_new_albums_hash['photosets']['photoset']
    all_albums_with_urls_clone = {}
    for this_photoset in all_photosets_list[1:11]:
        album_title = this_photoset['title']['_content']
        #print(album_title)
        album_id = this_photoset['id']
        #print(album_id)
        owner = '99753978@N03'
        #print(owner)
        username = 'citythatreads'
        #print(username)
        special_hash_filename = '/home/swickape/Pictures/flickr/Downloads/' + album_title + '/album_info.json'
        special_hash_file = open(special_hash_filename,'r')
        special_hash = json.load(special_hash_file)
        photo_list = special_hash['photoset']['photo']
        #print(photo_list)
        special_hash_file.close()
        all_albums_with_urls_clone[album_id] = {}
        all_albums_with_urls_clone[album_id]['title'] = album_title
        all_albums_with_urls_clone[album_id]['photoset_hash'] = photo_list
    all_old_albums_file = open('/home/swickape/projects/github/latex_photo_album_layout/allalbumswithurls3.json','r')
    all_old_albums_hash = json.load(all_old_albums_file)
    clone_keys = all_albums_with_urls_clone.keys()
    for thiskey in clone_keys:
        all_old_albums_hash[thiskey] = all_albums_with_urls_clone[thiskey]
    all_old_albums_file.close()
    final_file = open('all_newest_albums.json','w')
    final_file.write(json.dumps(all_old_albums_hash))
    final_file.close()
    
    #all_info_file.write(json.dumps(bighash))
    #all_info_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_albums()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
