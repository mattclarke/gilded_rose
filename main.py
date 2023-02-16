
class Test:
    def __init__(self, function):
        self.was_run = False

    def run(self):
        self.was_run = True

def test_test_is_run():
    test = Test(lambda: 123)
    test.run()
    assert test.was_run == True


if __name__ == "__main__":
    test_test_is_run()
