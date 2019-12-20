import unittest

import helpers
from op import op, run


class Tests(unittest.TestCase):
    def test_run(self):
        self.assertEqual([2, 0, 0, 0], run([[1, 0, 0, 0], ]))
        self.assertEqual([2, 3, 0, 6], run([[2, 3, 0, 3], ]))
        self.assertEqual(
            [2, 4, 4, 5, 99, 9801],
            run(helpers.get_instruction_set([2, 4, 4, 5, 99, 0]))
        )
        self.assertEqual(
            [30, 1, 1, 4, 2, 5, 6, 0, 99],
            run(helpers.get_instruction_set([1, 1, 1, 4, 99, 5, 6, 0, 99])),
        )
