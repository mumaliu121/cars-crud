from app import database
from app.schemas import CarInput

def test_saved_car_can_be_read_from_sqlite(database_path):
    database.initialize(database_path)
    saved = database.create_car(
        database_path,
        CarInput(make="Toyota", model="Yaris", year=2020, color="Blue")
    )
    loaded = database.get_car(database_path, saved.id)
    assert loaded is not None
    assert loaded.id == saved.id
    assert loaded.make == "Toyota"
    assert loaded.year == 2020

#自己编写集成测试：删除一台车不影响另一台
def test_deleting_one_car_keeps_the_other(database_path):
    database.initialize(database_path)
    car1 = database.create_car(database_path,CarInput(make="A",model="1",year=2020,color="red"))
    car2 = database.create_car(database_path,CarInput(make="B",model="2",year=2021,color="blue"))
    database.delete_car(database_path,car1.id)
    assert database.get_car(database_path,car1.id) is None
    rest_list = database.list_cars(database_path)
    assert len(rest_list) == 1
    assert rest_list[0].id == car2.id
