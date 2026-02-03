# Yuhang Pan
# SoftDev 2026
# Continuous Integration DEMO

from app import app

def test_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 500
