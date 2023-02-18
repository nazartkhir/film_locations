def read():
    with open('locations.list', encoding='UTF-8') as file:
        data = file.read().splitlines()
    return data

def clean_and_write(data):
    ans = []
    locations = set()
    names = set()
    for row in data:
        if '{' not in row:
            if ',' in row:
                if ord(row[0]) in range(65, 91):
                    if row.count('(') == 1:
                        year = row.find('(')
                        loc = row[year + 6:].strip()
                        name = row[:year].strip()
                        if name in names:
                            continue
                        else:
                            names.add(name)
                        if loc in locations:
                            continue
                        else:
                            locations.add(loc)
                        if row[year+1:year+4].isnumeric():
                            if row.find(')') - row.find('(') == 5:
                                if 'Federal' not in row:
                                    tf = False
                                    for char in row:
                                        if ord(char) > 127:
                                            tf = True
                                    if not tf:
                                        ans.append(row)
    with open("new_locations.csv", 'w', encoding='UTF-8') as file:
        #file.write('name|year|address\n')
        for row in ans:
            first = row.find('(')
            last = row.find(')')
            name = row[:first].strip()
            year = row[first + 1:last]
            address = row[last + 1:].strip()
            file.write(f'{name}|{year}|{address}\n')
            
clean_and_write(read())