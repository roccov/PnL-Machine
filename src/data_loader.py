import pandas as pd
import os

RAW_DIR   = os.path.join(os.path.dirname(__file__), "../data_raw") 
#Point to the folder where we keep the original downloads

PROCESSED = os.path.join(os.path.dirname(__file__), "../data_processed")
#Points to the folder where we save cleaned or transformed data

raw_crsp_path = os.path.join(RAW_DIR, "monthly_crsp.csv")
crsp_preview = pd.read_csv(raw_crsp_path, nrows=5) 



