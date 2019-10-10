
# content of test_expectation.py
import pytest
import mimetypes
import requests




@pytest.mark.parametrize("url", ["https://images2.minutemediacdn.com/image/upload/c_fill,g_auto,h_1248,w_2220/f_auto,q_auto,w_1100/v1555285691/shape/mentalfloss/waldomain.png","https://miro.medium.com/max/1500/1*yO4EVVeBHYIrxKXDGY_-zw.jpeg"])
def test_imagen(url):
    response = requests.get(url, stream=True)
    assert response.headers['Content-Type'].split("/")[0] == "image"

