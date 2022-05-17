import numpy as np
import typing as t


if tuple(np.__version__.split(".")) < ("1", "20"):
    # this hack is because NewType doesn't allow `Any` as a base type
    # and numpy <=1.20 didn't provide type stubs for np.ndarray
    # https://github.com/python/mypy/issues/6701#issuecomment-609638202
    class Array(np.ndarray):
        def __getattr__(self, name: str) -> t.Any:
            return object.__getattribute__(self, name)

else:
    Array = np.ndarray  # type: ignore


ImageData = t.NewType("ImageData", Array)
"""Dense array of image intensity.  Can be N >= 2 dimensional."""

LabelsData = t.NewType("LabelsData", Array)
"""Dense array of integers or bool.  Can be N >= 2 dimensional."""

PointsData = t.NewType("PointsData", Array)
"""(N, D) Coordinates for N points in D dimensions."""

ShapeData = t.NewType("ShapeData", Array)
"""(N, D) array of the N vertices of a shape in D dimensions."""
ShapesData = t.NewType("ShapesData", t.List[ShapeData])
"""List of ShapeData.

Can be a 3-dimensional (M, N, D) array of M shapes if each shape has
the same number (N) of vertices in D dimensions.
"""

MeshVertices = t.NewType("MeshVertices", Array)
"""(N, D) array of vertices of mesh triangles."""
MeshFaces = t.NewType("MeshFaces", Array)
"""(M, 3) array of int of indices of triangular mesh faces."""
MeshValues = t.NewType("MeshValues", Array)
"""(K0, ..., KL, N) array of values used to color vertices.

where the additional L dimensions are used to color the same mesh with different values
"""

SurfaceData = t.NewType("SurfaceData", t.Tuple[MeshVertices, MeshFaces])
"""Surface data tuple, containing (vertices, faces)."""
SurfaceValueData = t.NewType(
    "SurfaceValueData", t.Tuple[MeshVertices, MeshFaces, MeshValues]
)
"""Surface data tuple, containing (vertices, faces, values)."""

TracksData = t.NewType("TracksData", Array)
"""(N, D+1) Array.  Coordinates for N points in D+1 dimensions. ID,T,(Z),Y,X.

The first axis is the integer ID of the track.
D is either 3 or 4 for planar or volumetric timeseries respectively.
"""

VectorsData = t.NewType("VectorsData", Array)
"""(N, 2, D) array interpreted as "coordinate-like" data.

N vectors with start point and projections of the vector in D dimensions.
"""

# alternate vector:
# An (N1, N2, ..., ND, D) array is interpreted as
# "image-like" data where there is a length D vector of the
# projections at each pixel.


# napari-specific ...  include?
LayerDataTuple = t.NewType("LayerDataTuple", tuple)
"""Tuple of data & metadata, for consumption by napari.

Could be one of the following forms:
1. length==1: (data,)
2. length==2: (data, dict_of_kwargs_for_napari_layer)
3. length==3: (data, dict_of_kwargs_for_napari_layer, string_layer_type)
"""
