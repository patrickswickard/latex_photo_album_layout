# latex_photo_album_layout
layout for 8.5x11" photo album with LaTeX

The problem being solved here is to sequentially display landscape photos (ratio 4x3) and portrait photos (ratio 3x4) on a page of dimensions 8.5"x11" in a compact, uniform, and aesthetically-pleasing fashion for print, with as many as four portrait photographs or two landscape photographs per page or some combination thereof.  Python code is being used to generate LaTeX which can then be used to generate PDF files for print or electronic publication.

The eventual goal is to automate this process so that an album of captioned photos in those formats may be submitted to the script and a LaTeX file automatically generated from the photos and captions.  This may eventually be done incorporating the Flickr API described at https://www.flickr.com/services/api/

Note: need to import pylatex package:
pip3 install pylatex

also need qrcode package:
pip3 install qrcode

Note that qrcode creation is commented out since it should be static, uncomment if necessary

Usage:

This is currently only configured to work with a hard-coded path with image files on my laptop.

Album number is hard-coded at top of file, output file will currently be named splay2.tex which can then be used to build a pdf with a program such as texmaker.

Future implementation of this will hopefully take the url of a photo album from Flickr as input, download photos to a cache directory, download metadata for captions, and then spit out an appropriate .tex file for the user.

Could also potentially use pylatex package to create the pdf directly and skip using external program.

May also add further enhancements to beautify layout.

python3 parse_flickr_api_json.py 

Current flaws and room for improvement:
It would be nice to have urls pointing to individual flickr albums where relevant.  This could be a one-time data harvest, there are about 360 of them.
It would be nice to be able to generate qr codes that would point the user to individual albums or at least print url for them.
Separate script to auto-generate PDFs for covers using title and image input.
