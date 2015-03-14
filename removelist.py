def purify(num):
    for idx,item in enumerate(num):
        print item,idx
        if(item%2!=0):
            num.pop(idx)
            idx -=1
    return num

print purify([4,5,5,4])
