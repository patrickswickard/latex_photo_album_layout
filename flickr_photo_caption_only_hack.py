"""This class has tools to create photo books with no captions in .tex format"""
import sys
import pylatex

class Album:
  """Album class for representing a collection of Photos"""
  def __init__(self,albumid):
    self.id = albumid
    self.title = ''
    self.author = ''
    self.owner_id = ''
    self.date = ''
    self.url = ''
    self.album_entries = []

class Photo:
  """Photo class with metadata for a single photo"""
  def __init__(self,photoid,url,location,caption,width,height):
    self.id = photoid
    self.url = url
    self.location = location
    self.caption = pylatex.escape_latex(caption)
    self.width = width
    self.height = height
    if width <= height:
      self.orientation = 'P'
    else:
      self.orientation = 'L'
    self.album_title = ''
    self.album_url = ''

class Page:
  """Class representing a single page with checks to see what layouts can work"""
  def __init__(self):
    photo_max_dims = {}
    one_up = False
    caption_only = True
    if one_up:
      landscape_width = photo_max_dims.get('landscape_width',7.5)
      landscape_height = photo_max_dims.get('landscape_height',9.0)
      portrait_width = photo_max_dims.get('portrait_width',7.5)
      portrait_height = photo_max_dims.get('portrait_height',9.0)
    else:
      landscape_width = photo_max_dims.get('landscape_width',7.5)
      landscape_height = photo_max_dims.get('landscape_height',4)
      portrait_width = photo_max_dims.get('portrait_width',7.5)
      portrait_height = photo_max_dims.get('portrait_height',4)
    self.photo_list = []
    self.layout = ''
    # currently hard-coded for 8.5x11
    self.landscape_width = landscape_width if landscape_width is not None else 7.5
    self.landscape_height = landscape_height if landscape_height is not None else 4
    self.portrait_width = portrait_width if portrait_width is not None else 7.5
    self.portrait_height = portrait_height if portrait_height is not None else 4
    self.one_up = one_up
    self.caption_only = caption_only

  def add_photo(self,photo):
    """Try to add next photo to page"""
    self.photo_list.append(photo)
    self.layout += photo.orientation

  def canfit_l(self):
    """Determine if page can fit another image in landscape orientation"""
    if self.one_up:
      if self.layout == '':
        return True
    else:
      canfit_set = {'','L','P','PP'}
      if self.layout in canfit_set:
        return True
    return False

  def canfit_p(self):
    """Determine if page can fit another image in portrait orientation"""
    if self.one_up:
      if self.layout == '':
        return True
    else:
      canfit_set = {'','L','LP','P','PP','PPP'}
      if self.layout in canfit_set:
        return True
    return False

  def print_landscape_line(self,thisfile,filename):
    """Print a photo inline in landscape format"""
    if self.one_up:
      # center is different
      thisfile.write('\\begin{center}')
      thisfile.write('\\includegraphics[width=' + str(self.landscape_width) + 'in,'
                     + 'height=' + str(self.landscape_height) + 'in,'
                     + 'keepaspectratio]{' + filename + '}\n')
      thisfile.write('\\end{center}')
    else:
      thisfile.write('\\includegraphics[width=' + str(self.landscape_width) + 'in,'
                     + 'height=' + str(self.landscape_height) + 'in,'
                     + 'keepaspectratio]{' + filename + '}\n')

  def print_portrait_line(self,thisfile, filename):
    """Print a photo inline in portrait format"""
    if self.one_up:
      # center is different
      thisfile.write('\\begin{center}\n')
      thisfile.write('\\includegraphics[width=' + str(self.portrait_width) + 'in,'
                     + 'height=' + str(self.portrait_height) + 'in,'
                     + 'keepaspectratio]{' + filename + '}\n')
      thisfile.write('\\end{center}\n')
    else:
      thisfile.write('\\includegraphics[width=' + str(self.portrait_width) + 'in,'
                     + 'height=' + str(self.portrait_height) + 'in,'
                     + 'keepaspectratio]{' + filename + '}\n')

  def print_caption_line(self,thisfile,text):
    """Print a caption line"""
    if self.one_up:
      if text:
        thisfile.write('\\begin{center}\n')
        thisfile.write(text +'\\\\\n')
        thisfile.write('\\end{center}\n')
      else:
        thisfile.write('\n')
    else:
      if text:
        thisfile.write(text +'\\\\\n')
      else:
        thisfile.write('\n')

  # final line does not need linebreak because of pagebreak
  def print_caption_line_final(self,thisfile,text):
    """Print the final caption line (special case)"""
    if self.one_up:
      if text:
        thisfile.write('\\begin{center}\n')
        thisfile.write(text +'\n')
        thisfile.write('\\end{center}\n')
      else:
        thisfile.write('\n')
    else:
      if text:
        thisfile.write(text +'\n')
      else:
        thisfile.write('\n')

  def print_ll(self,thisfile):
    """Print a page with LL orientation"""
    land1 = self.photo_list[0].location
    land2 = self.photo_list[1].location
    capt_l1 = self.photo_list[0].caption
    capt_l2 = self.photo_list[1].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout LL\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      self.print_landscape_line(thisfile, land2)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_l1)
    self.print_caption_line_final(thisfile, capt_l2)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_l(self,thisfile):
    """Print a page with L orientation"""
    land1 = self.photo_list[0].location
    capt_l1 = self.photo_list[0].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout L\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
    self.print_caption_line_final(thisfile, capt_l1)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_pppp(self,thisfile):
    """Print a page with PPPP orientation"""
    port1 = self.photo_list[0].location
    port2 = self.photo_list[1].location
    port3 = self.photo_list[2].location
    port4 = self.photo_list[3].location
    capt_p1 = self.photo_list[0].caption
    capt_p2 = self.photo_list[1].caption
    capt_p3 = self.photo_list[2].caption
    capt_p4 = self.photo_list[3].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout PPPP\n')
      self.print_portrait_line(thisfile, port1)
      self.print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      self.print_portrait_line(thisfile, port3)
      self.print_portrait_line(thisfile, port4)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line(thisfile, capt_p2)
    self.print_caption_line(thisfile, capt_p3)
    self.print_caption_line_final(thisfile, capt_p4)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_ppp(self,thisfile):
    """Print a page with PPP orientation"""
    port1 = self.photo_list[0].location
    port2 = self.photo_list[1].location
    port3 = self.photo_list[2].location
    capt_p1 = self.photo_list[0].caption
    capt_p2 = self.photo_list[1].caption
    capt_p3 = self.photo_list[2].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout PPP\n')
      self.print_portrait_line(thisfile, port1)
      self.print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      self.print_portrait_line(thisfile, port3)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line(thisfile, capt_p2)
    self.print_caption_line_final(thisfile, capt_p3)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_pp(self,thisfile):
    """Print a page with PP orientation"""
    port1 = self.photo_list[0].location
    port2 = self.photo_list[1].location
    capt_p1 = self.photo_list[0].caption
    capt_p2 = self.photo_list[1].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout PP\n')
      self.print_portrait_line(thisfile, port1)
      self.print_portrait_line(thisfile, port2)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line_final(thisfile, capt_p2)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_p(self,thisfile):
    """Print a page with P orientation"""
    port1 = self.photo_list[0].location
    capt_p1 = self.photo_list[0].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout P\n')
      self.print_portrait_line(thisfile, port1)
      thisfile.write('\n')
    self.print_caption_line_final(thisfile, capt_p1)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_ppl(self,thisfile):
    """Print a page with PPL orientation"""
    port1 = self.photo_list[0].location
    port2 = self.photo_list[1].location
    land1 = self.photo_list[2].location
    capt_p1 = self.photo_list[0].caption
    capt_p2 = self.photo_list[1].caption
    capt_l1 = self.photo_list[2].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout PPL\n')
      self.print_portrait_line(thisfile, port1)
      self.print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line(thisfile, capt_p2)
    self.print_caption_line_final(thisfile, capt_l1)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_lpp(self,thisfile):
    """Print a page with LPP orientation"""
    land1 = self.photo_list[0].location
    port1 = self.photo_list[1].location
    port2 = self.photo_list[2].location
    capt_l1 = self.photo_list[0].caption
    capt_p1 = self.photo_list[1].caption
    capt_p2 = self.photo_list[2].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout LPP\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      self.print_portrait_line(thisfile, port1)
      self.print_portrait_line(thisfile, port2)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_l1)
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line_final(thisfile, capt_p2)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_pl(self,thisfile):
    """Print a page with PL orientation"""
    port1 = self.photo_list[0].location
    land1 = self.photo_list[1].location
    capt_p1 = self.photo_list[0].caption
    capt_l1 = self.photo_list[1].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout PL\n')
      self.print_portrait_line(thisfile, port1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_p1)
    self.print_caption_line_final(thisfile, capt_l1)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

  def print_lp(self,thisfile):
    """Print a page with LP orientation"""
    land1 = self.photo_list[0].location
    port1 = self.photo_list[1].location
    capt_l1 = self.photo_list[0].caption
    capt_p1 = self.photo_list[1].caption
    thisfile.write('\n')
    if not self.caption_only:
      thisfile.write('% Layout LP\n')
      self.print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      self.print_portrait_line(thisfile, port1)
      thisfile.write('\n')
    self.print_caption_line(thisfile, capt_l1)
    self.print_caption_line_final(thisfile, capt_p1)
    if not self.caption_only:
      thisfile.write('\\pagebreak\n')

