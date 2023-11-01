import numpy as np
from astropy.constants import c
from aavs_uv.utils import  vis_arr_to_matrix
from aavs_uv.postx.ant_array import RadioArray

LIGHT_SPEED = c.to('m/s').value
cos, sin = np.cos, np.sin

def simulate_visibilities(ant_arr: RadioArray, sky_model: dict):
    """ Simulate model visibilities for an antenna array 
    
    Args:
        ant_arr (AntArray): Antenna array to use
        sky_model (dict): Sky model to use

    Returns:
        model_vis_matrix (np.array): Model visibilities that should be expected given the known applied delays, (Nchan, Nant, Nant)
    """
    for srcname, src in sky_model.items():
        phs = ant_arr._generate_phase_vector(src, conj=True).squeeze()
        phsmat = np.outer(phs, np.conj(phs))
    return phsmat
