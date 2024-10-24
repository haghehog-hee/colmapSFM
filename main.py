import os
import subprocess
from pycolmap import extract_features


# Define paths
project_path = os.path.abspath('C:\\Users\\MuhametovRD\\PycharmProjects\\COLMAP\\')
image_path = os.path.join(project_path, 'images2')
database_path = os.path.join(project_path, 'database.db')
model_path = os.path.join(project_path, 'model')


extract_features(database_path, image_path, sift_options={"max_num_features": 512})

# Create a new database
# subprocess.run(['colmap', 'database_creator', '--database_path', database_path])

# # Import images into the database
# subprocess.run(['colmap', 'import_images', '--database_path', database_path, '--image_path', image_path])
#
# # Feature extraction
# subprocess.run(['colmap', 'feature_extractor', '--database_path', database_path, '--image_path', image_path])
#
# # Feature matching
# subprocess.run(['colmap', 'exhaustive_matcher', '--database_path', database_path])
#
# # Create a sparse model
# os.makedirs(model_path, exist_ok=True)
# subprocess.run(['colmap', 'mapper', '--database_path', database_path, '--image_path', image_path, '--output_path', model_path])
#
# # Dense reconstruction
# subprocess.run(['colmap', 'image_undistorter', '--input_path', model_path, '--output_path', model_path, '--input_type', 'model'])
#
# # Optionally, you can export the dense model to a specific format
# subprocess.run(['colmap', 'model_converter', '--input_path', model_path, '--output_path', os.path.join(project_path, 'dense_model.ply'), '--output_type', 'PLY'])