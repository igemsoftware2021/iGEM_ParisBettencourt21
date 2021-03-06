# iGEM_ParisBettencourt21
The official repository of iGEM Paris Bettencourt team's software tools.

## Cell counting
There are two programs dedicated to the cell counting from the GFP images obtained from the experiments.

The first python program(**gfpminicell_count.py**) involves the following image processing techniques
- cleaning by border stripping
- gray-scaling
- gaussian blurring
- binary thresholding for preparing the processed image

The second program(**cell_count.py**) involves additional sharpening and thresholding techniques before gaussian blurring in order to capture the full contours of different sized images. So in sequence, the image goes through cleaning -> gray-scaling -> filter-convolved sharpening -> binary thresholding -> gaussian blurring -> final binary thresholding.

For the final counting, a procedure called [contour mapping from OpenCV](https://docs.opencv.org/4.5.3/d4/d73/tutorial_py_contours_begin.html) is used and the corresponding contours are counted as the number of cells seen on the processed images. 

## Example Images

There are two folders dedicated to store images for each of the two programs described above:
- **Cells** folder consists of sample images containing both mother and minicells and
- **Minicells** folder has Green Fluorescent Protein (GFP) images of only minicells

## Running the program for cell counting
We need a basic python environment and preferably [Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html) as they help keep all the packages modular

- In order to install the required packages for this program, run the following command that uses python3-pip:
`pip3 install -r requirements.txt`

- For minicell counting (from images that has only minicells filtered), put them in the Minicells folder and run the following command
`python gfpminicell_count.py -i GFPMinicells/3.png`

- For cell counting from images that includes both mother and minicells, put them in the Cells folder and run the following command in the main folder containing the .py file
`python cell_count.py -i Cells/mgfp01.JPG`

  **Note:** Cells/mgfp01.JPG and Minicells/1.png are just sample images from the example folders, they could be replaced by GFP microscopic images with the corresponding relative path to the files

## Interpreting results
The program outputs:
- Original border-cropped image: "Cleaned-original image"

![Example: GFPMinicells/3.png](https://drive.google.com/uc?export=view&id=1bNSMWY3YJUErigR02chNzEHq6cpbuRZw) 

- Final processed image on which the contours are mapped and counted: "Contour-ready image"

![Example: Contour-ready3.png](https://drive.google.com/uc?export=view&id=16oQJpK2l2cKbfYkjfxi4PODcSD-PxwV8)

- The number of cells counted in the GFP image: "cell-count" (Also in the window-caption of the processed image)
Example above: cell-count is 18

## Another (Mini)cells count example
![Example: Cells/mgfp01.JPG](https://drive.google.com/uc?export=view&id=1nlJ8HRB027Tzt4OOfzwPzgKS3BS7vlbf)

## Image uploader
 
 The **image_uploading_bot.py** script is dedicated to automated web navigation. 
 It uses the selenium python extensions to 
 - Upload a set of images from a local folder to the igem servers
 - Store the data of the uploaded files for accessible wiki editing 

## Minicell producing culture models 

There are two version of simulation for culture of minicell producing strains:
- Version 1 is an algorithmic approach for low number of cells
- Version 2 is another approach using approximation of partial differential equations

## Version 1

On the first version - **minicell_bioproduction_model_v1.py**, different simulations were implementated according to different assumptions (constant/exponential) of growth of the cell and production rates of mini-cells. The ouputs are graphs of cell-growth and minicell/mothercell counts

## Version 2

On the second version - **minicell_bioproduction_model_v2.py**, a set of differential equations have been used based on growth-fragmentation problem.
The ouputs are graphs of cell-growth and minicell/mothercell counting

Simulated example graphs are below:

![Example: SimulatedGraph1.png](https://drive.google.com/uc?export=view&id=12TEnZkfk2FyDWZrhU7kaQkPhS3kEb3F4)

![Example: SimulatedGraph2.png](https://drive.google.com/uc?export=view&id=1lIFtTahb-01HhQznFOWtZnw4RKbiweHz)
