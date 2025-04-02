import sys, os, time
import glob

acol_folder = '/mnt/0_ARCTUS_Projects/'
sys.path.append(acol_folder+"/acolite")
import acolite as ac

#l1c="/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L1/Planet/Request15-R15-D-2024-05-19-C1-TOAR-8band-COG-Mosaic/"

def process(l1c,Outputdir):
    out_name = 'Acolite_out'
    # p= Path(l1c)
    # l2_dir= str(p.parent)
    settings = {
        'inputfile': l1c,
        'l2w_parameters': ['rhorc_*', 'rhos_*','Rrs_*','spm_nechad2010','tur_nechad2010'],
        'output': Outputdir,
        'output_rhorc': False,
        'l1r_export_geotiff': True,
        'l2r_export_geotiff': True,
        'l2w_export_geotiff': True,
        'dsf_aot_estimate': 'fixed',
        'atmospheric_correction_method':'radcor',
        'atmospheric_correction': True,
        'ancillary_data': False,
        'l1r_export_geotiff_rgb': True,
        'l2r_export_geotiff_rgb': True,
        'use_gdal_merge_import': False,
        'reproject_inputfile': True,
        'dsf_residual_glint_correction': True

    }
    ac.acolite.acolite_run(settings=settings, inputfile=l1c)

#if __name__ == '__main__':
#   main()
planet_dir = '/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L1/Planet/'
l2_base_dir = '/mnt/0_ARCTUS_Projects/19_SAGE-Port/dataset/L2/Planet_Aco_radcor/'

for fname in  glob.glob(os.path.join(planet_dir,'Hatfield+Consultants*','composite*.tif'), recursive=True):
    l2_dir = os.path.join(l2_base_dir, os.path.basename(os.path.dirname(os.path.normpath(fname))))
    l1d=os.path.dirname(os.path.normpath(fname))+'/'
    if os.path.exists(l2_dir):
        #print(f"Skipping {l1d} as {l2_dir} already exists.")
        continue
    print('THIS is the process to do', l1d)
    process(l1c=l1d, Outputdir=l2_dir)
#process(l1c=l1d)
