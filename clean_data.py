def read():
    with open('locations.list', encoding='UTF-8') as file:
        data = file.read().splitlines()
    return data

def clean(data):
    with open('new_locations', 'w',encoding='UTF-8') as file:
        names = set()
        for row in data:
            if '{' not in row:
                if ord(row[0]) in range(65, 91):
                    if row.count('(') == 1:
                        year = row.find('(')
                        name = row[:year].strip()
                        if name in names:
                            continue
                        else:
                            names.add(name)
                        if row[year+1:year+4].isnumeric():
                            if ',' in row:
                                if 'Federal' not in row:
                                    tf = False
                                    for chr in row:
                                        if ord(chr) > 127:
                                            tf = True
                                    if not tf:
                                        file.write(row)
                                        file.write('\n')

clean(read())