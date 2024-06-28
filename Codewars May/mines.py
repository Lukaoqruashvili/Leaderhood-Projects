def mine_location(field):
    x = 0
    for i in field:
        if 1 in i:
            return [x, i.index(1)]
        x += 1