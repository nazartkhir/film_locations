"""
This module cleanes the data from locations.list
"""

def read():
    """
    Read data from locations.list
    """
    with open('locations.list', encoding='UTF-8') as file:
        data = file.read().splitlines()
    return data

def clean_and_write(data):
    """
    Clean the data in order to make a smaller dataset
    """
    ans = []
    locations = set()
    names = set()
    for row in data:
        if '{' in row or 'Federal' in row or ',' not in row:
            continue
        if row.count('(') != 1:
            continue
        if ord(row[0]) not in range(65, 91):
            continue
        year = row.find('(')
        loc = row[year + 6:].strip()
        name = row[:year].strip()
        if name in names:
            continue
        names.add(name)
        if loc in locations:
            continue
        locations.add(loc)
        if row[year+1:year+4].isnumeric():
            if row.find(')') - row.find('(') == 5:
                t_f = False
                for char in row:
                    if ord(char) > 127:
                        t_f = True
                if not t_f:
                    ans.append(row)
    with open("new_locations.csv", 'w', encoding='UTF-8') as file:
        for row in ans:
            first = row.find('(')
            last = row.find(')')
            name = row[:first].strip()
            year = row[first + 1:last]
            address = row[last + 1:].strip()
            file.write(f'{name}|{year}|{address}\n')

clean_and_write(read())
