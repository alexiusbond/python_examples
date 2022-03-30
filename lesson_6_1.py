import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
print(result)

result = re.match(r'Analytics', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.findall(r'AV', text)
print(result)

result = re.split(r' ', text, 2)
print(result)

result = re.sub(r' ', ' - ', text)
print(result)

# result = re.findall(r'AV', text)
pattern = re.compile('AV')
result = pattern.findall(text)
print(result)

with open("test_regs.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

    print(re.findall(r'fruits\[\d\]', content))
    print(re.findall(r'log\d*\.txt', content))
