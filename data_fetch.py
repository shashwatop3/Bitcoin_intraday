import gdown

# Define the Google Drive direct download link
url = 'https://drive.google.com/uc?id=1p6wOzt7PR9onf2f5oo_Q3Vn6g0bosnQL'

# Define the destination path where the file will be saved
destination = 'data/btcusd_15min_preprcd.parquet'

# Download the file from Google Drive
gdown.download(url, destination, quiet=False)
