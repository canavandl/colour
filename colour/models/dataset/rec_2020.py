#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Rec. 2020 Colourspace
=====================

Defines the *Rec. 2020* colourspace:

-   :attr:`REC_2020_COLOURSPACE`.

See Also
--------
`RGB Colourspaces IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/models/rgb.ipynb>`_  # noqa

References
----------
.. [1]  `Recommendation ITU-R BT.2020 - Parameter values for ultra-high
        definition television systems for production and international
        programme exchange
        <http://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2020-1-201406-I!!PDF-E.pdf>`_  # noqa
        (Last accessed 2 September 2014)
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models import RGB_Colourspace, normalised_primary_matrix
from colour.utilities import Structure

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['REC_2020_PRIMARIES',
           'REC_2020_WHITEPOINT',
           'REC_2020_TO_XYZ_MATRIX',
           'XYZ_TO_REC_2020_MATRIX',
           'REC_2020_CONSTANTS',
           'REC_2020_TRANSFER_FUNCTION',
           'REC_2020_INVERSE_TRANSFER_FUNCTION',
           'REC_2020_COLOURSPACE']

REC_2020_PRIMARIES = np.array(
    [[0.708, 0.292],
     [0.170, 0.797],
     [0.131, 0.046]])
"""
*Rec. 2020* colourspace primaries.

REC_2020_PRIMARIES : ndarray, (3, 2)
"""

REC_2020_WHITEPOINT = ILLUMINANTS.get(
    'CIE 1931 2 Degree Standard Observer').get('D65')
"""
*Rec. 2020* colourspace whitepoint.

REC_2020_WHITEPOINT : tuple
"""

REC_2020_TO_XYZ_MATRIX = normalised_primary_matrix(REC_2020_PRIMARIES,
                                                   REC_2020_WHITEPOINT)
"""
*Rec. 2020* colourspace to *CIE XYZ* colourspace matrix.

REC_2020_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_REC_2020_MATRIX = np.linalg.inv(REC_2020_TO_XYZ_MATRIX)
"""
*CIE XYZ* colourspace to *Rec. 2020* colourspace matrix.

XYZ_TO_REC_2020_MATRIX : array_like, (3, 3)
"""

REC_2020_CONSTANTS = Structure(alpha=lambda x: 1.099 if x else 1.0993,
                               beta=lambda x: 0.018 if x else 0.0181)
"""
*CIE XYZ* constants.

REC_2020_CONSTANTS : Structure
"""


def _rec_2020_transfer_function(value, is_10_bits_system=True):
    """
    Defines the *Rec. 2020* colourspace transfer function.

    Parameters
    ----------
    value : numeric
        value.
    is_10_bits_system : bool
        *Rec. 709* *alpha* and *beta* constants are used if system is 10 bit.

    Returns
    -------
    :rtype: numeric
    :return: Companded value.

    References
    ----------
    .. [2]  `Recommendation ITU-R BT.2020 - Parameter values for ultra-high
            definition television systems for production and international
            programme exchange
            <http://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2020-1-201406-I!!PDF-E.pdf>`_  # noqa
            (Last accessed 2 September 2014)
    """

    a = REC_2020_CONSTANTS.alpha(is_10_bits_system)
    b = REC_2020_CONSTANTS.beta(is_10_bits_system)
    return (value * 4.5
            if value < b else
            a * (value ** 0.45) - (a - 1))


def _rec_2020_inverse_transfer_function(value, is_10_bits_system=True):
    """
    Defines the *Rec. 2020* colourspace inverse transfer function.

    Parameters
    ----------
    value : numeric
        value.
    is_10_bits_system : bool
        *Rec. 709* *alpha* and *beta* constants are used if system is 10 bit.

    Returns
    -------
    :rtype: numeric
    :return: Companded value.

    References
    ----------
    .. [3]  `Recommendation ITU-R BT.2020 - Parameter values for ultra-high
            definition television systems for production and international
            programme exchange
            <http://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.2020-1-201406-I!!PDF-E.pdf>`_  # noqa
            (Last accessed 2 September 2014)
    """

    a = REC_2020_CONSTANTS.alpha(is_10_bits_system)
    b = REC_2020_CONSTANTS.beta(is_10_bits_system)
    return (value / 4.5
            if value < b else
            ((value + (a - 1)) / a) ** (1 / 0.45))


REC_2020_TRANSFER_FUNCTION = _rec_2020_transfer_function
"""
Transfer function from linear to *Rec. 2020* colourspace.

REC_2020_TRANSFER_FUNCTION : object
"""

REC_2020_INVERSE_TRANSFER_FUNCTION = _rec_2020_inverse_transfer_function
"""
Inverse transfer function from *Rec. 2020* colourspace to linear.

REC_2020_INVERSE_TRANSFER_FUNCTION : object
"""

REC_2020_COLOURSPACE = RGB_Colourspace(
    'Rec. 2020',
    REC_2020_PRIMARIES,
    REC_2020_WHITEPOINT,
    REC_2020_TO_XYZ_MATRIX,
    XYZ_TO_REC_2020_MATRIX,
    REC_2020_TRANSFER_FUNCTION,
    REC_2020_INVERSE_TRANSFER_FUNCTION)
"""
*Rec. 2020* colourspace.

REC_2020_COLOURSPACE : RGB_Colourspace
"""
