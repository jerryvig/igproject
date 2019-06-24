from django.test import TestCase

# Create your tests here.
class MyTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('In MyTestClass.setUpTestData() which is a class method.')
        pass

    def setUp(self):
        print('in MyTestClass.setUp()')
        pass

    def tearDown(self):
        print('in MyTestClass.tearDown()')

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(True)
