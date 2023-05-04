import os
from re import A
import librosa
import math
import json
import numpy as np
import tensorflow
from pathlib import Path
model_genre = tensorflow.keras.models.load_model(r"/home/leo/Integrated/Genre Classification/saved model")
