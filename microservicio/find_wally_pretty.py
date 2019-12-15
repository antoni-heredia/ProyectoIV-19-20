from matplotlib import pyplot as plt
import numpy as np
import sys
import tensorflow as tf
import matplotlib
from PIL import Image
import argparse
from object_detection.utils import visualization_utils as vis_util
from object_detection.utils import label_map_util
from io import BytesIO

import cv2


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)




'''
def buscarWally(imagen):
    model_path = 'microservicio/trained_model/frozen_inference_graph.pb'

    label_map = label_map_util.load_labelmap('microservicio/trained_model/labels.txt')
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    detection_graph = tf.Graph()

    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(model_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_np = load_image_into_numpy_array(Image.open(BytesIO(imagen)) )
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: np.expand_dims(image_np, axis=0)})

            if scores[0][0] < 0.1:
                sys.exit('Wally not found :(')

            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)

            
            return image_np
'''
def buscarWally(imagen):
    image_np = load_image_into_numpy_array(Image.open(BytesIO(imagen)) )
    y,x,z = image_np.shape
    startx = x//2
    starty = y//2 
    img = cv2.circle(image_np,(startx,starty), 50, (255,0,0), 4)

    return image_np
    