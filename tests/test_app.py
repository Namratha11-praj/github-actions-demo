import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app, calculate_result

def test_calculate_result_pass():
    total, average, result = calculate_result(80, 70, 90)
    assert total == 240
    assert average == 80
    assert result == "PASS"


def test_calculate_result_fail():
    total, average, result = calculate_result(20, 30, 25)
    assert total == 75
    assert average == 25
    assert result == "FAIL"


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Result Application" in response.data


def test_result_page():
    client = app.test_client()
    response = client.post(
        "/result",
        data={
            "name": "Rahul",
            "mark1": "80",
            "mark2": "70",
            "mark3": "90"
        }
    )
    assert response.status_code == 200
    assert b"Rahul" in response.data
    assert b"PASS" in response.data


def test_result_page_fail():
    client = app.test_client()
    response = client.post(
        "/result",
        data={
            "name": "Priya",
            "mark1": "20",
            "mark2": "30",
            "mark3": "25"
        }
    )
    assert response.status_code == 200
    assert b"FAIL" in response.data
