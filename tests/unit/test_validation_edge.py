import pytest
from app.schemas import CarInput
from pydantic import ValidationError

def test_car_year_min_boundary():
    # 合法最小年份边界
    car = CarInput(make="BMW", model="320i", year=1886, color="Black")
    assert car.year == 1886

def test_car_year_below_min_fails():
    # 低于下限1886，触发校验异常
    with pytest.raises(ValidationError):
        CarInput(make="BMW", model="320i", year=1885, color="Black")

def test_empty_color_allowed():
    # 颜色允许为空字符串
    car = CarInput(make="Audi", model="A4", year=2024, color="")
    assert car.color == ""