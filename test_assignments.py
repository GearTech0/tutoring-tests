import importlib
import unittest
import argparse
import sys

parser = argparse.ArgumentParser(description='Testing for week 2 solutions')
parser.add_argument('--module', default=None, type=str, help='optional module name to test')
parser.add_argument('unittestargs', nargs='*')
args = parser.parse_args()

class TestAssignment2(unittest.TestCase):
    def test_Question1(self):
        self.assertEqual(solution_week2.question1([1, 2, 3]), 3)
        self.assertEqual(solution_week2.question1([65, 38, 2]), 65)
        self.assertEqual(solution_week2.question1([]), float('-inf'))
        self.assertEqual(solution_week2.question1([40]), 40)

    def test_question2(self):
        self.assertEqual(solution_week2.question2(4, [1, 2, 3, 4]), '4 occurs in the list')
        self.assertEqual(solution_week2.question2('', [1, 'se', 3, 7]), ' does not occur in the list')
        self.assertEqual(solution_week2.question2('deeep', ['dee', 'deep', 'deeep']), 'deeep occurs in the list')

    def test_question3(self):
        self.assertEqual(solution_week2.question3([1, 2, 3]), [1, 3])
        self.assertEqual(solution_week2.question3(['boop']), ['boop'])
        self.assertEqual(solution_week2.question3([1, 2, 3, 4]), [1, 3])

    def test_question4(self):
        self.assertEqual(solution_week2.question4([1, 2], [1, 2]), [1, 2, 2, 4])
        self.assertEqual(solution_week2.question4([], [1, 2, 3]), [])
    
    def test_question5(self):
        self.assertEqual(solution_week2.question5(["b", "o", "b", "b", "y"]), ["y", "b", "b", "o", "b"])
        self.assertEqual(solution_week2.question5([1]), [1])
        self.assertEqual(solution_week2.question5([]), [])

        if solution_week2.question5:
            self.assertEqual(solution_week2.question5(["b", "o", "b", "b", "y"]), ["y", "b", "b", "o", "b"])
            self.assertEqual(solution_week2.question5([1]), [1])
            self.assertEqual(solution_week2.question5([]), [])

if __name__ == '__main__':
    solution = 'solution'
    if args.module:
        solution = args.module
    solution_week2 = importlib.import_module(solution)
        
    sys.argv[1:] = args.unittestargs
    unittest.main()