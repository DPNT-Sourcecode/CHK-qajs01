from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout("Da") == -1
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AAAAAAB") == 280
        assert checkout_solution.checkout("BBBC") == 95
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEEBB") == 150
        assert checkout_solution.checkout("EEEBBB") == 165
        assert checkout_solution.checkout("AFFFFF") == 90
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("KKK") == 190
        assert checkout_solution.checkout("STXYZ") == 86


