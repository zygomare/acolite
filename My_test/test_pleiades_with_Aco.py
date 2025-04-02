import sys, os, time
acol_folder = '/mnt/0_ARCTUS_Projects/'
sys.path.append(acol_folder+"/acolite")
import acolite as ac

l1c="/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L1/Pleiades/WO_000224478_1_3_SAL24206904-3_ACQ_PNEO3_04803413386209+(2)/000224478_1_2_STD_A/"
settings = {
        'inputfile': l1c,
        'output': "/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L2/",
        'l2w_parameters': ['rhorc_*', 'rhos_*','Rrs_*'],
        #'l2w_parameters': [],
        'output_rhorc': False,
        'l1r_export_geotiff': True,
        'l2r_export_geotiff': True,
        'l2w_export_geotiff': True,
        'dsf_aot_estimate': 'fixed',
        'atmospheric_correction': True,
        'atmospheric_correction_method': 'radcor',
        'ancillary_data': False,
        #'s2_target_res': 10,
        'l1r_export_geotiff_rgb': True,
        'l2r_export_geotiff_rgb': True,
        'use_gdal_merge_import': False,
        'reproject_inputfile': True
    }

ac.acolite.acolite_run(settings=settings, inputfile=l1c)
