import os,sys,shutil

def seperate_train_data(path):

    os.makedirs(os.path.join('train', 'cat'))
    os.makedirs(os.path.join('train', 'dog'))
        
    for i in os.listdir(path):
        print(i)
        if "cat" in i:
            old_path = path+"\\"+i
            new_path = 'train\cat\\'+i
            os.rename(old_path,new_path)
        if "dog" in i:
            old_path = path+'\\'+i
            new_path = 'train\dog\\'+i
            os.rename(old_path,new_path)

        

seperate_train_data(sys.argv[1])