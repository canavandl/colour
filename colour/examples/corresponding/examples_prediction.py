#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Showcases corresponding chromaticities prediction computations.
"""

from __future__ import division, unicode_literals

from pprint import pprint

import colour
from colour.utilities.verbose import message_box

message_box('Corresponding Chromaticities Prediction Computations')

message_box(('Computing corresponding chromaticities prediction with '
             '"Von Kries" chromatic adaptation model for "Edwin J. Breneman" '
             'experiment number "3" and "Bianco" CAT.'))
pprint(colour.corresponding_chromaticities_prediction_vonkries(3, 'Bianco'))

print('\n')

message_box(('Computing corresponding chromaticities prediction with '
             '"CIE 1994" chromatic adaptation model for "Edwin J. Breneman" '
             'experiment number "1".'))
pprint(colour.corresponding_chromaticities_prediction_cie1994(1))

print('\n')

message_box(('Computing corresponding chromaticities prediction with '
             '"CMCCAT2000" chromatic adaptation model for "Edwin J. Breneman" '
             'experiment number "1".'))
pprint(colour.corresponding_chromaticities_prediction_CMCCAT2000(1))

print('\n')

message_box(('Computing corresponding chromaticities prediction with '
             '"Fairchild (1990)" chromatic adaptation model for '
             '"Edwin J. Breneman" experiment number "1".'))
pprint(colour.corresponding_chromaticities_prediction_fairchild1990(1))