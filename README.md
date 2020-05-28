# RSML-to-Image (Annotataions)
This script written to produce image base annotations/Ground Truth (GT) from RSML files. It takes an RSML file along with the original input image and generates Color-coded GT. You can also tweak it to work with the (only) RSML file. 

## Installing 
You will first need to download the code, either as a zip above, or by cloning the git repository (recommended):
```
https://github.com/robail-yasrab/RSML-to-Image.git
```
Next, install the required dependencies (cv2 and numpy). :
```
cd RSML-to-Image
pip install opencv-python
pip install numpy
```
## Using the tool
Set Input and Output directory paths in the script and run the following command. 
```
python RSML_to_annotations.py
```
