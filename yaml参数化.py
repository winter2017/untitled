import yaml
import pytest

class Demo2:
    @pytest.mark.parametrize("a,b",[(2,3),(4,5)])
    def test_case001(a,b):
        print(a+b)

if __name__ == "__main__":
    pytest.main(["-v","-s"])



