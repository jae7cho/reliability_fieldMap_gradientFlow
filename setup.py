#!/usr/bin/env python

import setuptools
from distutils.core import setup

setup(name='variabilityFMGF',
      version='1.0',
      description='Package to utilize variability field map and variability gradient flow frameworks',
      author='Jae Wook Cho',
      author_email='jae7cho@gmail.com',
      url='https://github.com/jae7cho/reliability_fieldMap_gradientFlow',
      packages=setuptools.find_packages(),
      install_requires=['numpy','matplotlib','scipy','pandas','cifti',
                        'scikit-learn>0.20.0','brainspace','seaborn'],
    #   include_package_data=True,
      package_data={'': [
                        'tutorial/example_data/tutorial_data.npy',
                        'misc/cmaps/gradientFlow_cmap.npy',
                        'misc/cmaps/ICC_cmap.npy',
                        'misc/Glasser2016_labels/181Yeo7matchlh.csv',
                        'misc/Glasser2016_labels/181Yeo7matchrh.csv',
                        'misc/Glasser2016_labels/GlasserRegionNames.csv',
                        'misc/Glasser2016_labels/HCP_MMP_P210_10k.dlabel.nii',
                        'misc/surfaces/Conte69.L.very_inflated.10k_fs_LR.surf.gii',
                        'misc/surfaces/Conte69.R.very_inflated.10k_fs_LR.surf.gii'
                        ]
                    }
     )