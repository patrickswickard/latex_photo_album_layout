"""Script for spitting out covers to html for webpage"""
import re

for i in range(1,51):
  if i < 10:
    file = 'texfiles2/ctr_00' + str(i) + '.tex'
    print('<H2>VOLUME ' + str(i) + '</H2>')
    print('<P>')
    print('<img width="1920" src="images/fullcovers/fullcover_00' + str(i) + '.jpg">')
    print('Includes:')
    print('<UL>')
  else:
    file = 'texfiles2/ctr_0' + str(i) + '.tex'
    print('VOLUME ' + str(i))
    print('<P>')
    print('<img width="1920" src="images/fullcovers/fullcover_0' + str(i) + '.jpg">')
    print('Includes:')
    print('<UL>')
  with open(file,'r',encoding='utf-8') as myinfile:
    lines = myinfile.read().splitlines()


  section_list = []
  url_list = []

  # find and report
  for thisline in lines:
    section = re.search(r"section\*\{(.*)\}",thisline)
    url = re.search(r"url\{(.*)\}",thisline)
    if section:
      this_section = section.group(1)
      section_list.append(this_section)
    elif url:
      this_url = url.group(1)
      url_list.append(this_url)

  for mylist, mysection in zip(url_list,section_list):
    print('<LI><A HREF="' + mylist + '">' + mysection + '</A>')
  print('</UL>')
  print('<P>')
