## Directory Structure

IntroToCalciumImaging </br>
|-- data </br>
|-- notebooks </br>
|-- scratch

`data/`: all relevant data for the notebooks </br>
`notebooks/`: notebooks for course </br>
`scratch/`: any learning projects or notes that might help in notebook preparation

## Notebooks (Planned)

1. TIFF File 
2. Image processing (summary images, high pass spatial filtering with OpenCV) 
3. Image registration with Scikit-image
4. CaImAn pre-processing steps 
5. Talk/CaImAn movie handling (depends on Eric Thomson's availability)
6. Talk/CaImAn movie handling (depends on Eric Thomson's availability)
7. CaImAn Motion Correction
8. CaImAn Source Extraction (2p imaging)
9. CaImAn Source Extraction (1p imaging)
10. Deconvolution with Oasis (or Retroscpective or bring your own dataset) 


## Other ideas (Anything that comes to mind)

1. Registration with scikit-image
2. Deconvolution with Oasis (oasis-deconvolve)
3. CaImAn Movie Handling
4. High Pass and Low Pass Spatial Filtering with CV2
5. Making summary images with Numpy
6. CaImAn Logger
7. Handling moving in formats other than TIF
8. Loading multiple files or data collected in noncontiguous sessions
9. Loading only *n* frames of a large file with movie object `subindices`
10. Using change_params() to iteratively change params for CNMF model fitting
11. Estimates class exploration (e.g., recover raw calcium traces, background models)
12. nb_view_components customization

## To Learn

1. [jnormcorre](https://github.com/apasarkar/jnormcorre)
2. [funimag](https://github.com/paninski-lab/funimag)


## Milestone meeting

1. Make Bokeh app for pre-processing steps (gaussian filter etc)
2. From calcium traces to viz (like in Screenshot 2024-02-05 144351.png)
3. Notebook on different file formats
4. Unit on Numpy arrays (make an array, save it, load and compare) 
