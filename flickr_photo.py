class Photo:
  def __init__(self,id,location,caption,width,height):
    self.id = id
    self.location = location
    self.caption = caption
    self.width = width
    self.height = height
    if width < height:
      self.orientation = 'P'
    else:
      self.orientation = 'L'

class Page:
    def __init__(self):
      self.photo_list = []
      self.layout = ''

    def add_photo(self,photo):
      self.photo_list.append(photo)
      self.layout += photo.orientation

    def canfit_l(self):
      if (self.layout == ''):
        return True
      if (self.layout == 'L'):
        return True
      if (self.layout == 'P'):
        return True
      if (self.layout == 'PP'):
        return True
      return False

    def canfit_p(self):
      if (self.layout == ''):
        return True
      if (self.layout == 'L'):
        return True
      if (self.layout == 'LP'):
        return True
      if (self.layout == 'P'):
        return True
      if (self.layout == 'PP'):
        return True
      if (self.layout == 'PPP'):
        return True
      return False

    def print_landscape_line(thisfile,filename):
      thisfile.write('\\includegraphics[width=5.19in]{landscape.jpg}\n')

    def print_caption_line(thisfile,text):
      thisfile.write(text +'\\\\\n')

    def print_portrait_line(thisfile, filename):
      thisfile.write('\\includegraphics[height=4in]{portrait.jpg}\n')

    def print_ll(thisfile,land1,land2,capt_l1,capt_l2):
      thisfile.write('\n')
      thisfile.write('% Layout LL\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      print_landscape_line(thisfile, land2)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_l1)
      print_caption_line(thisfile, capt_l2)
      thisfile.write('\\pagebreak\n')

    def print_l(thisfile,land1,capt_l1):
      thisfile.write('\n')
      thisfile.write('% Layout L\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_l1)
      thisfile.write('\\pagebreak\n')

    def print_pppp(thisfile,port1,port2,port3,port4,capt_p1,capt_p2,capt_p3,capt_p4):
      thisfile.write('\n')
      thisfile.write('% Layout PPPP\n')
      print_portrait_line(thisfile, port1)
      print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      print_portrait_line(thisfile, port3)
      print_portrait_line(thisfile, port4)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_p2)
      print_caption_line(thisfile, capt_p3)
      print_caption_line(thisfile, capt_p4)
      thisfile.write('\\pagebreak\n')

    def print_ppp(thisfile,port1,port2,port3,capt_p1,capt_p2,capt_p3):
      thisfile.write('\n')
      thisfile.write('% Layout PPP\n')
      print_portrait_line(thisfile, port1)
      print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      print_portrait_line(thisfile, port3)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_p2)
      print_caption_line(thisfile, capt_p3)
      thisfile.write('\\pagebreak\n')

    def print_pp(thisfile,port1,port2,capt_p1,capt_p2):
      thisfile.write('\n')
      thisfile.write('% Layout PP\n')
      print_portrait_line(thisfile, port1)
      print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_p2)
      thisfile.write('\\pagebreak\n')

    def print_p(thisfile,port1,capt_p1):
      thisfile.write('\n')
      thisfile.write('% Layout P\n')
      print_portrait_line(thisfile, port1)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      thisfile.write('\\pagebreak\n')

    def print_ppl(thisfile,port1,port2,land1,capt_p1,capt_p2,capt_l1):
      thisfile.write('\n')
      thisfile.write('% Layout PPL\n')
      print_portrait_line(thisfile, port1)
      print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_p2)
      print_caption_line(thisfile, capt_l1)
      thisfile.write('\\pagebreak\n')

    def print_lpp(thisfile,land1,port1,port2,capt_l1,capt_p1,capt_p2):
      thisfile.write('\n')
      thisfile.write('% Layout LPP\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      print_portrait_line(thisfile, port1)
      print_portrait_line(thisfile, port2)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_l1)
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_p2)
      thisfile.write('\\pagebreak\n')

    def print_pl(thisfile,port1,land1,capt_p1,capt_l1):
      thisfile.write('\n')
      thisfile.write('% Layout PL\n')
      print_portrait_line(thisfile, port1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_p1)
      print_caption_line(thisfile, capt_l1)
      thisfile.write('\\pagebreak\n')

    def print_lp(thisfile,land1,port1,capt_l1,capt_p1):
      thisfile.write('\n')
      thisfile.write('% Layout LP\n')
      print_landscape_line(thisfile, land1)
      thisfile.write('\n')
      thisfile.write('\\vspace{0.25in}\n')
      print_portrait_line(thisfile, port1)
      thisfile.write('\n')
      print_caption_line(thisfile, capt_l1)
      print_caption_line(thisfile, capt_p1)
      thisfile.write('\\pagebreak\n')

