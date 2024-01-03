"""Quickie class to do a poem book"""
class Poem:
  """Quickie class to do a poem book"""
  def __init__(self):
    self.title = 'UNTITLED'
    self.body = []
    self.image = 'cache/GENERIC/noimage.jpg'
    self.webfilename_full = ''
    self.webfilename_part = ''

  def return_section(self):
    """Return a section of poem book"""
    section_string =  """% Layout ???
\\begin{center}\\includegraphics[width=5.0in,height=6.5in,keepaspectratio]{GENERIC/GENERIC1.jpg}
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
    section_string += """\\end{center}
\\pagebreak
"""
    return section_string

  def return_web(self):
    """Return a section of poem book for web"""
    section_string =  """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="mystyle.css">
</head>
<body>"""
#    section_string += "images/cancorps/GENERIC/noimage.jpg"
    section_string += "<H1>"
    section_string += self.title
    section_string += "</H1>\n"
    section_string += "<P>\n"
    for thisline in self.body:
      section_string += thisline
      section_string += "<BR>\n"
    section_string += "<P>\n"
    section_string += "<img style=\"max-width:100%;height:auto;\" src=\""
    section_string += self.image
    section_string += "\">\n"
    section_string += """
</body>
</html>
"""
    return section_string
