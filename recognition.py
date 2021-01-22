import os
import pathlib

import io
import scipy.misc
import numpy as np
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont
from six.moves.urllib.request import urlopen

import tensorflow as tf
import tensorflow_hub as hub

tf.get_logger().setLevel('ERROR')

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.utils import ops as utils_ops

PATH_TO_LABELS = './models/research/object_detection/data/mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

hub_model = hub.load('https://tfhub.dev/tensorflow/efficientdet/d0/1')


import cv2

video_capture = cv2.VideoCapture("mall.mp4")

while True:
    re,frame = video_capture.read()
    frame = cv2.resize(frame, (1280,720))
    image_expanded = np.expand_dims(frame, axis=0)
    # image_np = load_image_into_numpy_array(frame)
    # Imagenp=show_inference(detection_model, frame)
    # cv2.imshow('object detection', cv2.resize(Imagenp, (800,600)))
    results = hub_model(image_expanded)
    result = {key:value.numpy() for key,value in results.items()}

    label_id_offset = 0
    image_np_with_detections = image_expanded.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
          image_np_with_detections[0],
          result['detection_boxes'][0],
          (result['detection_classes'][0] + label_id_offset).astype(int),
          result['detection_scores'][0],
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=200,
          min_score_thresh=.40,
          agnostic_mode=False)

    cv2.imshow('object detection',image_np_with_detections[0])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
