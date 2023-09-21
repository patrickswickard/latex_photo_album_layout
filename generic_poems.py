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
generic_poem_image_1 = 'cache/GENERIC/GENERIC1.jpg'
generic_poem_image_2 = 'cache/GENERIC/GENERIC2.jpg'

class Poem:
  def __init__(self):
    self.title = 'UNTITLED'
    self.body = []
    self.image = 'cache/GENERIC/noimage.jpg'

poem_1 = Poem()
poem_2 = Poem()

poem_1.title = generic_poem_title_1
poem_2.title = generic_poem_title_2

poem_1.body = generic_poem_body_1
poem_2.body = generic_poem_body_2

poem_1.image = generic_poem_image_1
poem_2.image = generic_poem_image_2

poem_list = []
poem_list.append(poem_1)
poem_list.append(poem_2)

for thispoem in poem_list:
  print(thispoem.title)
