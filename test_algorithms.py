from unittest import TestCase
import problem2D
import peak
import algorithms
import generate


class TestAlgorithms(TestCase):

    def test_Algorithm1(self):
        for testNumber in range(10000):
            testArray = generate.randomProblem(10, 10, 1000)
            testProblem = peak.createProblem(testArray)
            testPeak = algorithms.algorithm1(testProblem)
            self.assertTrue(testProblem.isPeak(testPeak))

    def test_Algorithm2(self):
        for testNumber in range(10000):
            testArray = generate.randomProblem(10, 10, 1000)
            testProblem = peak.createProblem(testArray)
            testPeak = algorithms.algorithm2(testProblem)
            self.assertTrue(testProblem.isPeak(testPeak))



    def test_Algorithm3(self):
        for testNumber in range(10000):
            testArray = generate.randomProblem(10, 10, 1000)
            testProblem = peak.createProblem(testArray)
            testPeak = algorithms.algorithm3(testProblem)
            self.assertTrue(testProblem.isPeak(testPeak))


    def test_Algorithm4(self):
        for testNumber in range(10000):
            testArray = generate.randomProblem(10, 10, 1000)
            testProblem = peak.createProblem(testArray)
            testPeak = algorithms.algorithm4(testProblem)
            self.assertTrue(testProblem.isPeak(testPeak))

    def test_dummy(self):
        testArray = generate.randomProblem(10, 10, 100)