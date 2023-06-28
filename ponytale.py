def ponytale(des):
    count = 0
    for d, e in des:
        if d == e:
            count += 1
    if count >= 3:
        print("OK")
    print("NG")
