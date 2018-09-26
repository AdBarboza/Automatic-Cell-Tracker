#!/usr/bin/env python

#Pattern Recognition and Machine Learning (PARMA) Group
#School of Computing, Costa Rica Institute of Technology
#
#title           :unet_CellSegmentation.py
#description     :Cell segmentation using pretrained unet architecture. 
#authors         :Willard Zamora wizaca23@gmail.com, 
#                 Manuel Zumbado manzumbado@ic-itcr.ac.cr
#date            :20180823
#version         :0.1
#usage           :python unet_CellSegmentation.py
#python_version  :>3.5
#==============================================================================
#
import os
import time
import numpy as np

from PIL import Image
import glob
from keras.models import Model
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose
from keras.optimizers import Adam
from keras import backend as K

# #Image size
# img_rows = 256
# img_cols = 256
# #Dice coeficient parameter
# smooth = 1.
# #Paths declaration
# image_path = 'raw/hoechst/test/*.png'
# weights_path = 'weights/pre_0_3_5.h5'
# pred_dir = 'preds/'

class Cell_Segmentation():

    def __init__(self, img_rows = 256, img_cols = 256, smooth = 1, weights_path = 'weights/pre_0_3_5.h5', pred_dir = 'preds/',
                        saveImgs = False):

        self.img_rows = img_rows
        self.img_cols = img_cols
        self.smooth = smooth
        self.weights_path = weights_path
        self.pred_dir = pred_dir
        self.saveImgs = saveImgs

        #Set channel configuration for backend
        K.set_image_data_format('channels_last')

    #Compute dice coeficient used in loss function
    def dice_coef(self, y_true, y_pred):
        y_true_f = K.flatten(y_true)
        y_pred_f = K.flatten(y_pred)
        intersection = K.sum(y_true_f * y_pred_f)
        return (2. * intersection + self.smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + self.smooth)

    #Loss function
    def dice_coef_loss(self, y_true, y_pred):
        return -self.dice_coef(y_true, y_pred)

    #Load test data from directory
    def load_test_data(self, image_path):
        raw = []
        image_filename = dict()
        count = 0
        for filename in glob.glob(image_path):
            name = os.path.basename(filename)[:-4]
            try:
                im = Image.open(filename)
                im = im.convert('L')     
                im = im.resize((self.img_rows,self.img_cols)) 
                raw.append(np.array(im))
                image_filename[count] = name
                count+=1
                im.close()
                break
            except IOError:
                print('Error loading image ', filename)
        return [raw, image_filename]

    # Prepares N amount of images to predict
    def prepare_data(self, X):
        raw = []
        for im in X:
            try:
                im = im.convert('L')
                im = im.resize((self.img_rows,self.img_cols)) 
                raw.append(np.array(im))
                im.close()
            except IOError:
                print('Error loading image ', im)
        return raw


    #Preprocess loaded images
    def preprocess(self, imgs):
        imgs_p = np.ndarray((len(imgs), self.img_rows, self.img_cols), dtype=np.float32)
        for i in range(len(imgs)):
            imgs_p[i] = imgs[i].reshape((self.img_rows, self.img_cols))/255.

        imgs_p = imgs_p[..., np.newaxis]

        #Perform data normalization
        mean = imgs_p.mean()
        std = imgs_p.std()
        imgs_p -=mean
        imgs_p /=std

        return imgs_p

    
    #Define unet architecture
    def get_unet(self):
        inputs = Input((self.img_rows, self.img_cols, 1))
        conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
        conv1 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv1)
        pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

        conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(pool1)
        conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv2)
        pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

        conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(pool2)
        conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv3)
        pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

        conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(pool3)
        conv4 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv4)
        pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

        conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(pool4)
        conv5 = Conv2D(512, (3, 3), activation='relu', padding='same')(conv5)

        up6 = concatenate([Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv5), conv4], axis=3)
        conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(up6)
        conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')(conv6)

        up7 = concatenate([Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv6), conv3], axis=3)
        conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(up7)
        conv7 = Conv2D(128, (3, 3), activation='relu', padding='same')(conv7)

        up8 = concatenate([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv7), conv2], axis=3)
        conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(up8)
        conv8 = Conv2D(64, (3, 3), activation='relu', padding='same')(conv8)

        up9 = concatenate([Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(conv8), conv1], axis=3)
        conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(up9)
        conv9 = Conv2D(32, (3, 3), activation='relu', padding='same')(conv9)

        conv10 = Conv2D(1, (1, 1), activation='sigmoid')(conv9)

        model = Model(inputs=[inputs], outputs=[conv10])

        model.compile(optimizer=Adam(lr=1e-4), loss=self.dice_coef_loss, metrics=[self.dice_coef])

        return model


    def predict(self, X):
        K.clear_session()


        #Load test data
        cell_segmentation_data = self.prepare_data(X)
        
        #Preprocess and reshape test data
        x_test = self.preprocess(cell_segmentation_data)

        #Get model
        model = self.get_unet()

        #Load weights
        model.load_weights(self.weights_path);

        #Make predictions
        imgs_mask_predict = model.predict(x_test, verbose=1)


        np.save('imgs_mask_predict.npy', imgs_mask_predict)

        #if self.saveImgs and not os.path.exists(self.pred_dir):
        #   os.mkdir(self.pred_dir)
        #Save predictions as images

        r = []
        for image_pred,index in zip(imgs_mask_predict,range(x_test.shape[0])):
            image_pred = image_pred[:, :, 0]
            image_pred[image_pred > 0.5] *= 255.
            im = Image.fromarray(image_pred.astype('uint8'))
            
            if self.saveImgs:
                name_file = './resultado.png'
                r.append(name_file)
                im.save(name_file)

        return r
    



