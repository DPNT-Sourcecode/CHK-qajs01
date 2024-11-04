from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("BBBC") == 95