class Section:
  """Class representing a Book section representing a group of related Pages"""
  def __init__(self):
    self.page_list = []
    self.thisfile = ''
    self.title = ''
    self.author = ''
    self.date = ''
    self.url = ''
    self.qr = ''
    self.qrdim = 5.19
    self.blank_after_qr = False
    self.one_up = False
    self.caption_only = True

  def add_page(self,page):
    """Append a page to section"""
    self.page_list.append(page)

  def print_section(self):
    """Print a section of book"""
    if self.qr != '':
      self.print_qr_page(self.thisfile,self.qr)
    if self.caption_only:
      for thispage in self.page_list:
        if thispage.layout == 'LL':
          thispage.print_ll(self.thisfile)
        elif thispage.layout == 'L':
          thispage.print_l(self.thisfile)
        elif thispage.layout == 'PPPP':
          thispage.print_pppp(self.thisfile)
        elif thispage.layout == 'PPP':
          thispage.print_ppp(self.thisfile)
        elif thispage.layout == 'PP':
          thispage.print_pp(self.thisfile)
        elif thispage.layout == 'P':
          thispage.print_p(self.thisfile)
        elif thispage.layout == 'PPL':
          thispage.print_ppl(self.thisfile)
        elif thispage.layout == 'LPP':
          thispage.print_lpp(self.thisfile)
        elif thispage.layout == 'PL':
          thispage.print_pl(self.thisfile)
        elif thispage.layout == 'LP':
          thispage.print_lp(self.thisfile)
        else:
          print('That did not match any known layouts!')
          sys.exit(1)
      self.thisfile.write('\\pagebreak\n')
    else:
      for thispage in self.page_list:
        if thispage.layout == 'LL':
          thispage.print_ll(self.thisfile)
        elif thispage.layout == 'L':
          thispage.print_l(self.thisfile)
        elif thispage.layout == 'PPPP':
          thispage.print_pppp(self.thisfile)
        elif thispage.layout == 'PPP':
          thispage.print_ppp(self.thisfile)
        elif thispage.layout == 'PP':
          thispage.print_pp(self.thisfile)
        elif thispage.layout == 'P':
          thispage.print_p(self.thisfile)
        elif thispage.layout == 'PPL':
          thispage.print_ppl(self.thisfile)
        elif thispage.layout == 'LPP':
          thispage.print_lpp(self.thisfile)
        elif thispage.layout == 'PL':
          thispage.print_pl(self.thisfile)
        elif thispage.layout == 'LP':
          thispage.print_lp(self.thisfile)
        else:
          print('That did not match any known layouts!')
          sys.exit(1)

  @staticmethod
  def print_blank_page(thisfile):
    """Print a blank page"""
    thisfile.write('\\newpage\n')
    thisfile.write('\n')
    thisfile.write('\\ % The empty page\n')
    thisfile.write('\n')
    thisfile.write('\\newpage\n')

  def print_qr_page(self,thisfile,qr_location):
    """Print a page with a qr code"""
    thisfile.write('\n')
    thisfile.write('\\section*{' + self.title + '}\n\n')
    thisfile.write('\\url{' + self.url + '}\n\n')
    thisfile.write('Scan the QR code below to go to the original album '
                   + 'with full-size photos on Flickr:\n\n')
    thisfile.write('\\begin{center}\n')
    thisfile.write('\\includegraphics[width=' + str(self.qrdim) + 'in]{' + qr_location + '}\n')
    thisfile.write('\\end{center}\n')
    thisfile.write('\\pagebreak\n')
    if self.blank_after_qr:
      Section.print_blank_page(thisfile)

