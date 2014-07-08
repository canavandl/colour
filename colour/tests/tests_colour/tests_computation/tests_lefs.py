# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_lefs.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.computation.lefs` module.

**Others:**

"""

from __future__ import unicode_literals

import numpy
import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import colour.computation.lefs

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["MESOPIC_LEF_SPD_DATA",
           "TestMesopicWeightingFunction",
           "TestMesopicLuminousEfficiencyFunction"]

MESOPIC_LEF_SPD_DATA = numpy.array([
    0.000423996221042,
    0.000478105586021,
    0.000539901310829,
    0.000612292743837,
    0.000696128469661,
    0.000792943994169,
    0.000907002019269,
    0.00103899106295,
    0.00119229801342,
    0.00137030978874,
    0.0015771001337,
    0.00181673294407,
    0.00209421757886,
    0.00241607656854,
    0.0027888324436,
    0.00321969465573,
    0.00372228510684,
    0.00429576958789,
    0.00495315038359,
    0.00571429894141,
    0.00657847902152,
    0.00756579824913,
    0.00869129492222,
    0.00996380213983,
    0.0114058913763,
    0.0130401340563,
    0.014875060844,
    0.0169310810534,
    0.0192211073827,
    0.0217511833178,
    0.0245342215569,
    0.0275773753428,
    0.0309172783989,
    0.0345148966619,
    0.0383998876964,
    0.0425744317194,
    0.0471074203238,
    0.0519322888741,
    0.0570541111131,
    0.0625466529082,
    0.0683462958769,
    0.0745255324768,
    0.0809440933885,
    0.0877344085018,
    0.0948915234567,
    0.102273099642,
    0.10987700161,
    0.117842125287,
    0.126031604242,
    0.134377265167,
    0.14301700466,
    0.15181283161,
    0.160832831285,
    0.170008823906,
    0.179272634672,
    0.188693478005,
    0.198204129186,
    0.207803250139,
    0.217418447892,
    0.227114713722,
    0.236819654657,
    0.246462295388,
    0.256115392007,
    0.265716062323,
    0.27533879347,
    0.284852031027,
    0.2944648409,
    0.303490271989,
    0.313234753059,
    0.322325715015,
    0.331451347545,
    0.340612983749,
    0.349811757758,
    0.358361748147,
    0.36763779227,
    0.376267037501,
    0.384939235443,
    0.393654052823,
    0.402407748999,
    0.411196583328,
    0.419329893917,
    0.428180314526,
    0.436380414469,
    0.445311711528,
    0.454294964706,
    0.462650937977,
    0.471757050336,
    0.480930016714,
    0.490177596952,
    0.499507550892,
    0.509614559627,
    0.519129332098,
    0.529425904806,
    0.539131693733,
    0.549621720283,
    0.560210336614,
    0.570219774106,
    0.581020791226,
    0.591909355274,
    0.602868354806,
    0.613880678377,
    0.624937372324,
    0.636061964883,
    0.646598972109,
    0.657953823041,
    0.668784162222,
    0.679793972609,
    0.690988775626,
    0.702382747907,
    0.713303244319,
    0.724451313004,
    0.735847049962,
    0.746811890694,
    0.758029423699,
    0.769496415709,
    0.780522562978,
    0.791780560382,
    0.802612337361,
    0.813079325993,
    0.823929780124,
    0.835225181574,
    0.845634267483,
    0.856481883918,
    0.867692173457,
    0.878502108708,
    0.888148910997,
    0.898640517466,
    0.907932280953,
    0.917425551605,
    0.925773944818,
    0.935065632507,
    0.943236567905,
    0.950906320821,
    0.958693118011,
    0.965841393474,
    0.9722825522,
    0.977992469041,
    0.983610660576,
    0.988346542032,
    0.992096449883,
    0.995443641861,
    0.997620215803,
    0.999345724088,
    1.0,
    0.999649798071,
    0.999048794087,
    0.997535634478,
    0.995761525329,
    0.993014375646,
    0.989955936939,
    0.985874118213,
    0.981445295295,
    0.976688569332,
    0.970936319193,
    0.964894766246,
    0.958583260353,
    0.952011998742,
    0.944491622775,
    0.936708904475,
    0.92935066561,
    0.921042964191,
    0.912477248043,
    0.903660431385,
    0.894595846968,
    0.884599956036,
    0.875050033331,
    0.865945730653,
    0.855922407877,
    0.845684595123,
    0.835249901265,
    0.825322906166,
    0.815207983624,
    0.804220500547,
    0.794420922234,
    0.783746644455,
    0.773568077475,
    0.762780824837,
    0.752271069435,
    0.74175498962,
    0.731290980804,
    0.72079831316,
    0.710193918959,
    0.699636273302,
    0.68906568747,
    0.678559906736,
    0.668059341867,
    0.657569763,
    0.647157872558,
    0.636820835214,
    0.626487173259,
    0.616154150852,
    0.605889614493,
    0.59570008046,
    0.585593706536,
    0.57544126625,
    0.565388301637,
    0.555374278353,
    0.545468087493,
    0.535597256497,
    0.525826697054,
    0.516015244479,
    0.506232237549,
    0.496559550172,
    0.486874671128,
    0.477329907438,
    0.467802847366,
    0.458370440306,
    0.448972251399,
    0.43976063741,
    0.430613136861,
    0.421544622781,
    0.412568127725,
    0.403755029916,
    0.395035990576,
    0.386410412794,
    0.377877749402,
    0.369440537271,
    0.361107481351,
    0.352859660515,
    0.344705630486,
    0.336647077773,
    0.328691712476,
    0.320841076614,
    0.313080884594,
    0.305410539505,
    0.297822525481,
    0.290302706157,
    0.282872778768,
    0.275531191822,
    0.268290082505,
    0.261147799838,
    0.254117629826,
    0.247188574622,
    0.24035705276,
    0.233605744352,
    0.226937937143,
    0.220352731031,
    0.213846544549,
    0.20739460116,
    0.200978993536,
    0.194581814351,
    0.188194308912,
    0.181822635824,
    0.175498734556,
    0.169247675365,
    0.163087659295,
    0.15702570005,
    0.151071000005,
    0.145246954751,
    0.139584565755,
    0.134108701934,
    0.128840802338,
    0.123766619272,
    0.118863181143,
    0.114107516355,
    0.109476653316,
    0.10496136833,
    0.100567919488,
    0.0962924363428,
    0.0921296746063,
    0.0880778245964,
    0.0841305974305,
    0.0802887392473,
    0.0765559902146,
    0.0729367276787,
    0.0694345923224,
    0.0660490961947,
    0.0627792444441,
    0.0596278723973,
    0.0565970787172,
    0.0536895992453,
    0.0509068859909,
    0.048244432277,
    0.0456950950701,
    0.0432510692865,
    0.0409052367641,
    0.0386537325048,
    0.036495591266,
    0.0344285447862,
    0.0324501187277,
    0.030557907445,
    0.0287496277538,
    0.0270233385096,
    0.02537768174,
    0.023811304447,
    0.0223226525306,
    0.0209086279758,
    0.0195688079709,
    0.0183056706434,
    0.0171216254289,
    0.0160192878392,
    0.0149986249495,
    0.0140537631093,
    0.0131784387812,
    0.0123662560177,
    0.0116107551535,
    0.0109097963105,
    0.0102587832748,
    0.00964764507027,
    0.00906652177145,
    0.00850535235064,
    0.00795670337244,
    0.00742298427234,
    0.00690949168694,
    0.00642130622795,
    0.0059637295062,
    0.00553774145039,
    0.00514019832989,
    0.00477000322621,
    0.00442633358667,
    0.00410813420548,
    0.00381489891643,
    0.0035455950637,
    0.00329848442859,
    0.00307184302824,
    0.00286394737725,
    0.00267382152631,
    0.00250002611485,
    0.00234016314816,
    0.00219184787251,
    0.00205266755991,
    0.00192077567129,
    0.00179599869981,
    0.00167846268369,
    0.00156832064055,
    0.00146570448296,
    0.00137020203448,
    0.00128100050147,
    0.00119762574244,
    0.00111958251087,
    0.00104639567042,
    0.000977644493684,
    0.000913102154518,
    0.000852563310843,
    0.000795835861579,
    0.000742713469792,
    0.000692929112612,
    0.00064629407619,
    0.000602683198736,
    0.000561985056886,
    0.000524088227275,
    0.000488865075198,
    0.000456100902232,
    0.000425592157031,
    0.000397124984426,
    0.000370486903095,
    0.000345511126189,
    0.000322107797301,
    0.000300185818831,
    0.000279651295749,
    0.000260410283283,
    0.000242354880318,
    0.000225413417278,
    0.0002095485067,
    0.000194724821881,
    0.000180904975355,
    0.000168036678203,
    0.000156055324297,
    0.00014490794727,
    0.000134542904857,
    0.000124905757365,
    0.000115947828132,
    0.00010763024689,
    9.99218250454e-05,
    9.27920111835e-05,
    8.62095172257e-05,
    8.01385569434e-05,
    7.45426903485e-05,
    6.93820925892e-05,
    6.4618362399e-05,
    6.02131482536e-05,
    5.61336295294e-05,
    5.23563182569e-05,
    4.88548011297e-05,
    4.56019132548e-05,
    4.25711866087e-05,
    3.97370933028e-05,
    3.70857651076e-05,
    3.46082533342e-05,
    3.22949173981e-05,
    3.01374855831e-05,
    2.81222782078e-05,
    2.62387005777e-05,
    2.44797036965e-05,
    2.2839057899e-05,
    2.13103911615e-05,
    1.98861982773e-05,
    1.85586466859e-05,
    1.73210599866e-05,
    1.61666243942e-05,
    1.50885261236e-05,
    1.40803235117e-05,
    1.31378630535e-05,
    1.22576795865e-05,
    1.14365189992e-05,
    1.06710634617e-05,
    9.95726582356e-06,
    9.29144016011e-06,
    8.67065568628e-06,
    8.0917805149e-06])


class TestMesopicWeightingFunction(unittest.TestCase):
    """
    Defines :func:`colour.computation.lefs.mesopic_weighting_function` definition units tests methods.
    """

    def test_mesopic_weighting_function(self):
        """
        Tests :func:`colour.computation.lefs.mesopic_weighting_function` definition.
        """

        self.assertAlmostEqual(colour.computation.lefs.mesopic_weighting_function(500, 0.2),
                               0.7052200000000001,
                               places=7)
        self.assertAlmostEqual(colour.computation.lefs.mesopic_weighting_function(500,
                                                                                  0.2,
                                                                                  source="Red Heavy",
                                                                                  method="LRC"),
                               0.9095099999999999,
                               places=7)
        self.assertAlmostEqual(colour.computation.lefs.mesopic_weighting_function(700,
                                                                                  10,
                                                                                  source="Red Heavy",
                                                                                  method="LRC"),
                               0.004102,
                               places=7)


class TestMesopicLuminousEfficiencyFunction(unittest.TestCase):
    """
    Defines :func:`colour.computation.lefs.mesopic_luminous_efficiency_function` definition units tests methods.
    """

    def test_mesopic_luminous_efficiency_function(self):
        """
        Tests :func:`colour.computation.lefs.mesopic_luminous_efficiency_function` definition.
        """

        numpy.testing.assert_almost_equal(colour.computation.lefs.mesopic_luminous_efficiency_function(0.2).values,
                                          MESOPIC_LEF_SPD_DATA,
                                          decimal=7)


if __name__ == "__main__":
    unittest.main()
