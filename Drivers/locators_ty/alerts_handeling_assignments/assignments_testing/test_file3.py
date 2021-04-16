import pytest

class TestExample:


    @pytest.mark.parametrize("a", [1,2,3,4])
    def test_add(self,a):
        assert a+2==3, "not equal to 3"

    @pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
    def test_add(self, a,b):
        assert a%b==0


