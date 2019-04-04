napari image types
==================

[napari](http://napari.org) is an image viewer and graphical image processing
environment.  Writing a plugin for napari involves annotating a Python function
with image types provided by this package.  As an example, if you provide the
following in a module:

```python
from typing import Union as U, Tuple as Tup
from imtypes import Image


def gaussian_filter(image : Image, sigma : U[float, Tup[float, ...]], *,
                    multichannel : bool = True) -> Image:
    ...
```

Then napari can ingest the module and make the gaussian filter available to
users from its graphical user interface.
