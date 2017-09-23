# CV_FaceCascadeClassifier_Parser
This is a python xml parser for parsing opencv trained face cascade classifiers

To run:

python read_xml.py example/haarcascade_frontalface_default.xml

Understanding the xml file:

Example:
```
<stages>
    <_>
      <maxWeakCount>9</maxWeakCount>
      <stageThreshold>-5.0425500869750977e+00</stageThreshold>
      <weakClassifiers>
              <_>
                <internalNodes>
                  0 -1 0 -3.1511999666690826e-02</internalNodes>
                <leafValues>
                  2.0875380039215088e+00 -2.2172100543975830e+00</leafValues></_>
              <_>
                <internalNodes>
                  0 -1 1 1.2396000325679779e-02</internalNodes>
                <leafValues>
                  -1.8633940219879150e+00 1.3272049427032471e+00</leafValues></_>
.
.
.
</stages>
```
The given stage has 9 weak classifiers and the stage threshold is as given.
Format of internal node: <left_leaf_label, right_leaf_label, feature_index, feature_threshold>
Format of leafvalues corresponding to the internal node: <left_leaf_value_to_add, right_leaf_value_to_add>

```
<features>
<_>
      <rects>
        <_>
          2 14 8 10 -1.</_>
        <_>
          2 14 4 5 2.</_>
        <_>
          6 19 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 11 20 13 -1.</_>
        <_>
          2 11 10 13 2.</_></rects></_>
    <_>
.
.
</features>
```
The feature index in internalnode corresponds to the rects in features element in the order given.
Format of rect element : <color_block> <color_block> ...
Format of <_>: <top_left_position_x, top_left_position_y, block_width, block_height, block_weight>
  

