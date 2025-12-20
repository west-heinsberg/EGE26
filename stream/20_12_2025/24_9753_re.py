from re import finditer

with open("../../files/24_9753.txt") as file:
    data = file.readline()

pattern = r'(?<=Y)([^Y]*Y){150}[^Y]*(?=Y)'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))
#слишком много наложений, не решается ре-ми, замена единсвтенный оковый метод