import pandas as pd
import streamlit as st
import openpyxl
from io import BytesIO
from streamlit_extras.mention import mention
st.set_page_config(page_title="Cleaning Analysis",
    page_icon="🧹",
    layout="wide",
    initial_sidebar_state="expanded"
    )
hide_menu="""
    <style>
    #MainMenu{
        visibility:hidden;
    }
    footer{
        visibility:hidden;
    }
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.header(":green[Information about Cleaning Analysis.]")
st.sidebar.write("The Cleaning Analysis perform's some operation that remove or drop the missing value "
                "that are present in given dataset files. This Analysis gives three option to user to remove missing "
                "values in Dataset. This option's are:")
st.sidebar.write("1). Remove Missing Value's by :green[Column's]")
st.sidebar.write("2). Remove Missing Value's by :green[Row's]")
st.sidebar.write("3). Remove Missing Value's by both :green[Column] and :green[Row]")
st.title(":green[Cleaning Analysis on DataSet]")
st.markdown("---")
left, right = st.columns((2,2))
with left:
    st.subheader("Upload **:green[CSV]** File . . . . ")
    file_uploads = st.file_uploader("", type=['CSV'])
with right:
    st.subheader("Upload **:green[Excel]** File . . . . ")
    excel_file_upload = st.file_uploader("", type=['xlsx'])
st.markdown("---")
if file_uploads is not None:
    df = pd.read_csv(file_uploads)
    st.subheader("Cleaning data for **:red[CSV File]**")
    st.subheader("**:red[{}]** dataSet are . . . ".format(file_uploads.name))
    st.write(df)
    st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
    st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
    st.markdown("---")
    st.header("New DataSet with **:green[Missing Values]** Removed / :green[Cleaned DataSet]")
    missing_values_count = df.columns[df.isnull().any()]
    st.write("###  Missing Value removed by :green[Columns]")
    columns_to_drop = st.multiselect("", missing_values_count)
    if len(columns_to_drop) > 0:
        df = df.drop(columns_to_drop, axis=1)
        st.write(df)
        st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
        st.download_button("Download Data as .CSV", df.to_csv(), file_name='cleaned_data.csv', mime='text/csv')
    st.markdown("---")
    st.write("### Droping Missing Value by :green[Rows]")
    if st.checkbox("Click here to Drop the missing value Rows"):
        df = df.dropna()
        st.write(df)
        st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
        st.download_button("Download Data as .CSV", df.to_csv(), file_name='cleaned_data.csv', mime='text/csv')
    st.markdown("---")
    missing = df.columns[df.isnull().any()]
    st.write("### Cleand Data for both :green[Column and Row]")
    columns_for_both = st.multiselect(":red[First Select Columns. . . .] ", missing)
    if len(columns_for_both) > 0:
        df = df.drop(columns_for_both, axis=1)
    if st.checkbox("Click here to Show Cleand data"):
        df = df.dropna()
        st.write(df)
        st.write("The :green[Row No.] of Dataset is: ",df.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",df.shape[1])
        st.download_button("Download Data as .CSV", df.to_csv(), file_name='cleaned_data.csv', mime='text/csv')
    st.markdown("---")
st.text("")
st.text("")
if excel_file_upload is not None:
    dfs = pd.read_excel(excel_file_upload, engine='openpyxl')
    st.subheader("Cleaning data for **:red[Excel File]**")
    st.subheader("**:red[{}]** dataSet are . . . ".format(excel_file_upload.name))
    st.write(dfs)
    st.write("The :green[Row No.] of Dataset is: ",dfs.shape[0])
    st.write("The :green[Column No.] of Dataset is: ",dfs.shape[1])
    st.markdown("---")
    st.header("New DataSet with **:green[Missing Values]** Removed / :green[Cleaned DataSet]")
    missing_values_count = dfs.columns[dfs.isnull().any()]
    st.write("###  Droping Missing Value by :green[Columns]")
    columns_to_drop = st.multiselect("", missing_values_count)
    if len(columns_to_drop) > 0:
        dfs = dfs.drop(columns_to_drop, axis=1)
        st.write(dfs)
        st.write("The :green[Row No.] of Dataset is: ",dfs.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",dfs.shape[1])
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        dfs.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_descen_percent.xlsx',key=8)
    st.markdown("---")
    st.write("### Droping Missing Value by :green[Rows]")
    if st.checkbox("Click here to Drop the missing value Rows"):
        dfs = dfs.dropna()
        st.write(dfs)
        st.write("The :green[Row No.] of Dataset is: ",dfs.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",dfs.shape[1])
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        dfs.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_descen_percent.xlsx',key=9)
    st.markdown("---")
    missing = dfs.columns[dfs.isnull().any()]
    st.write("### Droping Missing value for both :green[Column and Row]")
    columns_for_both = st.multiselect(":red[First Select Columns. . . .] ", missing)
    if len(columns_for_both) > 0:
        dfs = dfs.drop(columns_for_both, axis=1)
    if st.checkbox("Click here to Show Cleand data"):
        dfs = dfs.dropna()
        st.write(dfs)
        st.write("The :green[Row No.] of Dataset is: ",dfs.shape[0])
        st.write("The :green[Column No.] of Dataset is: ",dfs.shape[1])
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        dfs.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_descen_percent.xlsx')
    st.markdown("---")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.subheader("Reach out to me for any :red[Suggestion/Feedback]")
left, right = st.columns((2,8))
with left:
    mention(
    label="LinkedIn",
    icon="https://img.freepik.com/premium-vector/linkedin-logo_578229-227.jpg?w=740",
    url="https://www.linkedin.com/in/pawan-dabi-a42a081b7/",
    )
with right:
    mention(
    label="Instagram",
    icon="https://www.freepnglogos.com/uploads/logo-ig-png/logo-ig-instagram-new-logo-vector-download-13.png",
    url="https://www.instagram.com/pawan_dabi_001/",
    )
