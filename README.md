# brain_tumor_classification

# Project Description
This project aims to classify brain tumors using CNN applied to an MRI dataset ('Brain Tumor MRI Dataset'). The images are classified into four categories: glioma, meningioma, no tumor, and pituitary. A Django-based web interface is included to allow user interaction, result visualization, and predictions.

# Datasets
The data used for this project is from the Kaggle "Brain Tumor MRI Dataset." This dataset contains a total of 7023 images, split into 5712 training images and 1311 testing images across four classes: glioma, meningioma, no tumor, and pituitary.

# CNN (Convolutional Neural Network) model

Architecture: Four convolutional layers with the activation function RELU, followed by two fully connected layers with RELU and the last layer with Softmax
- **Optimizer**: Adam
- **loss function**= categorical_crossentropy
- **Accuracy**: 0.96
- **Recall**: 0.96
- **Precision**: 0.96
- **F1-Score**: 0.96# brain_tumor_classification
