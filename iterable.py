def count(sequence,item):
    counter = 0
    for mem in sequence:
        print mem
        if(item == mem):
            counter+=1
    return counter

print count([1],7)
