import unittest
import serializer as s
from decimal import *

k = 10
sums = [Decimal("1.01"), Decimal("2.02")]
muls = [1, 4]
values = [1.01, 1.0, 4.0, 2.02]
data = [k, sums, muls, values]
mul_result = 4
sum_result = "30.30"
sorted_values = [1.0, 1.01, 2.02, 4.0]

json_incoming = '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}'
json_expected = '{"SumResult":"30.30","MulResult":4,"SortedInputs":[1.0,1.01,2.02,4.0]}'

xml_incoming = '<Input><K>10</K><Sums><decimal>1.01</decimal><decimal>2.02</decimal></Sums><Muls><int>1</int><int>4</int></Muls></Input>'
xml_expected = '<Output><SumResult>30.30</SumResult><MulResult>4</MulResult><SortedInputs><decimal>1.0</decimal><decimal>1.01</decimal><decimal>2.02</decimal><decimal>4.0</decimal></SortedInputs></Output>'


class Test(unittest.TestCase):
    def test_do_task(self):
        self.assertEqual(["30.30", 4, [1.0, 1.01, 2.02, 4.0]], s.do_task(*data))

    def test_form_json(self):
        self.assertEqual(json_expected, s.form_json(sum_result, mul_result, sorted_values))

    def test_parse_json(self):
        self.assertEqual([Decimal(10),  # K
                          [Decimal('1.01'), Decimal('2.02')],  # sums
                          [1, 4],  # muls
                          [1, 4, Decimal('1.01'), Decimal('2.02')]],  # values
                         s.parse_json(json_incoming))

    def test_parse_xml(self):
        self.assertEqual([Decimal(10),  # K
                          [Decimal('1.01'), Decimal('2.02')],  # sums
                          [1, 4],  # muls
                          [1, 4, Decimal('1.01'), Decimal('2.02')]],  # values
                         s.parse_xml(xml_incoming))

    def test_form_xml(self):
        self.assertEqual(xml_expected, s.form_xml(sum_result, mul_result, sorted_values))


if __name__ == '__main__':
    unittest.main()
