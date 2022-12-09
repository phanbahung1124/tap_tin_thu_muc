#1
import os

def cwd():
    #2
    cwd = os.getcwd()
    print(cwd)

def main():
    #3
    os.chdir('D:/data')
    chdir = os.getcwd()
    print(chdir)

    #4
    os.makedirs('D:/data/nnlt')

    #5
    dir_list = os.listdir('C:/Users/Admin/OneDrive/Documents')
    print(dir_list)

    #6
    ex = os.path.exists('D:/data/hung1124.txt')
    print(ex)

    #7
    file = 'hung1100.txt'
    location = 'D:/data'
    path = os.path.join(location,file)
    os.remove(path)

    path1 = os.path.join('D:/data','hung1')
    os.rmdir(path1)

if __name__ =="__main__":
    main()