# Feature Extraction

All of the models in timm have consistent mechanisms for obtaining various types of features from the model for tasks besides classification.

## Penultimate Layer Features (Pre-Classifier Features)

The features from the penultimate model layer can be obtained in several ways without requiring model surgery (although feel free to do surgery). One must first decide if they want pooled or un-pooled features.

### Unpooled

forward_features():

Create with no classifier and pooling:

Remove it later:

Chaining unpooled output to classifier:

### Pooled

Create with no classifier:

Remove it later:

## Multi-scale Feature Maps (Feature Pyramid)

### Create a feature map

### Query the feature information

### Select specific feature levels or limit the stride

Output index selection

Output stride (feature map dilation)

## Flexible intermediate feature map extraction
