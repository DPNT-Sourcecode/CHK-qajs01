from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        # Edge cases
        assert checkout_solution.checkout("Da") == -1
        assert checkout_solution.checkout("") == 0
        # Basic
        assert checkout_solution.checkout("ABCD") == 115
        # Multi buy
        assert checkout_solution.checkout("AAAAB") == 210
        assert checkout_solution.checkout("AAAAAAB") == 280
        assert checkout_solution.checkout("BBBC") == 95
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("VVVVV") == 220
        # Cross bundle
        assert checkout_solution.checkout("EE") == 80
        assert checkout_solution.checkout("EEEBB") == 150
        assert checkout_solution.checkout("EEEBBB") == 165
        # Single bundle
        assert checkout_solution.checkout("AFFFFF") == 90
        assert checkout_solution.checkout("UUUUU") == 160
        # New price
        assert checkout_solution.checkout("KKK") == 190
        # Group buy
        assert checkout_solution.checkout("STXYZ") == 82
        assert checkout_solution.checkout("STXYZS") == 90
        assert checkout_solution.checkout("ST") == 40
        assert checkout_solution.checkout("ZX") == 38
        assert checkout_solution.checkout("ZZZZ") == 66
        assert checkout_solution.checkout("ZZZS") == 65
        assert checkout_solution.checkout("SSSZ") == 65
        assert checkout_solution.checkout("STXS") == 62





