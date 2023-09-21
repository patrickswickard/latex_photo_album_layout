generic_poem_title_1 = 'TITLE1'
generic_poem_title_2 = 'TITLE1'
generic_poem_body_1 = [
  'LINE1-1',
  'LINE1-2',
  'LINE1-3',
  'LINE1-4',
  'LINE1-5',
]
generic_poem_body_2 = [
  'LINE2-1',
  'LINE2-2',
  'LINE2-3',
  'LINE2-4',
  'LINE2-5',
]
generic_poem_image1 = 'cache/GENERIC/GENERIC1.jpg'
generic_poem_image2 = 'cache/GENERIC/GENERIC2.jpg'

class Poem:
  def __init__(self):
    self.title = 'UNTITLED'
    self.body = []
    self.image = 'cache/GENERIC/noimage.jpg'

poem1 = Poem()
