def test_update_car_success(client):
    # 先创建车辆
    create_payload = {"make":"Mazda","model":"CX5","year":2020,"color":"Red"}
    resp_create = client.post("/api/cars", json=create_payload)
    car_id = resp_create.json()["id"]

    # PUT更新车辆信息
    update_payload = {"make":"Mazda","model":"CX5","year":2021,"color":"Dark Red"}
    resp_update = client.put(f"/api/cars/{car_id}", json=update_payload)
    assert resp_update.status_code == 200
    updated = resp_update.json()
    assert updated["year"] == 2021
    assert updated["color"] == "Dark Red"

def test_update_non_exist_car_returns_404(client):
    payload = {"make":"Test","model":"NotFound","year":2020,"color":"Blue"}
    resp = client.put("/api/cars/99999", json=payload)
    assert resp.status_code == 404
