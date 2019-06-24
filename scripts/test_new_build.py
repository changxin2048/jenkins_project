import os
import sys

sys.path.append(os.getcwd())

class Test01:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_new(self):
        assert 1
