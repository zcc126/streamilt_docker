# Import streamlit 
import streamlit as st
import pandas as pd
import numpy as np
#import os
#key_blob=os.environ["KEY_BLOB"]
f = open("/etc/keys_azure/keyblob", "r")
key_blob=f.read()
st.title('Hello in my first streamlit App :)' + str(key_blob))
