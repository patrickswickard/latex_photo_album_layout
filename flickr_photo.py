"""This class has tools to create photo books with captions in .tex format"""
import pylatex

class Album:
  """Album class for representing a collection of Photos"""
  def __init__(self,id):
    self.id = id
    self.title = ''
    self.author = ''
    self.date = ''
    self.url = ''
    self.album_entries = []

class Photo:
  """Photo class with metadata for a single photo"""
  def __init__(self,id,url,location,caption,width,height):
    self.id = id
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
    self.landscape_width = 7.5
    self.landscape_height = 4
    self.portrait_width = 7.5
    self.portrait_height = 4

  def add_photo(self,photo):
    """Try to add next photo to page"""
    self.photo_list.append(photo)
    self.layout += photo.orientation

  def canfit_l(self):
    """Determine if page can fit another image in landscape orientation"""
    if self.layout == '':
      return True
    if self.layout == 'L':
      return True
    if self.layout == 'P':
      return True
    if self.layout == 'PP':
      return True
    return False

  def canfit_p(self):
    """Determine if page can fit another image in portrait orientation"""
    if self.layout == '':
      return True
    if self.layout == 'L':
      return True
    if self.layout == 'LP':
      return True
    if self.layout == 'P':
      return True
    if self.layout == 'PP':
      return True
    if self.layout == 'PPP':
      return True
    return False

  def print_landscape_line(self,thisfile,filename):
    """Print a photo inline in landscape format"""
    thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
    #thisfile.write('\\includegraphics[width=7.5in,height=9.5in,keepaspectratio]{' + filename + '}\n')

  def print_portrait_line(self,thisfile, filename):
    """Print a photo inline in portrait format"""
    thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
    #thisfile.write('\\includegraphics[width=7.5in,height=9.5in,keepaspectratio]{' + filename + '}\n')

  @staticmethod
  def print_caption_line(thisfile,text):
    """Print a caption line"""
    if text:
      thisfile.write(text +'\\\\\n')
    else:
      thisfile.write('\n')

  # final line does not need linebreak because of pagebreak
  @staticmethod
  def print_caption_line_final(thisfile,text):
    """Print the final caption line (special case)"""
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
    self.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    self.print_landscape_line(thisfile, land2)
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
    self.print_landscape_line(thisfile, land1)
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
    self.print_portrait_line(thisfile, port1)
    self.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    self.print_portrait_line(thisfile, port3)
    self.print_portrait_line(thisfile, port4)
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
    self.print_portrait_line(thisfile, port1)
    self.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    self.print_portrait_line(thisfile, port3)
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
    self.print_portrait_line(thisfile, port1)
    self.print_portrait_line(thisfile, port2)
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
    self.print_portrait_line(thisfile, port1)
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
    self.print_portrait_line(thisfile, port1)
    self.print_portrait_line(thisfile, port2)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    self.print_landscape_line(thisfile, land1)
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
    self.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    self.print_portrait_line(thisfile, port1)
    self.print_portrait_line(thisfile, port2)
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
    self.print_portrait_line(thisfile, port1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    self.print_landscape_line(thisfile, land1)
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
    self.print_landscape_line(thisfile, land1)
    thisfile.write('\n')
    thisfile.write('\\vspace{0.25in}\n')
    self.print_portrait_line(thisfile, port1)
    thisfile.write('\n')
    Page.print_caption_line(thisfile, capt_l1)
    Page.print_caption_line_final(thisfile, capt_p1)
    thisfile.write('\\pagebreak\n')

class PageOneup(Page):
  """Special instance of Page class except we force one image per page"""
  def __init__(self,landscape_width = None, landscape_height = None, portrait_width = None, portrait_height = None):
    self.photo_list = []
    self.layout = ''
    #self.landscape_width = 5.0
    #self.landscape_height = 7.5
    #self.portrait_width = 5.0
    #self.portrait_height = 7.5
    # currently hard-coded for 6x9
    self.landscape_width = landscape_width if landscape_width is not None else 5.0
    self.landscape_height = landscape_height if landscape_height is not None else 7.5
    self.portrait_width = portrait_width if portrait_width is not None else 5.0
    self.portrait_height = portrait_height if portrait_height is not None else 7.5

  def canfit_l(self):
    if self.layout == '':
      return True
    return False

  def canfit_p(self):
    if self.layout == '':
      return True
    return False

  def print_landscape_line(self,thisfile,filename):
    # historical 8.5x11 values
    #thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
#    thisfile.write('\\includegraphics[width=7.5in,height=9.0in,keepaspectratio]{' + filename + '}\n')
#    thisfile.write('\\includegraphics[width=5.0in,height=7.0in,keepaspectratio]{' + filename + '}\n')
    # use this for 6 x 9 oneup
    #thisfile.write('\\includegraphics[width=5.0in,height=7.5in,keepaspectratio]{' + filename + '}\n')
    #thisfile.write('\\includegraphics[width=' + str(5.0) + 'in,height=' + str(7.5) + 'in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\begin{center}')
    thisfile.write('\\includegraphics[width=' + str(self.landscape_width) + 'in,height=' + str(self.landscape_height) + 'in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\end{center}')
    # use this for 6 x 9 two-up
#    thisfile.write('\\includegraphics[width=5.0in,height=3.25in,keepaspectratio]{' + filename + '}\n')

  def print_portrait_line(self,thisfile, filename):
    # historical 8.5x11 values
    #thisfile.write('\\includegraphics[width=7.5in,height=4in,keepaspectratio]{' + filename + '}\n')
#    thisfile.write('\\includegraphics[width=7.5in,height=9.0in,keepaspectratio]{' + filename + '}\n')
#    thisfile.write('\\includegraphics[width=5.0in,height=7.0in,keepaspectratio]{' + filename + '}\n')
    # use this for 6 x 9 oneup
    #thisfile.write('\\includegraphics[width=5.0in,height=7.5in,keepaspectratio]{' + filename + '}\n')
    #thisfile.write('\\includegraphics[width=' + str(5.0) + 'in,height=' + str(7.5) + 'in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\begin{center}\n')
    thisfile.write('\\includegraphics[width=' + str(self.portrait_width) + 'in,height=' + str(self.portrait_height) + 'in,keepaspectratio]{' + filename + '}\n')
    thisfile.write('\\end{center}\n')
    # use this for 6 x 9 two-up
#    thisfile.write('\\includegraphics[width=5.0in,height=3.25in,keepaspectratio]{' + filename + '}\n')

  # this maybe only looks okay for one-up?
  def print_caption_line(self,thisfile,text):
    if text:
      thisfile.write('\\begin{center}\n')
      thisfile.write(text +'\\\\\n')
      thisfile.write('\\end{center}\n')
    else:
      thisfile.write('\n')

  # this maybe only looks okay for one-up?
  # final line does not need linebreak because of pagebreak
  def print_caption_line_final(self,thisfile,text):
    if text:
      thisfile.write('\\begin{center}\n')
      thisfile.write(text +'\n')
      thisfile.write('\\end{center}\n')
    else:
      thisfile.write('\n')

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
    self.qrdim = 5.19
    self.blank_after_qr = False

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
        raise 'That did not match any known layouts!'

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
    thisfile.write('Scan the QR code below to go to the original album with full-size photos on Flickr:\n\n')
    thisfile.write('\\begin{center}\n')
    thisfile.write('\\includegraphics[width=' + str(self.qrdim) + 'in]{' + qr_location + '}\n')
    thisfile.write('\\end{center}\n')
    thisfile.write('\\pagebreak\n')
    if self.blank_after_qr:
      Section.print_blank_page(thisfile)
    #thisfile.write('\\newpage\n')
    #thisfile.write('\n')
    #thisfile.write('\ % The empty page\n')
    #thisfile.write('\n')
    #thisfile.write('\\newpage\n')

class Book:
  """Book class representing a single photo book"""
  #def __init__(self,thisfile):
  def __init__(self,thisfile,paper_width=None,paper_height=None,top_margin=None,bottom_margin=None,left_margin=None,right_margin=None):
    self.section_list = []
    self.thisfile = thisfile
    self.title = ''
    self.author = ''
    self.date = ''
    self.url = ''
    self.qr = ''
    self.paper_width = paper_width if paper_width is not None else 8.5
    self.paper_height = paper_height if paper_height is not None else 11.0
    self.top_margin = top_margin if top_margin is not None else 0.75
    self.bottom_margin = bottom_margin if bottom_margin is not None else 0.75
    self.left_margin = left_margin if left_margin is not None else 0.5
    self.right_margin = right_margin if right_margin is not None else 0.5
    #self.paper_width = paper_width if paper_width is not None else 6.0
    #self.paper_height = paper_height if paper_height is not None else 9.0
    #self.top_margin = top_margin if top_margin is not None else 0.5
    #self.bottom_margin = bottom_margin if bottom_margin is not None else 0.5
    #self.left_margin = left_margin if left_margin is not None else 0.5
    #self.right_margin = right_margin if right_margin is not None else 0.5

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

  def print_preamble(self,thisfile,top_margin=None,bottom_margin=None,left_margin=None,right_margin=None,paper_width=None,paper_height=None):
    """Print preamble of latex document given margins which are currently ignored"""
    # ignore inputs for now
    top_margin = '0.75in'
    bottom_margin = '0.75in'
    left_margin = '0.75in'
    right_margin = '0.75in'
    paper_width = '8.5in'
    paper_height = '11in'
    thisfile.write('\\documentclass[10pt,letterpaper]{article}\n')
    #thisfile.write('\\usepackage[top=0.75in, bottom=0.75in, left=0.5in, right=0.5in, paperwidth=8.5in, paperheight=11in]{geometry}\n')
    thisfile.write('\\usepackage[top=' + top_margin + ', bottom=' + bottom_margin + ', left=' + left_margin + ', right=' + right_margin + ', paperwidth=' + paper_width + ', paperheight=' + paper_height + ']{geometry}\n')
    # above is what has historically been used but the margins below are probably better
    #thisfile.write('\\usepackage[top=0.5in, bottom=0.5in, left=0.5in, right=0.5in, paperwidth=8.5in, paperheight=11in]{geometry}\n')
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

class BookOneup(Book):
  """Class representing a book that has one image per page"""
  def print_preamble(self,thisfile):
    """Print the latex preamble for a one-up book"""
    thisfile.write('\\documentclass[10pt,letterpaper]{article}\n')
    thisfile.write('\\pagenumbering{gobble}\n')
    # 8.5 x 11 format historical
    #thisfile.write('\\usepackage[top=0.75in, bottom=0.75in, left=0.5in, right=0.5in, paperwidth=8.5in, paperheight=11in]{geometry}\n')
    # 8.5 x 11 format
#    thisfile.write('\\usepackage[top=0.5in, bottom=0.5in, left=0.5in, right=0.5in, paperwidth=6.0in, paperheight=9in]{geometry}\n')
    # 6 x 9 format
    #thisfile.write('\\usepackage[top=0.5in, bottom=0.5in, left=0.5in, right=0.5in, paperwidth=6.0in, paperheight=9in]{geometry}\n')
    thisfile.write('\\usepackage[top=' + str(self.top_margin) + 'in, bottom=' + str(self.bottom_margin) + 'in, left=' + str(self.left_margin) + 'in, right='  + str(self.right_margin) + 'in, paperwidth=' + str(self.paper_width) + 'in, paperheight=' + str(self.paper_height) + 'in]{geometry}\n')
    thisfile.write("\\usepackage{amsfonts,amssymb,amsmath}\n")
    thisfile.write("\\usepackage{pslatex}\n")
    thisfile.write("\\usepackage[pdftex]{graphicx}\n")
    thisfile.write("\\usepackage{float}\n")
    thisfile.write("\\usepackage{hyperref}\n")
    thisfile.write("\\setlength{\\parindent}{0pt}\n")
    thisfile.write("\\title{" + self.title + "}\n")
    thisfile.write("\\author{" + self.author + "}\n")
    thisfile.write("\\date{" + self.date + "}\n")
