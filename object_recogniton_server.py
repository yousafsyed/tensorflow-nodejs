import tensorflow as tf
import sys
from flask import Flask,jsonify
import json


app = Flask(__name__)


PATH_TO_CKPT = "/Users/yousafsyed/Documents/tensorflow/person_classifier/retrained_graph.pb"
PATH_TO_LABEL = "/Users/yousafsyed/Documents/tensorflow/person_classifier/retrained_labels.txt"
PATH_TO_FILES = '/Users/yousafsyed/Documents/Node/tensorflow/files/webcam.jpg'
# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile(PATH_TO_LABEL)]


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Web Server
@app.route('/getLabel', methods=['GET'])
def get_tasks():
    
    image_data = tf.gfile.FastGFile(PATH_TO_FILES, 'rb').read()
    results = {}
    
            # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = detection_graph.get_tensor_by_name('final_result:0')
            
    predictions = sess.run(softmax_tensor, \
                     {'DecodeJpeg/contents:0': image_data})
            
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]


            
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        results[human_string] = str(score)
        #print(jsonify({human_string:str(score)}))
        #print('%s (score = %.5f)' % (human_string, score))

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=False)

