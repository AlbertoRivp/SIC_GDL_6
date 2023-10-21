f = open("test.txt", 'r')
print("readLine() method")
print(f.readline())
print(f.readline())
f.close()


f = open("test.txt", 'r')
print("readLines() method")
lines = f.readline()
for line in lines:
    print(line.strip())
f.close()


f = open("test.txt", 'r')
print("read() method")
data = f.read()
print(data)
f.close()