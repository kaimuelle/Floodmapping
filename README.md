# Flood mapping project



**Summary:**

This project uses Sentinel-1 SAR satellite images and a U-Net neural network to identify water areas. The research question is: 

"How well does a U-Net trained on Sentinel-1 SAR imagery generalize to flood events in geographically unseen regions?"

The model was trained using images from Sri Lanka and the Mekong region and tested on images from Spain, Somalia as well as the same region as the training. The notebooks can train the model, calculate Water Intersection over Union (IoU) scores and show the actual water areas next to the model's predictions. Different classification thresholds were also tested to see how they affect the results.



**Data Sources:**

The satellite images and corresponding water labels come from the Sen1Floods11 dataset (Bonafilia et al., 2020).

* Dataset: https://github.com/cloudtostreet/Sen1Floods11
* Satellite data: Sentinel-1 SAR imagery

Each image is a 512 × 512 pixel GeoTIFF file with labels such as 1 = water, 0 = non-water, -1 = invalid pixel



**Setup Instructions:**

To run the notebooks, Python, Jupyter Notebook and the following Python libraries are required:

* numpy
* matplotlib
* rasterio
* torch (PyTorch)
* segmentation-models-pytorch



Download the required Sen1Floods11 images and put them into the following folders like so:



*project/*

*├── data/*

*│   ├── S1Hand/*

*│   │   	├── Spain\_8565131\_S1Hand.tif*

*│   │  	   └── ...*

*│   └── LabelHand/*

*│      	   ├── Spain\_8565131\_LabelHand.tif*

*│     	  └── ...*

*├── floodproject\_mekongsrilanka.ipynb*

*├── floodproject\_spain.ipynb*

*├── floodproject\_somali.ipynb*

*├── unet\_95epochs.pth*

*└── README.md*



If necessary rename the downloaded files so that the image IDs match the format used in the notebooks (like above). Run the notebooks from the project folder because the code uses relative paths.

For testing without retraining, the saved model file "unet\_95epochs.pth" is available in the project folder. 



**Execution Instructions:**

There are three notebooks, one for Sri Lanka/Mekong, one for Spain, and one for Somalia.

If you wish to do the Training yourself and not use the pretrained model, then you can just open one of the notebooks and run it from top to bottom. If you are using the saved model however then do not run the training cell again and only run the first three (preparation) and the last three cells (evaluation).



The classification threshold can be changed in the notebooks. The original comparison uses 0.5 for all regions. For spain 0.3 was also used as it yielded better results. Somalia was evaluated also with 0.09.



**Notes:**

The model identifies water but not necessarily new flooding. This is because the labels do not distinguish between new water or old. It is therefore more of a "water area map".



**Reference:**

Bonafilia, D., Tellman, B., Anderson, T., \& Issenberg, E. (2020). *Sen1Floods11: A georeferenced dataset to train and test deep learning flood algorithms for Sentinel-1*. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops.



