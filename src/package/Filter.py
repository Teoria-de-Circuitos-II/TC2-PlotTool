import sys
import traceback
from src.package.transfer_function import TFunction
import scipy.signal as signal
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial import Legendre
import sympy as sym
from src.package.Parser import ExprParser
pi = np.pi

MAX_ORDER = 50
LOW_PASS, HIGH_PASS, BAND_PASS, BAND_REJECT, GROUP_DELAY = range(5)
BUTTERWORTH, CHEBYSHEV, CHEBYSHEV2, CAUER, LEGENDRE, BESSEL, GAUSS, APPRX_NONE = range(8)
TEMPLATE_FREQS, F0_BW = range(2)
class AnalogFilter():
    pass
        
    def __str__(self):
        return "{} - orden {}".format(approx_to_str(self.approx_type), self.N)

    def validate(self):
        pass

    def get_tf_norm(self):     
        pass
    
    def compute_normalized_parameters(self, init=False):
        pass
    
    def compute_denormalized_parameters(self):
        pass

    def resetStages(self):
        pass

    def addStage(self, z_arr, p_arr, gain, pz_in_hz=False):
        return True
        

    def removeStage(self, i):
        pass

    def addHelperFilters(self):
        pass

    def swapStages(self, index0, index1):
        pass
    
    def orderStagesBySos(self):
        return True
