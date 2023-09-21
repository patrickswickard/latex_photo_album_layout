generic_poem_title_1 = 'TITLE1'
generic_poem_title_2 = 'TITLE2'
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

  def return_section(self):
    section_string =  """% Layout ???
\\begin{center}\includegraphics[width=5.0in,height=6.5in,keepaspectratio]{GENERIC/GENERIC1.jpg}
\\end{center}
\\begin{center}
\\textbf{"""
    section_string += self.title
    section_string += """}\\\\
\\vskip 0.2in
"""
    for thisline in self.body:
      section_string += thisline
      section_string += """\\\\\n"""
    section_string += """\end{center}
\pagebreak
"""
    return section_string

  def return_web(self):
    section_string =  """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="mystyle.css">
</head>
<body>"""
    section_string += "<img src=\""
    section_string += "images/cancorps/GENERIC/noimage.jpg"
    section_string += "\">\n"
    section_string += "<H1>"
    section_string += "TITLE1"
    section_string += "</H1>\n"
    section_string += "<P>\n"
    for thisline in self.body:
      section_string += thisline
      section_string += "<BR>\n"
    section_string += """<P>
</body>
</html>
"""
    return section_string

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
  poem_section = thispoem.return_section()
  print(poem_section)
  poem_webpage = thispoem.return_web()
  print(poem_webpage)
