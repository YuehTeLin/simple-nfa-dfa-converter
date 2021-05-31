import sys
import csv
import re

input = {}

output = {}

def removeCommasAndCurlyBrackets(str1):
    return re.sub(r'[,{}]', '', str1)

def buildInputDictionary(csvreader):
    for row in csvreader:
        splitRow = re.split('\,(?![^{}]*\})' ,row[0])
        mapRow = map(removeCommasAndCurlyBrackets, splitRow)
        listRow = list(mapRow)
        key = listRow[0]
        value = listRow[1:]
        input[key] = value
        
def unique(list1):
    listSet = set(list1)
    uniqueList = (list(listSet))
    return uniqueList
    
def getNodeValue(node):
    s = node.split('s')[1:]
    n = list(map(lambda x: 's' + x, s))
    length = 0
    for node in n:
        length = len(input[node])
    result = [ [] for i in range(length) ]
    for i in range(length):
        for node in n:
            result[i].append(input[node][i])
    answer = []
    for res in result:
        s = ''.join(res)
        numStr = s.split('s')[1:]
        nums = list(map(lambda x: int(x), numStr))
        nums.sort()
        u = unique(nums)
        us = list(map(lambda x: 's' + repr(x), u))
        ans = ''.join(us)
        answer.append(ans)
    return answer

def buildOutputDictionary(value):
    queue = []
    for node in value:
        queue.append(node)
    while queue:
        x = queue.pop(0)
        if x not in output:
            print('STATE => ', x)
            nodeValue = getNodeValue(x)
            output[x] = nodeValue
            for node in nodeValue:
                queue.append(node)

def main():
    fileName = sys.argv[1] if len(sys.argv) > 1 else 'import_data.csv'
    with open(fileName, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')
        headers = next(csvreader)
        buildInputDictionary(csvreader)
        print('INPUT MAP => ', input)
        firstKVPair = list(input.items())[0]
        key = firstKVPair[0]
        value = firstKVPair[1]
        output[key] = value
        buildOutputDictionary(value)
        print('OUTPUT MAP => ', output)
        header = headers[0].split(',')
        with open('export_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for node in output:
                row = []
                row.append(node)
                for node in output[node]:
                    row.append(node)
                writer.writerow(row)

if __name__ == "__main__":
    main()