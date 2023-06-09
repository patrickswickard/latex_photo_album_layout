# latex_photo_album_layout
layout for 8.5x11" photo album with LaTeX

The problem being solved here is to sequentially display landscape photos and portrait photos on a page of dimensions 8.5"x11" in a compact, uniform, and aesthetically-pleasing fashion for print, with as many as four portrait photographs or two landscape photographs per page or some combination thereof.  Python code is being used to generate LaTeX which can then be used to generate PDF files for print or electronic publication.

The goal was to automate this process so that an album of captioned photos in those formats may be submitted to the script and a LaTeX file automatically generated from the photos and captions.  This was ultimately done incorporating the Flickr API described at https://www.flickr.com/services/api/

This project was originally undertaken to create a fifty-volume run of roughly 30,000 of the author's own photos located on his Flickr account.  This project was completed and then some of the code was expanded to make it possible for other users to download their own albums if desired.  See Usage section below.

Note: need to import pylatex package:
pip3 install pylatex

also need qrcode package:
pip3 install qrcode

and
pip3 install requests

(I think those are all the non-standard ones...)

Usage:

This project contains a lot of messy hacked scripts to deal with some previously-downloaded photo albums and metadata unique to the author's environment and situation.  However, there are two files that can be tweaked for general usage.

download_photoset_from_flickr.py :
A script to systematically download all the album files from a particular Flickr album.  It has two hard-coded REPLACEME values in it that can be changed by the user in a hopefully-obvious manner.  The first is the album id, a numeric value which can be found in an album url which generally looks like:
https://www.flickr.com/photos/USERID/albums/ALBUM_ID


The second is an api key.  This can be requested from Flickr or, sneakily, may be obtained from the frequently-changing value used in their explore API section.  For example, go to https://www.flickr.com/services/api/explore/flickr.photosets.getPhotos and if you perform a request you can examine the url generated at the bottom of the page to find a temporary API key that will work for a short duration. 

Downloaded photos will be stored in the cache directory in a folder created that is keyed on the album id.  This folder will also contain a photoset_info.json file containing metadata for that album.

make_album_from_downloaded_files.py
This makes a .tex file from the downloaded files in the cache directory.  The output .tex file will be stored in this directory.  The user will need to specify the album id, swapping out REPLACEME for the desired album id.  For print publication the tex file should probably be turned into a PDF file.  The author uses MikTex and TexMaker for this task, which has been tested and works well on Linux and Windows.

MikTex: https://miktex.org/

TexMaker: https://www.xm1math.net/texmaker/
