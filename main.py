# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_book():
    thisfile = open("splayout.tex", 'w')
    print_preamble(thisfile)
    print_begin(thisfile)
    land1 = 'landscape.jpg'
    land2 = 'landscape.jpg'
    port1 = 'portrait.jpg'
    port2 = 'portrait.jpg'
    port3 = 'portrait.jpg'
    port4 = 'portrait.jpg'
    capt_l1 = 'CAPTION L1'
    capt_l2 = 'CAPTION L2'
    capt_p1 = 'CAPTION P1'
    capt_p2 = 'CAPTION P2'
    capt_p3 = 'CAPTION P3'
    capt_p4 = 'CAPTION P4'
    print_ll(thisfile,land1,land2,capt_l1,capt_l2)
    print_l(thisfile,land1,capt_l1)
    print_pppp(thisfile,port1,port2,port3,port4,capt_p1,capt_p2,capt_p3,capt_p4)
    print_ppp(thisfile,port1,port2,port3,capt_p1,capt_p2,capt_p3)
    print_pp(thisfile,port1,port2,capt_p1,capt_p2)
    print_p(thisfile,port1,capt_p1)
    print_ppl(thisfile,port1,port2,land1,capt_p1,capt_p2,capt_l1)
    print_lpp(thisfile,land1,port1,port2,capt_l1,capt_p1,capt_p2)
    print_pl(thisfile,port1,land1,capt_p1,capt_l1)
    print_lp(thisfile,land1,port1,capt_l1,capt_p1)
    print_end(thisfile)
    thisfile.close()

def print_preamble(thisfile):
    thisfile.write('\\documentclass[10pt,letterpaper]{article}\n')
    thisfile.write('\\usepackage[top=1in, bottom=1in, left=0.5in, right=0.5in, paperwidth=8.5in, paperheight=11in]{geometry}\n')
    thisfile.write("\\usepackage{amsfonts,amssymb,amsmath}\n")
    thisfile.write("\\usepackage{graphicx}\n")
    thisfile.write("\\usepackage{float}\n")
    thisfile.write("\\setlength{\parindent}{0pt}")

def print_begin(thisfile):
    thisfile.write('\\begin{document}\n')

def print_end(thisfile):
    thisfile.write('\\end{document}\n')

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_book()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
