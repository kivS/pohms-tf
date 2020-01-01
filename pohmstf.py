import click
from tensorflow import keras
from PIL import Image
import numpy as np


LABELS = np.array(['ceramic-resistor', 'not-a-ceramic-resistor'])


@click.group()
def main_cli():
    '''
        Ceramic-resistor/not-ceramic-resistor image detector
    '''
    pass


@main_cli.command()
def detect():
    '''
        Detect if an image is a ceramic resistor or not
    '''

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = keras.models.load_model('./model/keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open('./test_images/10.jpeg')

    image.show()

    # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
    image = image.resize((224, 224))
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    prediction = model.predict(data)

    pred_result_label = LABELS[prediction.argmax()]

    pred_result_val = prediction.max()

    click.echo(f'Image prediction: {pred_result_label}')
    click.echo(f'Prediction confidence: {pred_result_val}')


if __name__ == '__main__':
    main_cli()
