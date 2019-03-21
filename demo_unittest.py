from fileHandler import PrintClass
import unittest
# Happy day scenario : done
# Exceptions and edge cases : done


class TestDataExtraction(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.test_class = PrintClass('classDiagram.txt')

    #def tearDown(self):
        # be executed after each test case
        #print('down')

    def test_get_class_name(self):
        list_1 = ['class a {\n', '    n : String\n', '    add()\n', '}\n']
        list_2 = ['class  {\n', '    n : String\n', '    add()\n', '}\n']
        list_3 = ['    name : String\n', '    add_attributes()\n', '}\n']
        self.assertEqual(self.test_class.get_class_name(list_1), 'a')
        self.assertEqual(self.test_class.get_class_name(list_2), '')
        self.assertIsNone(self.test_class.get_class_name(list_3))

    def test_02(self):
        print(2)
        self.x = 6
        self.assertEqual(6, 3 * 2)

    @unittest.skip('I have not coded how this will work yet.')
    def test_01(self):
        print(1)
        self.assertTrue(None is 42)
        self.x = 666


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()