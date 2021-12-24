temperatura = int(input('Podaj temperature:'))
bardzo_cieplo = 30
cieplo = 22
# neutralnie jest miedzy zimno a cieplo
zimno = 5
bardzo_zimno = -10
max_cieplo = 50
max_zimno = -50

if temperatura > max_cieplo or temperatura < max_zimno:
    print('Temperatura jest nieprawidlowa')
else:
    if temperatura >= cieplo:
        if temperatura >= bardzo_cieplo:
            print('Na dworzu jest bardzo cieplo.')
        else:
            print('Na dworzu jest cieplo.')
    elif temperatura <= zimno:
        if temperatura <= bardzo_cieplo:
            print('Na dworzu jest bardzo zimno.')
        else:
            print('Na dworzu jest zimno.')
    else:
        print('Na dworzu jest neutralnie')
