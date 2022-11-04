import os
import time
import numpy as np
import open3d as o3d

start0 = time.time()
str0 = "/home/mingyu/colmap_test2"

str1 = "colmap feature_extractor \
   --database_path " + str0 + "/database.db \
   --image_path " + str0 + "/images"
os.system(str1)   

str1 = "colmap exhaustive_matcher \
   --database_path " + str0 + "/database.db"
os.system(str1)

str1 = "colmap mapper \
    --database_path " + str0 + "/database.db \
    --image_path " + str0 + "/images \
    --output_path " + str0 + "/sparse"
os.system(str1)

str1 = "colmap image_undistorter \
    --image_path " + str0 + "/images \
    --input_path " + str0 + "/sparse/0 \
    --output_path " + str0 + "/dense \
    --output_type COLMAP \
    --max_image_size 200"
os.system(str1)


str1 = "colmap patch_match_stereo \
    --workspace_path " + str0 + "/dense \
    --workspace_format COLMAP \
    --PatchMatchStereo.geom_consistency true"
os.system(str1)


str1 = "colmap stereo_fusion \
    --workspace_path " + str0 + "/dense \
    --workspace_format COLMAP \
    --input_type geometric \
    --output_path " + str0 + "/fused0.ply"
os.system(str1)

print("time used : + " +  str(time.time() - start0))


# Read .ply file
input_file = "fused0.ply"
pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud

# Visualize the point cloud within open3d
o3d.visualization.draw_geometries([pcd]) 

# Convert open3d format to numpy array
# Here, you have the point cloud in numpy format. 
point_cloud_in_numpy = np.asarray(pcd.points) 



