import pandas as pd
import streamlit as st
from io import BytesIO
import xlsxwriter
import openpyxl
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
st.set_page_config(page_title="Exploratory Data Analysis . Streamlit",
    page_icon="https://cdn-icons-png.flaticon.com/512/3090/3090011.png",
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

st.cache(persist=True)
st.sidebar.header("Operations on Given DataSet.")
option_name = ["", "Head", "Tail", "Summery", "Column Name", "Row No", "Column No",
               "Numeric Data", "Missing Values", "Missing Values per Column", "Missing Value(Column %)", "Count"]

op_column_name = st.sidebar.selectbox("**:green[Information About Operations on Given DataSet]**", option_name)
if op_column_name == 'Head':
    st.sidebar.write("**:green[{name}]**:  The :red[head dataset] method returns the first 5 rows if a number is not specified."
                    " if any number has been given the it will written number of rows that you have been given".format(name='Head'))
elif op_column_name == 'Tail':
    st.sidebar.write("**:green[{name}]**: The :red[tail dataset] method returns the last 5 rows if a number is not specified. "
                     " if any number has been given the it will written number of rows that you have been given".format(name='Tail'))
elif op_column_name == 'Summary':
    st.sidebar.write("**:green[{name}]**:  The :red[summary] method returns description of the data in the DataFrame. "
                     "If the DataFrame contains numerical data " .format(name='Summery'))
elif op_column_name == 'Column Name':
    st.sidebar.write("**:green[{name}]**:  It can be thought of as a dict-like container for Series objects. "
                     "This is the primary data structure of the Pandas. :red[DataFrame.columns] columns attribute return the column "
                     "labels of the given Dataframe.".format(name='Column Name'))
elif op_column_name == 'Row No':
    st.sidebar.write("**:green[{name}]**: The :red[Row No.] shows the number of rows in DataSet.".format(name='Row No'))
elif op_column_name == 'Column No':
    st.sidebar.write("**:green[{name}]**: The :red[Column No] shows the number of columns in dataset".format(name='Column No'))
elif op_column_name == 'Numeric Data':
    st.sidebar.write("**:green[{name}]**: The :red[Numeric Data] method returns a new DataFrame that includes/excludes columns of "
                     " The specified dtype(s)." "Note: You must specify at least one of the parameters include and/or exclude, "
                     "or else you will get an error.".format(name='Numeric Data'))
elif op_column_name == 'Missing Values':
    st.sidebar.write("**:green[{name}]**: The :red[Missing Value] method returns a DataFrame object where all the values "
                     "are replaced with a Boolean value True for NA (not-a-number) values, and otherwise False.".format(name='Missing Values'))
elif op_column_name == 'Missing Values per Column':
    st.sidebar.write("**:green[{name}]**: The :red[Missing Values per Column] returns the number of missing values in each column."
                     .format(name='Missing Values per Column'))
elif op_column_name == 'Missing Value(Column %)':
    st.sidebar.write("**:green[{name}]**: The :red[Missing Value(%)] will shows the percentage of missing value of each column. "
                     .format(name='Missing Value(Column %)'))
elif op_column_name == 'Count':
    st.sidebar.write("**:green[{name}]**: The :red[count] method counts the number of not empty values for each row, or column".format(name='Count'))
st.cache(persist=True)
st.title(":green[Streamlit EDA] : A :red[WebApp] for Efficient :green[Data Analysis .] ")
st.markdown("---")
st.cache(persist=True)
left, right = st.columns((2,2))
with left:
    st.subheader("Upload **:green[CSV]** File . . . . ")
    file_upload = st.file_uploader("", type=['CSV'])
with right:
    st.subheader("Upload **:green[Excel]** File . . . . ")
    file_upload_1 = st.file_uploader("", type=['xlsx'])
st.markdown("---")
df=None
if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.session_state.df = df
    st.session_state.file_upload=file_upload
    if file_upload:
        st.subheader("**:red[{}]** dataSet are . . . ".format(file_upload.name))
        st.write(df)
        st.markdown("---")
        st.header("Basic Operation on Given **:green[CSV]** DataSet File . . . . ")
        tabs = st.tabs(["Head DataSet", "Tail DataSet", "Summary", "Columns", "Row/Column No.", "Numeric Data Column",
        "Missing Values", "Missing Values per Column", "Missing Value(%)", "Count"])
        with tabs[0]:
            number_head = st.number_input(":green[Enter the No. of Head Rows] ", step=0, format='%d')
            head_dataset = df.head(number_head)
            st.write(head_dataset)
            st.download_button("Download Data as .CSV", head_dataset.to_csv(), file_name='head_dataset.csv', mime='text/csv')
        with tabs[1]:
            number_tail = st.number_input(":green[Enter the No. of Tail Rows]  ", step=0, format='%d')
            tail_dataset = df.tail(number_tail)
            st.write(tail_dataset)
            st.download_button("Download Data as .CSV", tail_dataset.to_csv(), file_name='tail_dataset.csv', mime='text/csv')
        with tabs[2]:
            num = ['float64', 'int64']
            numeric_summary = df.describe(include=num)
            st.write(":green[Summary for Numeric Columns]")
            st.write(numeric_summary)
            st.download_button("Download Data as .CSV", numeric_summary.to_csv(), file_name='numeric_dataset.csv', mime='text/csv')
            cat = 'object'
            cat_summary = df.describe(include=cat)
            st.write(":green[Summary for Categorical Column]")
            st.write(cat_summary)
            st.download_button("Download Data as .CSV", cat_summary.to_csv(), file_name='catgorical_dataset.csv', mime='text/csv')
        with tabs[3]:
            st.write(":green[Name of Columns] in DataSet: ")
            st.write(df.columns)
        with tabs[4]:
            st.write("No. of :green[Row] in DataSet: ")
            st.write(df.shape[0])
            st.write("No. of :green[Columns] in DataSet: ")
            st.write(df.shape[1])
        with tabs[5]:
            numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
            no_of_numeric = df.select_dtypes(include=numerics)
            st.write("No of :green[Numeric Data] in DataSet: ")
            st.write(len(no_of_numeric.columns))
            st.write(no_of_numeric)
            st.download_button("Download Data as .CSV", no_of_numeric.to_csv(), file_name='numeric_dataset.csv', mime='text/csv')
        with tabs[6]:
            st.write(":green[Column Name Contains Missing Value]")
            miss_col = df.columns[df.isnull().any()]
            st.write(miss_col)
            empty_dataset = df.isnull()
            st.write(empty_dataset)
            st.download_button("Download Data as .CSV", empty_dataset.to_csv(), file_name='missing_dataset.csv', mime='text/csv')
        with tabs[7]:
            st.write("Shows the :green[Missing Values Per Columns] in DataSet: ")
            missing_value_dataset = df.isna().sum()
            st.write(missing_value_dataset)
            st.download_button("Download Data as .CSV", missing_value_dataset.to_csv(), file_name='missing_column_dataset.csv', mime='text/csv')
            sort_data = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
            with sort_data[0]:
                st.write("Sorted in :green[Ascending Order] from DataSet ")
                missing_value_ascen_dataset = df.isna().sum().sort_values()
                st.write(missing_value_ascen_dataset)
                st.download_button("Download Data as .CSV", missing_value_ascen_dataset.to_csv(), file_name='missing_column_ascen_dataset.csv',
                                   mime='text/csv')
            with sort_data[1]:
                st.write("Sorted in :green[Descending Order] from DataSet ")
                missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
                st.write(missing_value_descen_dataset)
                st.download_button("Download Data as .CSV", missing_value_descen_dataset.to_csv(), file_name='missing_column_descen_dataset.csv',
                                   mime='text/csv')
        with tabs[8]:
            st.write("Show the :green[Percentage] of Missing Values of Each Column: ")
            df_missing_percentage = df.isna().sum() / len(df) * 100
            st.write(df_missing_percentage)
            st.download_button("Download Data as .CSV", df_missing_percentage.to_csv(), file_name='percentage_column_dataset.csv',
                               mime='text/csv')
            missing_value_sorted = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
            with missing_value_sorted[0]:
                df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
                st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Ascending Order]:")
                st.write(df_missing_percentage_Ascending)
                st.download_button("Download Data as .CSV", df_missing_percentage_Ascending.to_csv(),
                                   file_name='percentage_column_ascending_dataset.csv',
                                   mime='text/csv')
            with missing_value_sorted[1]:
                df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
                st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Descending Order]: ")
                st.write(df_missing_percentage_Descending)
                st.download_button("Download Data as .CSV", df_missing_percentage_Descending.to_csv(),
                                   file_name='percentage_column_descending_dataset.csv',
                                   mime='text/csv')

        with tabs[9]:
            st.write("Shows the :green[Non Empty Values] of Each Column and Row in DataSet:")
            empty_value = df.count()
            st.write(empty_value)
            st.download_button("Download Data as .CSV", empty_value.to_csv(),
                               file_name='empty_value.csv',
                               mime='text/csv')
            missing_value_sort = st.tabs(['Sort in Ascending Order', 'Sort in Descending Order'])
            with missing_value_sort[0]:
                df_missing_non_empty_ascending = df.count().sort_values()
                st.write("Shows the Sorted :green[Non Empty Value] in :green[Ascending Order]: ")
                st.write(df_missing_non_empty_ascending)
                st.download_button("Download Data as .CSV", df_missing_non_empty_ascending.to_csv(),
                                   file_name='df_missing_non_empty_ascending.csv',
                                   mime='text/csv')
            with missing_value_sort[1]:
                df_missing_non_empty_descending = df.count().sort_values(ascending=False)
                st.write("Shows teh Sorted :green[Non Empty Value] in :green[Descending Order]: ")
                st.write(df_missing_non_empty_descending)
                st.download_button("Download Data as .CSV", df_missing_non_empty_descending.to_csv(),
                                   file_name='df_missing_non_empty_descending.csv',
                                   mime='text/csv')
