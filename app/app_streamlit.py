import streamlit as st
import pandas as pd
import numpy as np
import os
from azure.storage.blob import BlobServiceClient
from io import StringIO

key_blob=os.environ["KEY_BLOB"]
url_blob=os.environ["URL_BLOB"]
local_file_name="Airlines.csv"
container_name="airline"

st.title('Hello in my first streamlit App :)')


blob_service_client_instance = BlobServiceClient(account_url=url_blob, credential=key_blob)
blob_client_instance = blob_service_client_instance.get_blob_client(container_name, local_file_name, snapshot=None)

with open(local_file_name, "wb") as my_blob:
    blob_data = blob_client_instance.download_blob()
    blob_data.readinto(my_blob)
dataframe_blobdata = pd.read_csv(local_file_name)
st.dataframe(dataframe_blobdata.head(5))
