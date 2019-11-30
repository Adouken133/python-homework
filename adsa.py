import random


file_path ='C:\Users\01yt0\Desktop\python\housing(1).data'

if os.path.isfile(file_path):
    my_file = open(file_path)
    for line in my_file.readlines():
        stripped_line = line.strip()
        print(f'line has the content "{stripped_line}"')


    

        
my_file.close()
