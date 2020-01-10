import pyperclip

text = pyperclip.paste().split('\n')
for x in text: 
    row = x.split(',')
    print('|', end='')
    for y in row:
        print(y.center(50, ' '), '|', end='')
    print('|')

"""
Good/Service, Market Event(s), D, S, P, Q
Video Cassettes Recorders (VCRs), Technological advances reduce the cost of DVD players. Public expects a future in which movies can be downloaded directly onto computers from the Internet, Inc, Inc, Dec
"""