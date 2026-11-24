# Flood mapping project



**Summary:**

This project uses Sentinel-1 SAR satellite images and a U-Net neural network to identify water areas. The research question is:

"How well does a U-Net trained on Sentinel-1 SAR imagery generalize to flood events in geographically unseen regions?"

The model was trained using images from Sri Lanka and the Mekong region and tested on images from Spain, Somalia as well as the same region as the training. The notebooks can train the model, calculate Water Intersection over Union (IoU) scores and show the actual water areas next to the model's predictions. Different classification thresholds were also tested to see how they affect the results.



**Data Sources:**

The satellite images and corresponding water labels come from the Sen1Floods11 dataset (Bonafilia et al., 2020).

* Dataset description: https://github.com/cloudtostreet/Sen1Floods11
* Data download: shorturl.ly/yQ-Ah
* Satellite data: Sentinel-1 SAR imagery

Each image is a 512 × 512 pixel GeoTIFF file with labels such as 1 = water, 0 = non-water, -1 = invalid pixel.



**Setup Instructions:**

To run the notebooks, Python, Jupyter Notebook and the Python libraries described in the env file are needed.



* The data needed can be download from the Sen1Floods11 bucket (shorturl.ly/yQ-Ah) and then needs to be put into the following folders like described below. More about how to access the data, name it correctly and how to use the python script to automate it, can be found in the data/README.



```text*
project/
├── data/
│   ├── S1Hand/
│   │   ├── Spain_8565131_S1Hand.tif
│   │   └── ...
│   └── LabelHand/
│       ├── Spain_8565131_LabelHand.tif
│       └── ...
├── notebooks/
├── scripts/
├── trainedmodel\_95epochs.pth
├── environment.yml
└── README.md
```

The notebooks etc. use relative paths so downloading the whole project/repository as it is, is recommended.



**Execution Instructions:**

There are three notebooks, one for Sri Lanka/Mekong, one for Spain, and one for Somalia.

If you wish to do the training yourself and not use the pretrained model, then you can just open one of the notebooks and run it from top to bottom. If you are using the saved model however then do not run the training cell again and only run the first three (preparation) and the last three cells (evaluation). The already trained and saved model file is "trainedmodel\_95epochs.pth".



The classification threshold can be changed in the notebooks. The original comparison uses 0.5 for all regions. For Spain 0.3 was also used as it yielded better results. Somalia was evaluated also with 0.09.



**Notes:**

The model identifies water but not necessarily new flooding. This is because the labels do not distinguish between new water or old. It is therefore more of a "water area map".



**AI use:**

Some parts of the notebooks have been created with the help of LLM's but all of the final code and writings have been verified and completed by me.

The script to rename and move the downloaded data ("filetransfer\_renaming") is done fully by ChatGPT and not by myself.



**Reference:**

Bonafilia, D., Tellman, B., Anderson, T., \& Issenberg, E. (2020). *Sen1Floods11: A georeferenced dataset to train and test deep learning flood algorithms for Sentinel-1*. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops.

