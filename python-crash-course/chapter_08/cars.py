def make_car(manufacturer, model, **car_infos):
    car_infos['manufacturer'] = manufacturer
    car_infos['model'] = model
    return car_infos

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)