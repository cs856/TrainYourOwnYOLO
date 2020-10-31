
import gdown
import zipfile
from google.colab import files

#download test_vids.zip
url = 'https://drive.google.com/uc?id=19OVZj6qRr9ygzlZuLaEoLjX584LaYESi'
output = 'test_vids.zip'
gdown.download(url, output, quiet=False) 

#extract test_vids.zip
zip = zipfile.ZipFile("test_vids.zip")
zip.extractall("./Data/Source_Images")


#download data_classes.txt
url = 'https://drive.google.com/uc?id=1G_GgucCbskWZq5umyMS8lVSe3692Ngkc'
output = './Data/Model_Weights/data_classes.txt'
gdown.download(url, output, quiet=False) 


#download the trained final weights
url = 'https://drive.google.com/uc?id=1TRjpUdYQd7RKfmHhm_1oB0u_WIAAs_LY'
output = './Data/Model_Weights/trained_weights_final.h5'
gdown.download(url, output, quiet=False) 



# files.download('./Data/Model_Weights/data_classes.txt') 
#files.download('requirements.txt') 