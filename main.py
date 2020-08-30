import seperate_data
import sys,os
import matplotlib.pyplot as plt
from matplotlib.image import imread
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import Callback
import numpy as np

class myCallback(Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.02):
            self.model.stop_training=True
callbacks=myCallback()
seperate_data.seperate_train_data(sys.argv[1])
#dim1=[]
#dim2=[]
#for test_img in os.listdir('train\\'+'cat'):
#    img = imread('train\\cat\\'+test_img)
#    d1,d2,_ = img.shape
#    dim1.append(d1)
#    dim2.append(d2)
#print(np.mean(dim1))
#print(np.mean(dim2))
#Mean image shape is around (356,410,3)
image_shape = (356,410,3)

img_gen = ImageDataGenerator(rescale=1/255)

model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=image_shape, activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

train_generator = img_gen.flow_from_directory('train', target_size=(356,410), batch_size=16,color_mode='rgb', class_mode='binary')
r = model.fit_generator(
    train_generator,
    epochs=15,
    callbacks=[callbacks]
    
)

plt.plot(r.history['accuracy'])
plt.show()


