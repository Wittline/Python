import math
import unittest
import csv


class directory:
    def __init__(self, n, e, a, c):
        self.Name = n
        self.Email = e
        self.Age = a
        self.Country = c


class ManageDirectory:
    def __init__(self, filename):
        self.myList = []
        self.myFile = filename

    def setFile(self, filename):
        self.myFile = filename

    def load_from_file(self):
        try:
            li = []
            with open(self.myFile) as f:
                reader = csv.reader(f)
                data = [r for r in reader]
                data.pop(0)
                for r in data:
                    li.append(directory(r[0], r[1], r[2], r[3]))
                self.myList = li
            return True
        except:
            return False

    def saveToCSVFile(self):
        with open(self.myFile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Email', 'Age', 'Country'])
            for r in self.myList:
                writer.writerow([r.Name, r.Email, r.Age, r.Country])

    def add(self, e):
        if e is None:
            return False
        try:
            self.myList.append(e)
            li.saveToCSVFile()
            return True
        except:
            return False

    def remove(self, i):
        if (i <= 1):
            return False
        try:
            self.myList.pop(i-1)
            li.saveToCSVFile()
            return True
        except:
            return False

    def lookBy_email_age(self, e, a):
        match = []
        for r in self.myList:
            if((e in r.Email) and (a == r.Age)):
                match.append(r)
        return match

    def show_list(self):
        return self.myList

li = ManageDirectory('test.csv')

# if the file  already contains  data you can use this method
# li.load_from_file(); #
# If there is no data in the file or it does not exist you can
# add records to the file in this way
li.add(directory("Ram1", "ram1@hotmail.com", "3", "Mexico"))
li.add(directory("Ram2", "ram2@hotmail.com", "2", "Mexico"))
li.add(directory("Ram3", "ram3@hotmail.com", "7", "Mexico"))
li.add(directory("Ram4", "ram4@hotmail.com", "5", "Mexico"))
li.add(directory("Ram", "ram@hotmail.com", "5", "Mexico"))
l = li.show_list()
for row in l:
    print(row.Name, row.Email, row.Age, row.Country)

print("----------Removing record 1--------------------")
li.remove(1)
l = li.show_list()
for row in l:
    print(row.Name, row.Email, row.Age, row.Country)

print("----------Searching record by email and age--------------------")
res = li.lookBy_email_age('ram4@hotmail.com', '5')
for row in res:
    print(row.Name, row.Email, row.Age, row.Country)

print("----------Showing all the records--------------------")
l = li.show_list()
for row in l:
    print(row.Name, row.Email, row.Age, row.Country)


class My_tests(unittest.TestCase):

    li = ManageDirectory('test.csv')

    def test_ceil_positive(self):
        res = math.ceil(2.25)
        self.assertEqual(3, res)

    def test_ceil_negative(self):
        res = math.ceil(-2.25)
        self.assertEqual(-2, res)

    def test_factorial_zero(self):
        res = math.factorial(0)
        self.assertEqual(1, res)

    def test_factorial(self):
        res = math.factorial(5)
        self.assertEqual(120, res)

    def test_pow(self):
        res = math.pow(2, 2)
        self.assertEqual(4, res)

    def test_loading_records(self):
        res = li.load_from_file()
        self.assertTrue(res)

    def test_loading_records_fail(self):
        li.setFile('')
        res = li.load_from_file()
        self.assertFalse(res)

    def test_adding_record(self):
        res = li.add(directory('testname',
                               'testemail@hotmail.com',
                               '20', 'Mex'))
        self.assertTrue(res)

    def test_adding_record2(self):
        res = li.add(directory('testname2',
                               'testemail2@hotmail.com',
                               '25', 'USA'))
        self.assertTrue(res)

    def test_adding_record3(self):
        res = li.add(directory('testname3',
                               'testemail3@hotmail.com',
                               '22', 'Arg'))
        self.assertTrue(res)

    def test_adding_record_fail(self):
        res = li.add(None)
        self.assertFalse(res)

    def test_removing_record(self):
        li.setFile('test.csv')
        res = li.remove(2)
        self.assertTrue(res)

    def test_removing_record_fail(self):
        res = li.remove(0)
        self.assertFalse(res)

    def test_searching_record(self):
        res = li.lookBy_email_age('testemail3@hotmail.com', '22')
        self.assertEqual(True, len(res) > 0)

    def test_searching_no_record(self):
        res = li.lookBy_email_age('testemail4@gmail.com', '22')
        self.assertEqual(False, len(res) > 0)

if __name__ == '__main__':
    unittest.main()