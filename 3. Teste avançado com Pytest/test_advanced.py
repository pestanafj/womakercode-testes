import pytest
import os


def str_to_bool(string):
    if string.lower() in ["yes", "y", "1"]:
        return True
    elif string.lower() in ["no", "n", "0"]:
        return False


@pytest.mark.parametrize("string", ["Y", "y", "1", "YES"])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True


@pytest.mark.parametrize("string", ["N", "n", "0", "NO"])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False


@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath

    return write


class TestFile:

    def test_f(self, tmpfile):
        path = tmpfile()
        with open(path) as _f:
            contents = _f.read()
        assert contents == "1"

    # def setup(self):
    #     with open("/tmp/done", 'w') as _f:
    #         _f.write("1")

    # def teardown(self):
    #     try:
    #         os.remove("/tmp/done")
    #     except OSError:
    #         pass

    # def test_done_file(self):
    #     with open("/tmp/done") as _f:
    #         contents = _f.read()
    #     assert contents == "1"



#   Etapa 2 – Executar os testes e explorar o relatório:
# Após adicionar testes, a próxima etapa é executar pytest e inspecionar a saída. Use o sinalizador de detalhamento maior (-v) para ver todos os valores de entrada tratados como um teste separado.


Pichau@Mariama MINGW64 ~ (add-my-user-Mariamapereira)
$ pytest -v test_code.py
================================================================================= test session starts =================================================================================
platform win32 -- Python 3.12.1, pytest-8.0.2, pluggy-1.4.0 -- C:\Users\Pichau\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Pichau
collected 9 items

test_code.py::test_str_to_bool_true[Y] PASSED                                                                                                                                    [ 11%]
test_code.py::test_str_to_bool_true[y] PASSED                                                                                                                                    [ 22%] 
test_code.py::test_str_to_bool_true[1] PASSED                                                                                                                                    [ 33%] 
test_code.py::test_str_to_bool_true[YES] PASSED                                                                                                                                  [ 44%] 
test_code.py::test_str_to_bool_false[N] PASSED                                                                                                                                   [ 55%]
test_code.py::test_str_to_bool_false[n] PASSED                                                                                                                                   [ 66%] 
test_code.py::test_str_to_bool_false[0] PASSED                                                                                                                                   [ 77%] 
test_code.py::test_str_to_bool_false[NO] PASSED                                                                                                                                  [ 88%] 
test_code.py::TestFile::test_file_contents PASSED                                                                                                                                [100%] 

================================================================================== 9 passed in 0.03s ================================================================================== 







