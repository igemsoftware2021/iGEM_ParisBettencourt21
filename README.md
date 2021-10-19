# iGEM_ParisBettencourt21
The official repository of iGEM Paris Bettencourt team's software tools.

## Running the program for cell counting
We need a basic python environment and preferably [Miniconda or Anaconda](https://docs.conda.io/en/latest/miniconda.html) as they help keep all the packages modular

- In order to install the required packages for this program, run the following command that uses python3-pip:
`pip3 install -r requirements.txt`

- For cell counting from images that includes both mother and minicells, put them in the Cells folder and run the following command in the main folder containing the .py file
`python cell_count.py -i Cells/mgfp01.JPG`

- For minicell counting (from images that has only minicells filtered), put them in the Minicells folder and run the following command
`python gfpminicell_count.py -i GFPMinicells/1.png`

  **Note:** Cells/mgfp01.JPG and Minicells/1.png are just sample images from the example folders, they could be replaced by GFP microscopic images with the corresponding relative path to the files
