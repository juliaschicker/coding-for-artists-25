# https://github.com/serengil/deepface?tab=readme-ov-file
from deepface import DeepFace

# TODO: Move one image you'd like to have as the image you're comparing all the faces with outside of the "faces" folder into the coding-for-artists folder
# TODO: Replace the image paths with your own. Make sure the file ending is the same (e.g. jpg/jpeg).
result = DeepFace.verify(img1_path = "faces/img_1.jpeg", img2_path = "faces/img_2.jpeg")
print(result)

# Check if the image in "image_path" is of the same person as any in your "faces" folder.
# TODO: Copy your faces collection you were asked to bring as one folder called "faces" into the coding-for-artists folder
# TODO: Update the paths below to match yours.
# TODO: Uncomment the following line to make it run.
# dfs = DeepFace.find(img_path = "img_1.jpg", db_path = "./faces")
# print(dfs)

# TODO: Uncomment the following line
# Store the best match in the "match" variable.
# match = dfs[0]
# print(match)
# TODO: Run the code

# TODO: Update the paths in the code below
# TODO: Uncomment the code below
# Show the emotion of a face.
# analysis = DeepFace.analyze(img_path = "faces/img_1.jpg", actions = ['emotion'])
# print(analysis)
# TODO: Run the code