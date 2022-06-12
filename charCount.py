st = input("enter the string: ")
li = []
for i in range(len(st)):
    c = 1
    if i == 0:
        for j in range(i + 1, len(st)):
            if st[i] == st[j]:
                li.append(j)
                c += 1
        print(st[i], "occured", c, "this many times")
    else:
        if i in li:
            continue
        else:
            for j in range(i + 1, len(st)):
                if st[i] == st[j]:
                    li.append(j)
                    c += 1
            print(st[i], "occured", c, "this many times")
