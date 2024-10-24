import numpy as np
import open3d as o3d

# Read .ply file
input_file = "C:\\Users\\MuhametovRD\\PycharmProjects\\COLMAP\\output\\mvs\\dense.ply"
pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud

# Visualize the point cloud within open3d
o3d.visualization.draw_geometries([pcd])
