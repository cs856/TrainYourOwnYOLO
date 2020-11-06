
import gdown
import zipfile
from google.colab import files


############ baby detector ############
# # download test_vids.zip
# url = 'https://drive.google.com/uc?id=19OVZj6qRr9ygzlZuLaEoLjX584LaYESi'
# output = 'test_vids.zip'
# gdown.download(url, output, quiet=False) 

# #extract test_vids.zip
# zip = zipfile.ZipFile("test_vids.zip")
# zip.extractall("./Data/Source_Images")

# #download data_classes.txt
# url = 'https://drive.google.com/uc?id=1G_GgucCbskWZq5umyMS8lVSe3692Ngkc'
# output = './Data/Model_Weights/data_classes.txt'
# gdown.download(url, output, quiet=False) 

# #download the trained final weights - uppper body
# url = 'https://drive.google.com/uc?id=1hXy_1_gBaQLiH9ef78Nhg1EB1MUq6I9x'
# output = './Data/Model_Weights/trained_weights_final.h5'
# gdown.download(url, output, quiet=False) 


############ facemask detector ############
#download test_vids.zip
url = 'https://drive.google.com/uc?id=1qWVqrdUX4x4Nff1IW0_-BNgIh18Ua32Z'
output = 'test_vids.zip'
gdown.download(url, output, quiet=False) 

#extract test_vids.zip
zip = zipfile.ZipFile("test_vids.zip")
zip.extractall("./Data/Source_Images/Test_Images")

#download data_classes.txt
url = 'https://drive.google.com/uc?id=1-O3rUenD3tQUI2zQsA4dTULC43XBFNUG'
output = './Data/Model_Weights/data_classes.txt'
gdown.download(url, output, quiet=False) 

#download the trained final weights
url = 'https://drive.google.com/uc?id=1xCrb0r-edPccjNGzIaEH_Q-6del5OgPV'
output = './Data/Model_Weights/trained_weights_final.h5'
gdown.download(url, output, quiet=False) 
