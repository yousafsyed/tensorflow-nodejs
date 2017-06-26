
# Create Image Classifier Director 

Like follwing

 /-person
 	/-data
 		/-Jinnah
 		/-Gandhi



# Run the following command to train the image classifier

Following command will download the image classifier image from docker and then run the entry point with your mounted classifier dir


docker run -v /Users/yousafsyed/Documents/tensorflow/person:/tf_files -it yousaf/retrain_image:1.0

-v tag will mount the classier in /tf_files which is required for the docker container to run