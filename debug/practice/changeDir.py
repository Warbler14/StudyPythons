import os

print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))

print('-----')

dir_path=os.getcwd()
removal = 'X2Download.com -'

file_list = os.listdir(dir_path)
for item in file_list:
        filename,fileExtention=os.path.splitext(item)
        #print(filename + '|' + fileExtention)
        #print(item.find(removal))
        if fileExtention == '.mp3' and item.find(removal) == 0:
                file_newname=item[len(removal) + 1:len(item)]
                #print(file_newname)
                file_oldname_path = os.path.join(dir_path, item)
                file_newname_path = os.path.join(dir_path, file_newname)
                print(file_oldname_path, file_newname_path)
                os.rename(file_oldname_path, file_newname_path)

print('-----end-----')
