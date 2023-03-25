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