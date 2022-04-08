import unittest

from Package1.TC_Iteractions_Test import Iteractions_Test
from Package2.TC_Widgets_Test import Widgets_Test

tc1 = unittest.TestLoader().loadTestsFromTestCase(Iteractions_Test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Widgets_Test)

functional_test_suit = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(functional_test_suit)
