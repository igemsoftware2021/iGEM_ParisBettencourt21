# iGEM_ParisBettencourt21
The official repository of iGEM Paris Bettencourt team's software tools.

## Cell counting
There are two programs dedicated to the cell counting from the GFP images obtained from the experiments.

The first python program(**gfpminicell_count.py**) involves the following image processing techniques
- cleaning by border stripping
- gray-scaling
- gaussian blurring
- binary thresholding for preparing the processed image

The second program(**cell_count.py**) involves additional sharpening and thresholding techniques before gaussian blurring in order to capture the full contours of different sized images. So the in sequence the image goes through cleaning -> gray-scaling -> filter-convolved sharpening -> binary thresholding -> gaussian blurring -> final binary thresholding.

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




## Image uploading
 
 There is one script dedicated to automatized web navigation. 
 It uses the selenium python extensions to 
 - upload a set of image from a local file to the igem servers
 - store the data of the uploaded file for accessible wiki editing
 
