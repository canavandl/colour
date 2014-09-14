#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Chromatic Adaptation Transforms
===============================

Defines various chromatic adaptation transforms (CAT):

-   :attr:`XYZ_SCALING_CAT`: *XYZ Scaling* CAT [1]_
-   :attr:`VON_KRIES_CAT`: *Johannes Von Kries* CAT [1]_
-   :attr:`BRADFORD_CAT`: *Bradford* CAT [1]_
-   :attr:`SHARP_CAT`: *Sharp* CAT [4]_
-   :attr:`FAIRCHILD_CAT`: *Mark D. Fairchild* CAT [2]_
-   :attr:`CMCCAT97_CAT`: *CMCCAT97* CAT [5]_
-   :attr:`CMCCAT2000_CAT`: *CMCCAT2000* CAT [5]_
-   :attr:`CAT02_CAT`: *CAT02* CAT [3]_
-   :attr:`BS_CAT`: *S. Bianco* and R. Schettini* CAT [4]_
-   :attr:`BS_PC_CAT`: *S. Bianco* and R. Schettini PC* CAT [4]_

See Also
--------
`Chromatic Adaptation Transforms IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/adaptation/cat.ipynb>`_  # noqa

References
----------
.. [1]  http://brucelindbloom.com/Eqn_ChromAdapt.html
.. [2]  http://rit-mcsl.org/fairchild//files/FairchildYSh.zip
.. [3]  http://en.wikipedia.org/wiki/CIECAM02#CAT02
.. [4]  **S. Bianco* and R. Schettini**,
        *Color Research & Application, Volume 35, Issue 3, pages 184–192,
        June 2010*,
        DOI: http://dx.doi.org/10.1002/col.20573
        `Two new von Kries based chromatic adaptation transforms found by
        numerical optimization
        <http://web.stanford.edu/~sujason/ColorBalancing/Papers/Two%20New%20von%20Kries%20Based%20Chromatic%20Adaptation.pdf>`_  # noqa
.. [5]  **Stephen Westland, Caterina Ripamonti, Vien Cheung**,
        *Computational Colour Science Using MATLAB, 2nd Edition*,
        The Wiley-IS&T Series in Imaging Science and Technology,
        published July 2012, ISBN-13: 978-0-470-66569-5, page  80.
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['XYZ_SCALING_CAT',
           'VON_KRIES_CAT',
           'BRADFORD_CAT',
           'SHARP_CAT',
           'FAIRCHILD_CAT',
           'CMCCAT97_CAT',
           'CMCCAT2000_CAT',
           'CAT02_CAT',
           'BS_CAT',
           'BS_PC_CAT',
           'CHROMATIC_ADAPTATION_TRANSFORMS']

XYZ_SCALING_CAT = np.array(np.identity(3)).reshape((3, 3))
"""
*XYZ Scaling* chromatic adaptation transform. [1]_

XYZ_SCALING_CAT : array_like, (3, 3)
"""

VON_KRIES_CAT = np.array(
    [[0.4002400, 0.7076000, -0.0808100],
     [-0.2263000, 1.1653200, 0.0457000],
     [0.0000000, 0.0000000, 0.9182200]])
"""
*Johannes Von Kries* chromatic adaptation transform. [1]_

VON_KRIES_CAT : array_like, (3, 3)
"""

BRADFORD_CAT = np.array(
    [[0.8951000, 0.2664000, -0.1614000],
     [-0.7502000, 1.7135000, 0.0367000],
     [0.0389000, -0.0685000, 1.0296000]])
"""
*Bradford* chromatic adaptation transform. [1]_

BRADFORD_CAT : array_like, (3, 3)
"""

SHARP_CAT = np.array(
    [[1.2694, -0.0988, -0.1706],
     [-0.8364, 1.8006, 0.0357],
     [0.0297, -0.0315, 1.0018]])
"""
*Sharp* chromatic adaptation transform. [4]_

SHARP_CAT : array_like, (3, 3)
"""

FAIRCHILD_CAT = np.array(
    [[0.8562, 0.3372, -0.1934],
     [-0.8360, 1.8327, 0.0033],
     [0.0357, -0.0469, 1.0112]])
"""
*Mark D. Fairchild* chromatic adaptation transform. [2]_

FAIRCHILD_CAT : array_like, (3, 3)
"""

CMCCAT97_CAT = np.array(
    [[0.8951, -0.7502, 0.0389],
     [0.2664, 1.7135, 0.0685],
     [-0.1614, 0.0367, 1.0296]])
"""
*CMCCAT97* chromatic adaptation transform. [5]_

CMCCAT97_CAT : array_like, (3, 3)
"""

CMCCAT2000_CAT = np.array(
    [[0.7982, 0.3389, -0.1371],
     [-0.5918, 1.5512, 0.0406],
     [0.0008, 0.0239, 0.9753]])
"""
*CMCCAT2000* chromatic adaptation transform. [5]_

CMCCAT2000_CAT : array_like, (3, 3)
"""

CAT02_CAT = np.array(
    [[0.7328, 0.4296, -0.1624],
     [-0.7036, 1.6975, 0.0061],
     [0.0030, 0.0136, 0.9834]])
"""
*CAT02* chromatic adaptation transform. [3]_

CAT02_CAT : array_like, (3, 3)
"""

BS_CAT = np.array(
    [[0.8752, 0.2787, -0.1539],
     [-0.8904, 1.8709, 0.0195],
     [-0.0061, 0.0162, 0.9899]])
"""
*S. Bianco* and R. Schettini* chromatic adaptation transform. [4]_

BS_CAT : array_like, (3, 3)
"""

BS_PC_CAT = np.array(
    [[0.6489, 0.3915, -0.0404],
     [-0.3775, 1.3055, 0.0720],
     [-0.0271, 0.0888, 0.9383]])
"""
*S. Bianco* and R. Schettini* chromatic adaptation transform. [4]_

BS_PC_CAT : array_like, (3, 3)

Notes
-----
-   This chromatic adaptation transform has no negative lobes.
"""

CHROMATIC_ADAPTATION_TRANSFORMS = CaseInsensitiveMapping(
    {'XYZ Scaling': XYZ_SCALING_CAT,
     'Von Kries': VON_KRIES_CAT,
     'Bradford': BRADFORD_CAT,
     'Sharp': SHARP_CAT,
     'Fairchild': FAIRCHILD_CAT,
     'CMCCAT97': CMCCAT97_CAT,
     'CMCCAT2000': CMCCAT2000_CAT,
     'CAT02': CAT02_CAT,
     'Bianco': BS_CAT,
     'Bianco PC': BS_PC_CAT})
"""
Supported chromatic adaptation transforms.

CHROMATIC_ADAPTATION_TRANSFORMS : CaseInsensitiveMapping
    {'XYZ Scaling', 'Von Kries', 'Bradford', 'Sharp', 'CMCCAT97', 'CMCCAT2000',
    'Fairchild, 'CAT02', 'Bianco', 'Bianco PC'}
"""