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
