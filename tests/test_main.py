"""
MIT License

Copyright (c) 2024 Christopher Atkinson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root_valid_request_correct_response():
    """
    Test the root endpoint ("/") of the FastAPI application.

    This test performs the following checks:
    1. Sends a GET request to the root URL ("/").
    2. Asserts that the response status code is 200 OK.
    3. Asserts that the response JSON matches the expected structure:
       - "message": A welcome message ("Hello World").
       - "version": The API version ("1.0.0").
       - "routers": A dictionary of additional routes configured in the app,
         excluding the root path ("/").

    The test dynamically generates the expected "routers" dictionary based on
    the actual routes present in the FastAPI application, starting from the 5th
    route (index 4) to skip the default routes added by FastAPI.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello World",
        "version": "1.0.0",
        "routers": {route.name: route.path for route in app.routes[4:] if route.path != "/"}
    }
