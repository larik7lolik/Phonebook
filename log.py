from datetime import datetime

def log_file(surname,  name, number_telephon,  comment, text_orientation):
    if text_orientation == '1':
        with open('vertical.csv', 'a') as file:
             file.write(f'{datetime.today()}\n{surname}\n{name}\n{number_telephon}\n{comment}\n\n')
           
    if text_orientation == '2':
        with open('horizontal.csv', 'a') as file:
             file.write(f'{datetime.today()}; {surname}; {name}; {number_telephon};{comment};\n\n')
            