
# content of test_expectation.py
import pytest



@pytest.mark.parametrize("nombreFichero", ["datos","imagen.txt","texto.jpg","wally.bmp"])
def test_imagen(nombreFichero):
    
    assert nombreFichero.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
