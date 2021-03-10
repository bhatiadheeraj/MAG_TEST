from rake_nltk import Rake


# /* file for testing purposes */
title = "HCP 7T / Diffusion"
desc = "Human Connectome Project Datasets - Diffusion MRI 3T (184 out of 1200-subjects-data-release) and T1/Freesurfer"
readme = "https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release\n\nThe 1200 Subjects Release (S1200) includes behavioral and 3T MR imaging data from 1206 healthy young adult participants (1113 with structural MR scans) collected in 2012-2015. In addition to 3T MR scans, 184 subjects have multimodal 7T MRI scan data and 95 subjects also have some resting-state MEG (rMEG) and/or task MEG (tMEG) data available. For the first time, 3T MRI and behavioral retest data for 46 subjects is also available. \n\nOnly unprocessed Diffusion data was released as part of the Initial 7T Release (June 2016). For all 7T subjects with dMRI scans, 7T dMRI data preprocessed v3.19.0 version of the diffusion pipeline is now available. \n\n## Data Use Terms\n\nTo use these datasets, you must register at [ConnectomeDB](https://db.humanconnectome.org) and agree to the [HCP Data Use Terms](https://store.humanconnectome.org/data/data-use-terms/). \n\n## qc_ tags\n\nqc_ tags are used to indicate subjects with various quality control issues. \n\n* qc_a: Anatomical anomalies \n* qc_b: Segmentation and Surface QC\n* qc_c: Some of subject’s data acquired during a period of instabilities in the head coil\n* qc_d: rfMRI scans with prominent artifact in MPP data (but cleaned appropriately by FIX)\n* qc_e: Manual reclassification of some FIX-ICA components\n\nPlease see https://wiki.humanconnectome.org/pages/viewpage.action?pageId=88901591 for more."

r = Rake()

r.extract_keywords_from_text(readme)

related = r.get_ranked_phrases()

for x in related:
    print(x)