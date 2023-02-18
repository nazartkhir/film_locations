def read():
    with open('locations.list', encoding='UTF-8') as file:
        data = file.read().splitlines()
    return data

def clean(data):
    with open('new_locations.txt', 'w',encoding='UTF-8') as file:
        locations = set()
        for row in data:
            if '{' not in row:
                if ',' in row:
                    if ord(row[0]) in range(65, 91):
                        if row.count('(') == 1:
                            year = row.find('(')
                            loc = row[year + 6:].strip()
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
                                            file.write(row)
                                            file.write('\n')
clean(read())