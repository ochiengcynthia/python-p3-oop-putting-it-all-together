
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            # print("size must be an integer")
            raise ValueError("size must be an integer")
        else:
            self.size = size

    def cobble(self):
        print("The shoe has been repaired.")
        self.condition = 'New'


class TestShoe:
    def test_requires_int_size(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "size must be an integer"

    def test_can_cobble(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "Your shoe is as good as new!"

    def test_cobble_makes_new(self):
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()
        assert stan_smith.condition == 'New'
