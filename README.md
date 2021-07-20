# Force-Estimation

## Task
To estimate the force that is *about to be* applied by a surgical robot arm.
* In other models (like in Force-Estimation ref2), we let the machine to learn the force being applied by giving it the video of an object being touched by another object. 
* In our task, we want to combine the information collected from the sensor and the camera to better reconstruct the 3D space and give a more accurate estimation of the force that is about to be applied with neural network compared to estimating using only sensor.

### Baseline model
* The structure of our baseline model uses essentially the same structure of network as mentioned in Force-Estimation ref2.
* The baseline model consists of two parts: a CNN which takes in an image and extracts its feature at a time and a RNN which takes in a sequence of processed images and makes inference based on the time-series data.
* Only the training part of the baseline model was implemented.

### Actual model
* In our actual model (as described in task) the most important difference is that we need to incorporate the data from sensor with our processed images so that the RNN makes inference from both information.
* The task of our CNN is to extract the relative position of our robot arm the the object to which the force is going to be applied. Therefore, a simple CNN like in our baseline model is not exactly for the job. We might want to train our CNN in order to better estiamte the distance (therefore helps reconstructing the spatial information).
* The executation time of our model may be a crucial element in actual application, so we want to keep the model efficient in terms of computation resource. There is intuition that our model should be relatively lightweight: since we already have the most important piece of information for calculating force (acceleration from sensor), the only hard part of the task is to estimate spatial relationship using CNN in order to make the calculation more accurate.
