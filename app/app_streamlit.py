
import streamlit as st
import pandas as pd
import numpy as np

f = open("/etc/keys_azure/keyblob", "r")
key_blob=f.read()
st.title('Hello in my first streamlit App :)' + str(key_blob))
