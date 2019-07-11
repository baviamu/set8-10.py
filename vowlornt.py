nmbr = input()
key = 'aeiou'
for x in key:
    if x in nmbr:
        nmbr = ''
        break
    else:
        continue
if nmbr == '':
    print('yes')
else:
    print('no')
