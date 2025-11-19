# https://github.com/serengil/deepface?tab=readme-ov-file
from deepface import DeepFace

# Store your images in the "faces" folder.
# Replace the image paths with your onw. Make sure the file ending is the same (e.g. jpg/jpeg).
result = DeepFace.verify(img1_path = "faces/img_1.jpg", img2_path = "faces/img_2.jpg")
print(result)

# Check if the image in "image_path" is of the same person as any in your "faces" folder.
# Make sure you're using an image for "img_path" that is not in your "faces" folder.
# Uncomment the following line to make it run.
# dfs = DeepFace.find(img_path = "img_1.jpg", db_path = "./faces")
# print(dfs)

# Store the best match in the "match" variable.
# match = dfs[0]
# print(match)

# Show the emotion of a face.
# analysis = DeepFace.analyze(img_path = "faces/img_1.jpg", actions = ['emotion'])
# print(analysis)