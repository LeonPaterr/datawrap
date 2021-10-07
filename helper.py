import streamlit as st
import base64
import os

def header(text,
           is_sidebar = False):
    '''
     A function to neatly display headers in app.
    Parameters
    ----------
    text : Text to display as header
    Returns
    -------
    A header defined by html5 code below.
    '''
    html_temp = f"""
    <h1 style = "color:#F26531; text_align:left; font-weight: bold;"> {text} </h1>
    </div>
    """
    
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else:
        st.markdown(html_temp, unsafe_allow_html = True)

def ntext(text,
           is_sidebar = False):
    '''
     A function to neatly display headers in app.
    Parameters
    ----------
    text : Text to display as header
    Returns
    -------
    A header defined by html5 code below.
    '''
    html_temp = f"""
    <h3 style = "color:white; text_align:left;"> {text} </h3>
    </div>
    """
    
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else:
        st.markdown(html_temp, unsafe_allow_html = True)
        
def set_bg():

        
    st.markdown(
         f"""
         <style>
         .reportview-container {{
             background: #12abdb
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

#DOWNLOAD CSV def
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False, sep = ";")
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="modelmapping.csv"><input type="button" value="DOWNLOAD CSV FILE"></a>'
    return href

def get_binary_file_link(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"><input type="button" value="DOWNLOAD ZIP">'
    return href



