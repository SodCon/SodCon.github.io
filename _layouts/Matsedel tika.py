from tika import parser
import re

raw = parser.from_file('Matsedel.pdf')

# Convert to string
text = str(raw['content'])

content = text.split('\n')
filtered = filter(lambda x: not re.match(r'^\s*$', x), content)
dagar = ['Måndagens', 'Tisdagens', 'Onsdagens', 'Torsdagens', 'Fredagens']
meny = {}

for word in filtered:
    for i in range(5):
        if dagar[i] in word:
            dag = dagar[i]
            dag = dag[:-3]
            meny[dag] = word.strip().split(':')[1].strip()


#print(meny)
with open('default.html', 'r') as f:
    contents = f.readlines()

for i, line in enumerate(contents):
    if '<div class="lunch1">' in line:
        new_line = '<div class="lunch1">'
        new_line = new_line + meny['Måndag']
        new_line += '</div></div>\n'
        contents[i] = new_line
    elif '<div class="lunch2">' in line:
        new_line = '<div class="lunch2">'
        new_line = new_line + meny['Tisdag']
        new_line += '</div></div>\n'
        contents[i] = new_line
    elif '<div class="lunch3">' in line:
        new_line = '<div class="lunch3">'
        new_line = new_line + meny['Onsdag']
        new_line += '</div></div>\n'
        contents[i] = new_line
    elif '<div class="lunch4">' in line:
        new_line = '<div class="lunch4">'
        new_line = new_line + meny['Torsdag']
        new_line += '</div></div>\n'
        contents[i] = new_line
    elif '<div class="lunch5">' in line:
        new_line = '<div class="lunch5">'
        new_line = new_line + meny['Fredag']
        new_line += '</div></div>\n'
        contents[i] = new_line

f = open('default.html', 'w')
f.write("".join(contents))
f.close()
