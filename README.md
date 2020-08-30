# Dog-or-Cat-Classifier
Solution of a famous dog or cat image classification tensorflow challenge.

## Dataset

First of all, you need to get the database from kaggle which is linked [here!](https://www.kaggle.com/c/dogs-vs-cats).

## Running the script
After that, you need to extract files from zip file, and run the script as shown below:
```
py main.py <full-path-of-extracted-train-file>
```

![alt text](https://i.hizliresim.com/ENFmOz.png)

**Remember** Your extracted train file's name must be different than "train", python script will be create a "train" directory and "cat" and "dog" subdirectories inside of it.

## Code 

Kaggle dataset wasn't that complicated but still not useful for direct training, so it's needed to be seperated. The case which can be done easily was solved with a pure python script. In order not to confuse us, this script is seperated from the main script.
![alt text](https://i.hizliresim.com/Ent7iq.png)

We have created a CNN model, which is a great model for image classification, and here is the code.
![alt text](https://i.hizliresim.com/fKSGyu.png)

Our model was so successful but training the model took a really long time. -around 5 hours-  Here is the epoch log and accuracy graph
![alt text](https://i.hizliresim.com/CNxN0n.png)
![alt text](https://i.hizliresim.com/s7hTGs.png)