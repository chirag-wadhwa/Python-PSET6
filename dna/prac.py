def finder(x, y):
    d = x
    i = 0
    no = [0]
    while d.find(y) != -1:
        index = d.find(y)
        temp = d[index:]
        j = 0
        count = 0
        while j < len(temp):
            if temp[j:j+len(y)] == y:
                count += 1
                j += len(y)
            else:
                break
        no.append(count)
        d = temp[j:]

    no.sort(reverse=True)
    return(no[0])

