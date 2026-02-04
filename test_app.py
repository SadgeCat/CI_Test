# Yuhang Pan
# SoftDev 2026
# Continuous Integration DEMO

from app import app

# has `test` in the func name as well as file name for pytest to run
def test_page():
    client = app.test_client()      # emulates a browser without a live server to test your app
    response = client.get('/')      # this client can do get/post requests which returns a response which usually contains the status code and data
    # this assert keyword asserts that the statement is true, so if the statement turns out to be false, that means something went wrong, this is often used for testing
    assert response.status_code == 200      # status code 200 is a successful request so this checks if our apps, the routes work without errors
