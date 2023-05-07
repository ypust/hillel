
conversion_rate = 37


with open('test_file.csv', 'r') as input_file:
    with open('salaries_uah.csv', 'w') as output_file:
        for line in input_file:
            columns = line.split(',')
            if columns[0] == '':
                output_file.write(line)
            else:
                salaries = [int(salary) * conversion_rate for salary in columns[1:]]
                output_file.write(f'{columns[0]},{",".join(str(salary) for salary in salaries)}\n')
