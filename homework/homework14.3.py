fs=open("specific_position.txt", mode="w+")
fs.write("hello")
fs=open("specific_position.txt",mode="r+")
fs.seek(7)
fs.write("have a good day")
