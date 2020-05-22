from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json, load_model
from sklearn.externals import joblib
import tensorflow as tf
from tensorflow.keras import backend as k
import numpy as np
config =tf.compat.v1.ConfigProto(
    device_count={'GPU': 1},
    intra_op_parallelism_threads=1,
    allow_soft_placement=True
)
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.6

session = tf.compat.v1.Session(config=config)

k.set_session(session)

# load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model = load_model("model_covid.h5")

loaded_model._make_predict_function()
def ans(path):
    with session.as_default():
        with session.graph.as_default():
            img=image.load_img(path,target_size=(224,224))
            img1=image.img_to_array(img)
            img1=img1/255.0
            img2=img1.reshape(1,224,224,3)
            predictions=loaded_model.predict(img2)
            prediction=np.array((predictions))
            labels=np.argmax(prediction,axis=-1)
            if labels==0:
                return 'positive'
            if labels==1:
                return 'negative'
            return labels
