import numpy as np
import pyvista as pv
import open3d as o3d
from pypcd import *
pcd = o3d.io.read_point_cloud("./cloudGlobal_run2.pcd")
xyz_load = np.asarray(pcd.points)

cloud = pv.PolyData(xyz_load)
#cloud.plot()

volume = cloud.delaunay_3d(alpha=0.16)
shell = volume.extract_geometry()
shell.plot()
