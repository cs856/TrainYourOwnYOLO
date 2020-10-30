# from google_drive_downloader import GoogleDriveDownloader as gdd

# gdd.download_file_from_google_drive(file_id='1jGtYIExXrUq7YxZaeAhwtbbkpZrv5rrN',
#                                     dest_path='./Data',
#                                     unzip=True)

#                                    # https://drive.google.com/file/d/1jGtYIExXrUq7YxZaeAhwtbbkpZrv5rrN/view?usp=sharing

#                                    #https://drive.google.com/drive/folders/17AecqojNwKaqQB2cHKXCWx6GERpwkGNM?usp=sharing



import gdown

url = 'https://drive.google.com/uc?id=1jGtYIExXrUq7YxZaeAhwtbbkpZrv5rrN'
output = 'temp1'
gdown.download(url, output, quiet=False) 