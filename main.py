
class Collector:
    def __init__(self):
        self.tests = []
        self.num_passed = 0
        self.num_runs = 0
        self.results = ""

    def get_results(self):
        return self.results

    def add_test(self, test):
        self.tests.append(test)

    def run_tests(self):
        for test in self.tests:
            test.run()
            if test.passed:
                self.num_passed += 1
            self.num_runs += 1
        self.results = f"{self.num_passed} of {self.num_runs}"

class Test:
    def __init__(self, function):
        self.was_run = False
        self.passed = False
        self.function = function

    def run(self):
        try:
            self.function()
        except:
            pass
        else:
            self.passed = True
        self.was_run = True


def test_test_passes():
    test = Test(lambda: 123)
    test.run()
    assert test.passed

def test_test_fails():
    def _fails():
        raise RuntimeError()
    test = Test(_fails)
    test.run()
    assert not test.passed

def test_test_is_run():
    test = Test(lambda: 123)
    test.run()
    assert test.was_run == True

def test_can_collect_one_fail():
    collector = Collector()
    def _fails():
        raise RuntimeError()
    collector.add_test(Test(_fails))
    collector.run_tests()
    assert collector.num_passed == 0
    assert collector.num_runs == 1

def test_can_collect_one_pass():
    collector = Collector()
    collector.add_test(Test(lambda: 123))
    collector.run_tests()
    assert collector.num_passed == 1
    assert collector.num_runs == 1

def test_collector_can_print_results():
    collector = Collector()
    collector.add_test(Test(lambda: 123))
    collector.run_tests()
    results = collector.get_results()
    assert results == "1 of 1"

def test_collector_can_list_failed_tests():
    collector = Collector()
    def _fails():
        raise RuntimeError()
    
    def _passes():
        pass
    collector.add_test(Test(_fails))
    collector.add_test(Test(_passes))
    collector.run_tests()

    assert len(collector.failures) == 1
    assert "_fails" in collector.failures

if __name__ == "__main__":
    test_test_is_run()
    test_test_passes()
    test_test_fails()
    test_can_collect_one_fail()
    test_can_collect_one_pass()
    test_collector_can_print_results()
    test_collector_can_list_failed_tests()
