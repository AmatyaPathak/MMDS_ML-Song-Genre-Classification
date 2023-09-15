
import tensorflow as tf
import numpy as np
import scipy
from scipy import misc
import glob
from PIL import Image
import os
import matplotlib.pyplot as plt
import librosa
from keras import layers
from keras.layers import (Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, 
                          Conv2D, AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D)
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.utils import layer_utils
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from keras.optimizers import Adam
from keras.initializers import glorot_uniform
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from pydub import AudioSegment


%pip install tensorflow         #Parent of Keras Neural Network API
%pip install numpy
%pip install scipy              
%pip install glob               #Keras ML dependency
%pip install pillow             #Image processing

%pip install librosa            #Mel-spectrogram generator
%pip install matplotlib         #Mel-spectrogram visualization
%pip install pydot              #Mel-spectrogram visualization

%pip install keras              #Neural Network API
%pip install ipython            #For Juypyter notebook code to run
%pip install pydub              #Saving audio files




os.makedirs('/content/spectrograms3sec')
os.makedirs('/content/spectrograms3sec/train')
os.makedirs('/content/spectrograms3sec/test')

genres = 'blues classical country disco pop hiphop metal reggae rock'
genres = genres.split()
for g in genres:
  path_audio = os.path.join('/content/audio3sec',f'{g}')
  os.makedirs(path_audio)
  path_train = os.path.join('/content/gdrive/My Drive/spectrograms3sec/train',f'{g}')
  path_test = os.path.join('/content/gdrive/My Drive/spectrograms3sec/test',f'{g}')
  os. makedirs(path_train)
  os. makedirs(path_test)