class Book:
  """Book class representing a single photo book"""
  def __init__(self,thisfile):
    self.section_list = []
    self.thisfile = thisfile
    self.title = ''
    self.author = ''
    self.date = ''
    self.url = ''
    self.qr = ''
    self.paper_dimensions = {}
    self.one_up = False
    self.caption_only = False

  def print_book(self):
    """Print book to .tex file"""
    thisfile = self.thisfile
    self.print_preamble(thisfile)
    Book.print_begin(thisfile)
    # this is dodgy
    for thissection in self.section_list:
      thissection.thisfile = thisfile
      thissection.print_section()
    Book.print_end(thisfile)
    thisfile.close()

  def print_preamble(self,thisfile):
    """Print preamble of latex document given margins which are currently ignored"""
    if not self.one_up:
      # ignore inputs for now
      self.paper_dimensions = {}
    top_margin = self.paper_dimensions.get('top_margin',0.75)
    bottom_margin = self.paper_dimensions.get('bottom_margin',0.75)
    left_margin = self.paper_dimensions.get('left_margin',0.75)
    right_margin = self.paper_dimensions.get('right_margin',0.75)
    paper_width = self.paper_dimensions.get('paper_width',8.5)
    paper_height = self.paper_dimensions.get('paper_height',11)
    thisfile.write('\\documentclass[10pt,letterpaper]{article}\n')
    if self.one_up:
      thisfile.write('\\pagenumbering{gobble}\n')
    thisfile.write('\\usepackage[top=' + str(top_margin) + 'in,'
                   + ' bottom=' + str(bottom_margin) + 'in,'
                   + ' left=' + str(left_margin) + 'in,'
                   + ' right=' + str(right_margin) + 'in,'
                   + ' paperwidth=' + str(paper_width) + 'in,'
                   + ' paperheight=' + str(paper_height) + 'in'
                   + ']{geometry}\n')
    thisfile.write("\\usepackage{amsfonts,amssymb,amsmath}\n")
    thisfile.write("\\usepackage{pslatex}\n")
    thisfile.write("\\usepackage[pdftex]{graphicx}\n")
    thisfile.write("\\usepackage{float}\n")
    thisfile.write("\\usepackage{hyperref}\n")
    thisfile.write("\\setlength{\\parindent}{0pt}\n")
    thisfile.write("\\title{" + self.title + "}\n")
    thisfile.write("\\author{" + self.author + "}\n")
    thisfile.write("\\date{" + self.date + "}\n")

  @staticmethod
  def print_begin(thisfile):
    """Print beginning of latex document"""
    thisfile.write('\\begin{document}\n')

  @staticmethod
  def print_end(thisfile):
    """Print end of latex document"""
    thisfile.write('\\end{document}\n')
