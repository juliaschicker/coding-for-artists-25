# https://www.tensorflow.org/tutorials/quickstart/beginner
# Before running:
# pip install tensorflow
# pip install matplotlib
import tensorflow as tf
import matplotlib.pyplot as plt
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)

model.evaluate(x_test,  y_test, verbose=2)

# Visualize predictions
def show_predictions(model, x_test, y_test, num_samples=9):
    plt.figure(figsize=(10, 10))
    
    # Get predictions for the first num_samples
    predictions = model.predict(x_test[:num_samples])
    predicted_classes = tf.argmax(predictions, axis=1).numpy()
    
    for i in range(num_samples):
        plt.subplot(3, 3, i + 1)
        plt.imshow(x_test[i], cmap='gray')
        plt.title(f'True: {y_test[i]}\nPred: {predicted_classes[i]}')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()

show_predictions(model, x_test, y_test)