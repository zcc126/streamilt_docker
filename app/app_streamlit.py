# Import streamlit 
import streamlit as st
import pandas as pd
import numpy as np
import os

key_blob=os.environ["KEY_BLOB"]

st.title('Hello in my first streamlit App :)' + key_blob)
