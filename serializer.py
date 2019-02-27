import json
from collections import namedtuple
from functools import reduce
import xml.etree.cElementTree as ET


class Output:
    def __init__(self, data):
        self.SumResult = "{:.2f}".format(sum(data.Sums) * data.K)
        self.MulResult = reduce(lambda x, y: x * y, data.Muls)
        sorted_inputs = data.Sums
        sorted_inputs.extend(data.Muls)
        sorted_inputs.sort()
        self.SortedInputs = sorted_inputs


def parse_json(json_object):
    data = json.loads(json_object, object_hook=lambda x: namedtuple('input', x.keys())(*x.values()))
    output = json.dumps(Output(data).__dict__)
    return output


def parse_xml(xml_object):
    input_root = ET.fromstring(xml_object)
    sums = []
    muls = []
    values = []
    K = input_root.find("K").text
    for value in input_root.find("Sums"):
        sums.append(float(value.text))
    for value in input_root.find("Muls"):
        muls.append(int(value.text))
    values.extend(muls)
    values.extend(sums)
    values.sort()
    muls = reduce(lambda x, y: float(x) * float(y), muls)
    sums = sum(sums) * int(K)
    output_root = ET.Element('Output')
    form_xml_tree(output_root, sums, muls, values)
    return ET.tostring(output_root, encoding='unicode').replace('"', "")


def form_xml_tree(root, sum_result, mul_result, sorted_inputs):
    SumResult = ET.Element('SumResult')
    SumResult.text = "{:.2f}".format(sum_result)
    root.append(SumResult)

    MulResult = ET.Element('MulResult')
    MulResult.text = str(mul_result)
    root.append(MulResult)

    SortedInputs = ET.Element('SortedInputs')
    for val in sorted_inputs:
        el = ET.Element('decimal')
        el.text = str(val)
        SortedInputs.append(el)
    root.append(SortedInputs)
