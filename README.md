# Optical-CharacterRecognition

* The main aim of the project was to recognize hand written digits. The Training data set was in the form of 28X28 matrix with each cell representing a pixel ranging from 0-255. The images were normalised and in a grey scale format.
Classified MNIST Dataset Images (28*28 pixels each in a .csv file) with an accuracy of
83% using Support Vector Machine (SVM).

* Tool Used - Support Vector Machine Library (LIBSVM)
* Programming Language - Python

# Step by Step Approach Explained:

* We have used SVM i.e. Support Vector Machine for classification purpose. We have made use of LIBSVM package to implement the functions of SVM such as generating training model, predicting output, finding accuracy, etc. We tried various SVM parameters and obtained 83% accuracy by using SVM with polynomial kernel of degree two and number of features = 784.

[1] Generating Feature Vector
The “svm-train.c” assumes that the format of training and testing data file is:
   <label> <index1>:<value1> <index2>:<value2> ...

Where label is the expected output and <index> are those indices which have value not equal to 0. <value> gives the value at that index. This is done to generate a dense feature vector. 

Therefore we generate a feature vector for the training data set and then use “svm-train” to generate a trained model( we have called it libsvmtrain).

We generate model using following command:
       svm-train –d 2 –t 1 –g 0.0012755102 libsvmtrain.data

      -t kernel_type : set type of kernel function (default 2)
	0 -- linear: u'*v
	1 -- polynomial: (gamma*u'*v + coef0)^degree
	2 -- radial basis function: exp(-gamma*|u-v|^2)
	3 -- sigmoid: tanh(gamma*u'*v + coef0)
	4 -- precomputed kernel (kernel values in training_set_file)

     -d degree : set degree in kernel function (default 3)

     -g gamma : set gamma in kernel function (default 1/num_features)
     
The model generated is called “libsvmtrain.data.model”.

A python script (csv2libsvm.py) was used to convert ocp_training.csv  to libsvmtrain.data.

[2]  Checking  Accuracy of the Model Generated

Svm-predict.c was used to predict how accurate results the model generated. Svm-predict assumes that the first column is the label while the rest is input. Therefore we append the “sampleoutput” file to “sampleinput”  file to generate a file called “outin”. Python script (combine_input_output.py) was used.

We run svm-predict by:

Svm-predict outin libsvmtrain.data.model  83%_accurate_output_of_sample_input

[3] Generating Solution to Testing File ( 83% accurate)

We append 0 to the first column of testing file(ocp_testing.csv) using a python script (convert_test.py)  because svm-predict assumes first column as label.The new file generated is 
We give the command:

Svm-predict libsvmtest.data libsvmtrain.data.model  Solution

IMPORTANT NOTE-

Here “Accuracy” is also shown on terminal but that is not the actual accuracy. Beacause we have appended 0 at beginning, it checks output with zero eveytime. The output to testing is in Solution File.The actual Accuracy comes when you run svm-predict with outin as this file contains both input and output so it matces the output with first column.The accuracy comes out to be 83 % infact.

The “Solution” contains the final output.

The Usage of Python files is given in the ReadME file in the Python files Folder. !! Solution File contains the answer obtained after running testing file(libsvmtest.data).
