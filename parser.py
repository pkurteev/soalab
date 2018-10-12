import json
import xml.etree.cElementTree as ET
from functools import reduce
from decimal import *


def parse_json(object):
    # object = '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}'
    json_obj = json.loads(object)
    sums = list(map(lambda x: Decimal(str(x)), json_obj["Sums"]))
    muls = json_obj["Muls"]
    K = Decimal(json_obj["K"])
    values = []
    values.extend(muls)
    values.extend(sums)
    return K, sums, muls, values


def do_task(k, sum_result, mul_result, values):
    sum_result = sum(sum_result) * k
    mul_result = reduce(lambda x, y: x * y, mul_result)
    sorted_vals = sorted(list(map(lambda x: float(x), values)))
    return sum_result, mul_result, sorted_vals


def form_json(sum_result, mul_result, sorted_vals):
    json_data = {}
    json_data['SumResult'] = str(sum_result)
    json_data['MulResult'] = float(mul_result)
    json_data['SortedInputs'] = sorted_vals
    json_data = json.dumps(json_data)
    print("Json")
    print(json_data)


def form_xml_tree(root, sum_result, mul_result, sorted_inputs):
    SumResult = ET.Element('SumResult')
    SumResult.text = str(sum_result)
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


def parse_xml(object):
    # object = "<Input><K>10</K><Sums><decimal>1.01</decimal><decimal>2.02</decimal></Sums><Muls><int>1</int><int>4</int></Muls></Input>"
    root = ET.fromstring(object)
    sums = []
    muls = []
    values = []
    K = Decimal(root.find("K").text)
    for dec in root.find("Sums"):
        sums.append(Decimal(dec.text))
    for int in root.find("Muls"):
        muls.append(Decimal(int.text))
    values.extend(muls)
    values.extend(sums)
    return K, sums, muls, values


def form_xml(sum_result, mul_result, sorted_vals):
    output_xml = ET.Element('Output')
    form_xml_tree(output_xml, sum_result, mul_result, sorted_vals)
    print("Xml")
    print(ET.tostring(output_xml, encoding='unicode'))


if __name__ == '__main__':
    object_type = input()
    object = input()
    if object_type == "Json":
        data = parse_json(object)
        data = do_task(*data)
        form_json(*data)
    else:
        data = parse_xml(object)
        data = do_task(*data)
        form_xml(*data)
