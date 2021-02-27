import plazas, streets

def run():
    for i in plazas.getPlazas():
        yield i
    for i in streets.getStreets():
        yield i