if file_upload_1 is not None:
    df2 = pd.read_excel(file_upload_1, engine='openpyxl')
    st.session_state.df2=df2
    st.session_state.file_upload_1=file_upload_1
    if file_upload_1:
        st.subheader("**:red[{}]** dataSet are . . . ".format(file_upload_1.name))
        st.write(df2)
        st.markdown("---")
        st.header("Basic Operation on Given **:green[Excel]** DataSet File . . . . ")
        tabs = st.tabs(["Head DataSet", "Tail DataSet", "Summary", "Columns", "Row/Column No.", "Numeric Data Column",
                        "Missing Values", "Missing Values per Column", "Missing Value(%)", "Count"])
        with tabs[0]:
            number_head = st.number_input(":green[Enter the No. of Head Rows]", step=0, format='%d')
            head_dataset = df2.head(number_head)
            st.write(head_dataset)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            head_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='head_dataset.xlsx')
            #st.download_button("Download CSV File ", head_dataset.to_excel(file_upload_1, index=False), file_name='head_dataset.xlsx')
        with tabs[1]:
            number_tail = st.number_input(":green[Enter the No. of Tail Rows] ", step=0, format='%d')
            tail_dataset = df2.tail(number_tail)
            st.write(tail_dataset)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            tail_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='tail.dataset.xlsx',key=1)
        with tabs[2]:
            num = ['float64', 'int64']
            numeric_summary = df2.describe(include=num)
            st.write(":green[Summary for Numeric Columns]")
            st.write(numeric_summary)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            numeric_summary.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='summary.xlsx',key=2)
            cat = 'object'
            cat_summary = df2.describe(include=cat)
            st.write(":green[Summary for Categorical Column]")
            st.write(cat_summary)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            cat_summary.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='category_summary.xlsx', key=3)
        with tabs[3]:
            st.write(":green[Name of Columns] in DataSet: ")
            st.write(df2.columns)
        with tabs[4]:
            st.write("No. of :green[Row] in DataSet: ")
            st.write(df2.shape[0])
            st.write("No. of :green[Columns] in DataSet: ")
            st.write(df2.shape[1])
        with tabs[5]:
            numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
            no_of_numeric = df2.select_dtypes(include=numerics)
            st.write("No of :green[Numeric Data] in DataSet: ")
            st.write(len(no_of_numeric.columns))
            st.write(no_of_numeric)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            no_of_numeric.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='Numeric_no.xlsx',key=4)
        with tabs[6]:
            st.write(":green[Column Name Contains Missing Value]")
            miss_col = df2.columns[df2.isnull().any()]
            st.write(miss_col)
            empty_dataset = df2.isnull()
            st.write(empty_dataset)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            empty_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value.xlsx',key=5)
        with tabs[7]:
            st.write("Shows the :green[Missing Values Per Columns] in DataSet: ")
            missing_value_dataset = df2.isna().sum()
            st.write(missing_value_dataset)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            missing_value_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_percent.xlsx',key=6)
            sort_data = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
            with sort_data[0]:
                st.write("Sorted in :green[Ascending Order] from DataSet ")
                missing_value_ascen_dataset = df2.isna().sum().sort_values()
                st.write(missing_value_ascen_dataset)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                missing_value_ascen_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_ascen_percent.xlsx',key=7)
            with sort_data[1]:
                st.write("Sorted in :green[Descending Order] from DataSet ")
                missing_value_descen_dataset = df2.isna().sum().sort_values(ascending=False)
                st.write(missing_value_descen_dataset)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                missing_value_descen_dataset.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_descen_percent.xlsx',key=8)
        with tabs[8]:
            st.write("Show the :green[Percentage] of Missing Values of Each Column: ")
            df_missing_percentage = df2.isna().sum() / len(df2) * 100
            st.write(df_missing_percentage)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df_missing_percentage.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_value_column.xlsx',key=9)
            missing_value_sorted = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
            with missing_value_sorted[0]:
                df_missing_percentage_Ascending = df2.isna().sum().sort_values() / len(df2) * 100
                st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Ascending Order]:")
                st.write(df_missing_percentage_Ascending)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df_missing_percentage_Ascending.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_ascen_percent.xlsx',key=10)
            with missing_value_sorted[1]:
                df_missing_percentage_Descending = df2.isna().sum().sort_values(ascending=False) / len(df2) * 100
                st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Descending Order]: ")
                st.write(df_missing_percentage_Descending)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df_missing_percentage_Descending.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='missing_percent_Descending.xlsx',key=11)
        with tabs[9]:
            st.write("Shows the :green[Non Empty Values] of Each Column and Row in DataSet:")
            empty_value = df2.count()
            st.write(empty_value)
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            empty_value.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='empty_value.xlsx',key=12)
            missing_value_sort = st.tabs(['Sort in Ascending Order', 'Sort in Descending Order'])
            with missing_value_sort[0]:
                df_missing_non_empty_ascending = df2.count().sort_values()
                st.write("Shows the Sorted :green[Non Empty Value] in :green[Ascending Order]: ")
                st.write(df_missing_non_empty_ascending)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df_missing_non_empty_ascending.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='ascen_empyt_value.xlsx',key=13)
            with missing_value_sort[1]:
                df_missing_non_empty_descending= df2.count().sort_values(ascending=False)
                st.write("Shows teh Sorted :green[Non Empty Value] in :green[Descending Order]: ")
                st.write(df_missing_non_empty_descending)
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df_missing_non_empty_ascending.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.save()
                processed_data = output.getvalue()
                button = st.download_button(label='Download Data as .XLSX', data=processed_data, file_name='descen_empty_value.xlsx',key=14)
