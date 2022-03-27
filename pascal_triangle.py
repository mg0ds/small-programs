def pascal(N):
    pascal_list = []
    if N == 0:
        return pascal_list
    else:
        for level in range(N):
            pascal_list.append([])
            if level == 0:
                pascal_list[0].append(1)
            elif level == 1:
                pascal_list[1].append(1)
                pascal_list[1].append(1)
            else:
                for poz in range(level+1):
                    if poz == 0:
                        pascal_list[level].append(1)
                    elif poz == level:
                        pascal_list[level].append(1)
                    else:
                        pascal_list[level].append(pascal_list[level-1][poz-1] + pascal_list[level-1][poz])
            #all elements
            #print(pascal_list)
        #only last element:
        print(pascal_list[N-1])
        return pascal_list[N-1]
