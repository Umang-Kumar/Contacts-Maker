# First in fh open the csv file to read.
fh = open('C:/Uabc/Usdg/Cfghjk/Contact Information.csv', 'r')

# After that open the vcf file to write.
fh1 = open('C:/Uabc/Usdg/Cfghjk/Contact Information.vcf', 'w')

for i in fh:
    # Get rid of starting and trailing spaces.
    i = i.strip()
    i = i.replace('\"', '')
    # Below line removes the first line of the csv file the column-specifiers.
    if i.find('Timestamp') != -1:
        pass
    else:
        i = i.split(',')
        # i[0] = 'Aitian 21'
        # if i[4].endswith('@aitpune.edu.in'):
        fh1.write('BEGIN:VCARD\n')
        fh1.write('VERSION:3.0\n')
        fh1.write('FN:' + ' ' + i[1].title() + ' ' + '\n')
        fh1.write('item1.TEL:' + i[4] + '\n')
        fh1.write('item1.X-ABLabel:Mobile\n')
        fh1.write('item2.EMAIL;type = INTERNET:' + i[2] + '\n')
        fh1.write('item2.X-ABLabel: Work\n')
        fh1.write('END:VCARD\n')

fh.close()
fh1.close()
