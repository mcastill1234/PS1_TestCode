from unittest import TestCase
import problem2D
import peak


class TestPeakProblem(TestCase):

    def setUp(self):
        self.testArray = problem2D.problemMatrix
        self.testProblem = peak.createProblem(self.testArray)

    def test_get(self):
        # Test for corners
        loc1 = (0, 0)
        loc2 = (0, len(self.testArray)-1)
        loc3 = (len(self.testArray[0])-1, 0)
        loc4 = (len(self.testArray)-1, len(self.testArray[0])-1)
        res1 = self.testArray[0][0]
        res2 = self.testArray[0][len(self.testArray)-1]
        res3 = self.testArray[len(self.testArray)-1][0]
        res4 = self.testArray[len(self.testArray)-1][len(self.testArray[0])-1]

        self.assertEqual(self.testProblem.get(loc1), res1)
        self.assertEqual(self.testProblem.get(loc2), res2)
        self.assertEqual(self.testProblem.get(loc3), res3)
        self.assertEqual(self.testProblem.get(loc4), res4)

        # Test location inside and outside of array
        loc5 = (25, 35)
        self.assertEqual(self.testProblem.get(loc5), 0)

        # Test location inside array
        loc6 = (2, 2)
        res6 = self.testArray[2][2]
        self.assertEqual(self.testProblem.get(loc6), res6)

    def test_getBetterNeighbor(self):
        self.assertEqual(self.testProblem.getBetterNeighbor((0, 0)), (1, 0))
        self.assertEqual(self.testProblem.getBetterNeighbor((2, 3)), (3, 3))
        self.assertEqual(self.testProblem.getBetterNeighbor((4, 4)), (4, 4))

    def test_getMaximum(self):
        locations = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertEqual(self.testProblem.getMaximum(locations), (3, 3))

    def test_isPeak(self):
        self.assertFalse(self.testProblem.isPeak((0, 0)))
        self.assertTrue(self.testProblem.isPeak((4, 4)))

    def test_getSubproblem(self):
        bounds1 = (0, 0, 6, 6)
        bounds2 = (0, 6, 5, 5)
        bounds3 = (6, 0, 6, 6)
        bounds4 = (6, 6, 5, 5)
        subProblem1 = self.testProblem.getSubproblem(bounds1)
        subProblem2 = self.testProblem.getSubproblem(bounds2)
        subProblem3 = self.testProblem.getSubproblem(bounds3)
        subProblem4 = self.testProblem.getSubproblem(bounds4)
        # print(subProblem1.get((0, 0)), subProblem1.get((0, 1)), subProblem1.get((0, 5)))
        # print(subProblem2.get((0, 0)), subProblem2.get((0, 1)), subProblem2.get((0, 4)))
        # print(subProblem3.get((0, 0)), subProblem3.get((0, 1)), subProblem3.get((0, 5)))
        # print(subProblem4.get((0, 0)), subProblem4.get((0, 1)), subProblem4.get((0, 4)))

        self.assertEqual(subProblem1.bounds, bounds1)
        self.assertEqual(subProblem2.bounds, bounds2)
        self.assertEqual(subProblem3.bounds, bounds3)
        self.assertEqual(subProblem4.bounds, bounds4)

    def test_getSubproblemContaining(self):
        bounds1 = (0, 0, 6, 6)
        bounds2 = (0, 6, 5, 5)
        bounds3 = (6, 0, 6, 6)
        bounds4 = (6, 6, 5, 5)
        testLoc1 = (2, 3)
        testLoc2 = (2, 8)
        testLoc3 = (8, 2)
        testLoc4 = (8, 8)
        boundList = [bounds1, bounds2, bounds3, bounds4]

        subProblem1 = self.testProblem.getSubproblemContaining(boundList, testLoc1)
        subProblem2 = self.testProblem.getSubproblemContaining(boundList, testLoc2)
        subProblem3 = self.testProblem.getSubproblemContaining(boundList, testLoc3)
        subProblem4 = self.testProblem.getSubproblemContaining(boundList, testLoc4)

        self.assertEqual(subProblem1.bounds, bounds1)
        self.assertEqual(subProblem2.bounds, bounds2)
        self.assertEqual(subProblem3.bounds, bounds3)
        self.assertEqual(subProblem4.bounds, bounds4)

    def test_getLocationInSelf(self):
        bounds3 = (6, 0, 6, 6)
        subProblem3 = self.testProblem.getSubproblem(bounds3)
        testloc3 = (2, 2)
        expectedLoc = (8, 2)
        resultLoc = self.testProblem.getLocationInSelf(subProblem3, testloc3)
        self.assertEqual(resultLoc, expectedLoc)



