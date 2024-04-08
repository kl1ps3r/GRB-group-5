
import numpy as np


def Fully_Coded(d_m, d_d, D):
    FCFOV = np.rad2deg(2 * np.arctan((d_m - d_d) / (2*D)))
    return FCFOV

def Partially_Coded(d_m, d_d, D):
    PCFOV = np.rad2deg(2 * np.arctan((d_m + d_d) / (2*D)))
    return PCFOV

def AngRes(l_m, D):
    AR = np.rad2deg(np.arctan(l_m / D))
    return AR

def Localisation(l_d, D, sigma):
    PSL = np.rad2deg((1 / sigma) * np.arctan(l_d / D))

    return PSL