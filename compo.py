elt = int(input())
if elt > 2:
    for g in range(2, elt):
        if elt % g == 0:
            print('yes')
            break
    else:
        print('no')
elif elt == 2:
    print('no')
