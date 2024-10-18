def read_file_lines(file_path):
    file=open(file_path,"r")
    
    while True:
        line=file.readline()
        if not line:
            break
        yield line.strip()
    file.close()

file_path = 'example.txt'
for line in read_file_lines(file_path):
    print(line)    
