def main():
    with open('new_locations_wcords.csv', encoding='UTF-8') as file:
        data = file.read().splitlines()
        for i, row in enumerate(data):
            data[i] = row.split('|')
        final_data = []
        for row in data:
            tmp = [row[1], row[3], row[4]]
            if tmp not in final_data:
                final_data.append(tmp)
    
    with open('final_dataset.csv', 'w', encoding='UTF-8') as file:
        for row in final_data:
            file.write('|'.join(row))
            file.write('\n')

main()
    