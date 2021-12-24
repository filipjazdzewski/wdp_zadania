import uuid

def add_country(name, inhabitants):
    return {'id': str(uuid.uuid4()),
            'name': name,
            'inhabitants': inhabitants,
            'capitalId': None}

def add_city(name, inhabitants):
    return {'id': str(uuid.uuid4()),
            'name': name,
            'inhabitants': inhabitants}

def set_capital(country_name, country_db, city_name, city_name, city_db):
    country_record = None
    for country in country_db:
        if country['name'] == country_name:
            country_record = country
            break

    city_record = None
    for country in city_db:
        if city['name'] == city_name:
            city_record = country
            break

    return {'id': ['id'],
            'name': country_name,
            'inhabitants': inhabitants,
            'capitalId': None}
