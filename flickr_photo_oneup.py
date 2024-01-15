"""This class has tools to create photo books one-up with captions in .tex format"""
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
    self.photo_list = []
    self.layout = ''

  def add_photo(self,photo):
    """Append a photo"""
    self.photo_list.append(photo)
    self.layout += photo.orientation

  def canfit_l(self):
    """Determine if a landscape photo can fit"""
    if self.layout == '':
      return True
    return False

  def canfit_p(self):
    """Determine if a portrait photo can fit"""
    if self.layout == '':
      return True
    return False

  @staticmethod
  def print_landscape_line(thisfile,filename):
    """Print landscape line"""
    #thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\includegraphics[width=' + str(7.5) + 'in,'
                   + 'height=' + str(9.0) + 'in,'
                   + 'keepaspectratio]{' + filename + '}\n')

  @staticmethod
  def print_portrait_line(thisfile, filename):
    """Print portrait line"""
    #thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\includegraphics[width=' + str(7.5) + 'in,'
                   + 'height=' + str(9.0) + 'in,'
                   + 'keepaspectratio]{' + filename + '}\n')

  @staticmethod
  def print_caption_line(thisfile,text):
    """Print caption line"""
    if text:
      thisfile.write(text +'\\\\\n')
    else:
      thisfile.write('\n')

  # final line does not need linebreak because of pagebreak
  @staticmethod
  def print_caption_line_final(thisfile,text):
    """Print final caption line"""
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
    thisfile.write('% Layout LL\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    Page.print_landscape_line(thisfile, land2)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_l1)
    Page.print_caption_line_final(thisfile, capt_l2)
    thisfile.write('\\pagebreak\n')

  def print_l(self,thisfile):
    """Print a page with L orientation"""
    land1 = self.photo_list[0].location
    capt_l1 = self.photo_list[0].caption
    thisfile.write('\n')
    thisfile.write('% Layout L\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    Page.print_caption_line_final(thisfile, capt_l1)
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
    thisfile.write('% Layout PPPP\n')
    Page.print_portrait_line(thisfile, port1)
    Page.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    Page.print_portrait_line(thisfile, port3)
    Page.print_portrait_line(thisfile, port4)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line(thisfile, capt_p2)
    Page.print_caption_line(thisfile, capt_p3)
    Page.print_caption_line_final(thisfile, capt_p4)
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
    thisfile.write('% Layout PPP\n')
    Page.print_portrait_line(thisfile, port1)
    Page.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    Page.print_portrait_line(thisfile, port3)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line(thisfile, capt_p2)
    Page.print_caption_line_final(thisfile, capt_p3)
    thisfile.write('\\pagebreak\n')

  def print_pp(self,thisfile):
    """Print a page with PP orientation"""
    port1 = self.photo_list[0].location
    port2 = self.photo_list[1].location
    capt_p1 = self.photo_list[0].caption
    capt_p2 = self.photo_list[1].caption
    thisfile.write('\n')
    thisfile.write('% Layout PP\n')
    Page.print_portrait_line(thisfile, port1)
    Page.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line_final(thisfile, capt_p2)
    thisfile.write('\\pagebreak\n')

  def print_p(self,thisfile):
    """Print a page with P orientation"""
    port1 = self.photo_list[0].location
    capt_p1 = self.photo_list[0].caption
    thisfile.write('\n')
    thisfile.write('% Layout P\n')
    Page.print_portrait_line(thisfile, port1)
    thisfile.write('\n')
    Page.print_caption_line_final(thisfile, capt_p1)
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
    thisfile.write('% Layout PPL\n')
    Page.print_portrait_line(thisfile, port1)
    Page.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line(thisfile, capt_p2)
    Page.print_caption_line_final(thisfile, capt_l1)
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
    thisfile.write('% Layout LPP\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    Page.print_portrait_line(thisfile, port1)
    Page.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_l1)
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line_final(thisfile, capt_p2)
    thisfile.write('\\pagebreak\n')

  def print_pl(self,thisfile):
    """Print a page with PL orientation"""
    port1 = self.photo_list[0].location
    land1 = self.photo_list[1].location
    capt_p1 = self.photo_list[0].caption
    capt_l1 = self.photo_list[1].caption
    thisfile.write('\n')
    thisfile.write('% Layout PL\n')
    Page.print_portrait_line(thisfile, port1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_p1)
    Page.print_caption_line_final(thisfile, capt_l1)
    thisfile.write('\\pagebreak\n')

  def print_lp(self,thisfile):
    """Print a page with LP orientation"""
    land1 = self.photo_list[0].location
    port1 = self.photo_list[1].location
    capt_l1 = self.photo_list[0].caption
    capt_p1 = self.photo_list[1].caption
    thisfile.write('\n')
    thisfile.write('% Layout LP\n')
    Page.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    Page.print_portrait_line(thisfile, port1)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_l1)
    Page.print_caption_line_final(thisfile, capt_p1)
    thisfile.write('\\pagebreak\n')

class Section:
  """Class representing a Book section representing a group of related Pages"""
  def __init__(self):
    self.page_list = []
    #self.thisfile = thisfile
    self.title = ''
    self.author = ''
    self.date = ''
    self.url = ''
    self.qr = ''

  def add_page(self,page):
    """Append a page to section"""
    self.page_list.append(page)

  def print_section(self):
    """Print a section of book"""
    thisfile = self.thisfile
    if self.qr != '':
      self.print_qr_page(thisfile,self.qr)
    for thispage in self.page_list:
      if thispage.layout == 'LL':
        thispage.print_ll(thisfile)
      elif thispage.layout == 'L':
        thispage.print_l(thisfile)
      elif thispage.layout == 'PPPP':
        thispage.print_pppp(thisfile)
      elif thispage.layout == 'PPP':
        thispage.print_ppp(thisfile)
      elif thispage.layout == 'PP':
        thispage.print_pp(thisfile)
      elif thispage.layout == 'P':
        thispage.print_p(thisfile)
      elif thispage.layout == 'PPL':
        thispage.print_ppl(thisfile)
      elif thispage.layout == 'LPP':
        thispage.print_lpp(thisfile)
      elif thispage.layout == 'PL':
        thispage.print_pl(thisfile)
      elif thispage.layout == 'LP':
        thispage.print_lp(thisfile)
      else:
        print('That did not match any known layouts!')
        sys.exit(1)

  def print_qr_page(self,thisfile,qr_location):
    """Print a page with a qr code"""
    thisfile.write('\n')
    thisfile.write('\\section*{' + self.title + '}\n\n')
    thisfile.write('\\url{' + self.url + '}\n\n')
    thisfile.write('Scan the QR code below to go to the original album '
                   + 'with full-size photos on Flickr:\n\n')
    thisfile.write('\\includegraphics[width=5.19in]{' + qr_location + '}\n')
    thisfile.write('\\pagebreak\n')

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
    thisfile.write('\\documentclass[10pt,letterpaper]{article}\n')
    thisfile.write('\\usepackage[top=' + str(0.75) + 'in, '
                   + 'bottom=' + str(0.75) + 'in, '
                   + 'left=' + str(0.5) + 'in, '
                   + 'right=' + str(0.5) + 'in, '
                   + 'paperwidth=' + str(8.5) + 'in, '
                   + 'paperheight=' + str(11) + 'in]{geometry}\n')
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
