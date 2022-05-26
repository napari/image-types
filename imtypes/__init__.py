from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("imtypes")
except PackageNotFoundError:
    __version__ = version("uninstalled")

from ._types import (
    ImageData,
    LabelsData,
    LayerDataTuple,
    MeshFaces,
    MeshValues,
    MeshVertices,
    PointsData,
    ShapeData,
    ShapesData,
    SurfaceData,
    SurfaceValueData,
    TracksData,
    VectorsData,
)

__all__ = [
    "ImageData",
    "LabelsData",
    "LayerDataTuple",
    "MeshFaces",
    "MeshValues",
    "MeshVertices",
    "PointsData",
    "ShapeData",
    "ShapesData",
    "SurfaceData",
    "SurfaceValueData",
    "TracksData",
    "VectorsData",
]
