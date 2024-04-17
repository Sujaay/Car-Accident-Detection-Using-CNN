from keras.models import model_from_json
import numpy as np

class AccidentDetectionModel:
    """A class to load and use an accident detection model."""

    class_nums = ['Accident', 'No Accident']

    def __init__(self, model_json_file, model_weights_file):
        """
        Initialize the AccidentDetectionModel.

        Args:
            model_json_file (str): Path to the JSON file containing the model architecture.
            model_weights_file (str): Path to the model weights file.
        """
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)

    def predict_accident(self, img):
        """
        Predict if an accident has occurred in the given image.

        Args:
            img (numpy.ndarray): Input image for prediction.

        Returns:
            tuple: A tuple containing the predicted class ('Accident' or 'No Accident') and the prediction probabilities.
        """
        preds = self.loaded_model.predict(img)
        return AccidentDetectionModel.class_nums[np.argmax(preds)], preds

# Usage example:
# model = AccidentDetectionModel("model.json", "model_weights.h5")
# pred_class, pred_prob = model.predict_accident(input_image)
