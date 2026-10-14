from app import database
from app.schemas import CarInput

def test_list_cars_return_all_saved_cars(database_path):
    database.initialize(database_path)
    # 一次性插入3台车
    database.create_car(database_path, CarInput(make="Honda", model="Fit", year=2021, color="Silver"))
    database.create_car(database_path, CarInput(make="Nissan", model="Altima", year=2022, color="White"))
    database.create_car(database_path, CarInput(make="Kia", model="Sportage", year=2023, color="Grey"))

    car_list = database.list_cars(database_path)
    assert len(car_list) == 3
    makes = [car.make for car in car_list]
    assert "Honda" in makes
    assert "Nissan" in makes
    assert "Kia" in makes

def test_list_empty_when_no_cars(database_path):
    database.initialize(database_path)
    car_list = database.list_cars(database_path)
    assert len(car_list) == 0
