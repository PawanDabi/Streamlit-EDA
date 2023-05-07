import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
st.set_page_config(page_title="Quantitative Statistics",
    page_icon="📉",
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
st.sidebar.header("Information About Quantitative Statistics Graphs.")
graph_option = ["", "Dist Plot", "Line Graph", "Histogram Graph",
                "Scatter Graph", "Box Plot", "Kde Plot"]
op_column_name = st.sidebar.selectbox("**:green[Brief Description About Graph's]**", graph_option)
if op_column_name == 'Dist Plot':
    st.sidebar.write("**:green[{name}]**:  The seaborn :red[Dist Graph] or distribution plot, depicts the variation in the data distribution. "
                     "Seaborn Distplot represents the overall distribution of continuous data variables. "
                     "The Seaborn module along with the Matplotlib module is used to depict "
                     "the distplot with different variations in it.".format(name='Dist Plot'))
elif op_column_name == 'Line Graph':
    st.sidebar.write("**:green[{name}]**: The Seaborn :red[Line Graph] depict the relationship between continuous "
                     "as well as categorical values in a continuous data point format.".format(name='Line Graph'))
elif op_column_name == 'Histogram Graph':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[histogram Plot] is a classic visualization tool that represents the "
                     "distribution of one or more variables by counting the number of "
                     "observations that fall within discrete bins.". format(name='Histogram Graph'))
elif op_column_name == 'Scatter Graph':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[scatter plot] displays data between two continuous data. "
                     "It shows how one data variable affects the other variable. "
                     "A scatter plot can display data in different types of plots, both 2D and 3D.". format(name='Scatter Graph'))
elif op_column_name == 'Box plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[box Graph] is a very basic plot Boxplots are used to visualize distributions. "
                     "That is very useful when you want to compare data between two groups. "
                     "Sometimes a boxplot is named a box-and-whisker plot. "
                     "Any box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.".format(name='Box Plot'))
elif op_column_name == 'Kde Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[Kde plot] is a Kernel Distribution Estimation Plot which depicts "
                     "the probability density function of the continuous or non-parametric data variables"
                     " i.e. we can plot for the univariate or multiple variables altogether". format(name='Kde Plot'))
st.sidebar.markdown("---")
st.sidebar.header("Visualization Width and Height.")
st.sidebar.write("**:green[Set Width and Height of Given Graph]**")

width = st.sidebar.slider("Plot Width", 1, 45, 9)
height = st.sidebar.slider("Plot Height", 1, 40, 4)

st.header(":green[Quantitative Statistics Analysis]")
st.markdown("---")
st.cache(persist=True)
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("Visualization for **:green[Numerical Data] of Given :red[CSV Dataset]**")
    numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
    select_columns = st.selectbox("**:green[Select a Column]**", numeric_columns)
    left_col, right_col, center_col, count_col = st.columns((2,2,2,2))
    with left_col:
        st.write("Column Name")
        st.write(df[[select_columns]])
    with right_col:
        st.write("No. of Missing Values are")
        st.write(df[[select_columns]].isna().sum())
    with center_col:
        st.write("Percentage of Missing Value are")
        st.write(df[[select_columns]].isna().sum() / len(df) * 100)
    with count_col:
        st.write("No of Non-Empty Values")
        st.write(df[[select_columns]].count())
    if select_columns:
        options = st.tabs(['Dist Plot', 'Line Plot', 'Histogram Graph', 'Scatter Graph', 'Box lot', 'kde Plot'])
        with options[0]:
            dist_slider = st.slider(label="Number of distplot Bins", min_value=5, max_value=100, value=15)
            histo_size, ax = plt.subplots(figsize=(width, height))
            sns.distplot(df[select_columns], bins=dist_slider)
            plt.grid()
            plt.title("Distance Plot")
            buffer = BytesIO()
            st.pyplot(histo_size)
            histo_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='distance chart.png',
                mime='image/png'
            )
        with options[1]:
            line_size, ax = plt.subplots(figsize=(width, height))
            sns.lineplot(df[select_columns])
            plt.title("Line Plot")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(line_size)
            line_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with options[2]:
            hist_slider = st.slider(label="Number of histogram Bins", min_value=5, max_value=100, value=15)
            hist_size, ax = plt.subplots(figsize=(width, height))
            sns.histplot(df[select_columns], bins=hist_slider, kde=True)
            plt.title("Histogram Plot")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(hist_size)
            hist_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with options[3]:
            scatter_size, ax = plt.subplots(figsize=(width, height))
            sns.scatterplot(df[select_columns])
            plt.title("Scatter Plot")
            buffer = BytesIO()
            st.pyplot(scatter_size)
            scatter_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='scatter chart.png',
                mime='image/png'
            )
        with options[4]:
            boxplot_size, ax = plt.subplots(figsize=(width, height))
            sns.boxplot(df[select_columns])
            plt.title("Box Plot")
            buf = BytesIO()
            boxplot_size.savefig(buf, format='png', bbox_inches='tight')
            buffer = BytesIO()
            st.pyplot(boxplot_size)
            boxplot_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with options[5]:
            heat_size, ax = plt.subplots(figsize=(width, height))
            sns.kdeplot(df[select_columns], common_grid=True)
            plt.grid()
            plt.title("Kernel Distribution Estimation Plot")
            buffer = BytesIO()
            st.pyplot(heat_size)
            heat_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='kernal distribution estimation chart.png',
                mime='image/png'
            )
if "df2" in st.session_state:
    df2 = st.session_state.df2
    st.subheader("Visualization for **:green[Numerical Data] of Given :red[Excel DataSet]**")
    numeric_columns = df2.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
    select_columns = st.selectbox("**:green[Select a Column]**", numeric_columns)
    left_col, right_col, center_col, count_col = st.columns((2,2,2,2))
    with left_col:
        st.write("Column Name")
        st.write(df2[[select_columns]])
    with right_col:
        st.write("No. of Missing Values are")
        st.write(df2[[select_columns]].isna().sum())
    with center_col:
        st.write("Percentage of Missing Value are")
        st.write(df2[[select_columns]].isna().sum() / len(df2) * 100)
    with count_col:
        st.write("No of Non-Empty Values")
        st.write(df2[[select_columns]].count())
    if select_columns:
        options = st.tabs(['Dist Graph', 'Line Plot', 'Histogram Graph', 'Scatter Graph', 'Box Plot', 'kde Plot'])
        with options[0]:
            dist_slider = st.slider(label="Number of distplot Bins", min_value=5, max_value=100, value=15)
            histo_size, ax = plt.subplots(figsize=(width, height))
            sns.distplot(df2[select_columns], bins=dist_slider)
            plt.grid()
            plt.title("Distance Plot")
            buffer = BytesIO()
            st.pyplot(histo_size)
            histo_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='distance chart.png',
                mime='image/png'
            )
        with options[1]:
            line_size, ax = plt.subplots(figsize=(width, height))
            sns.lineplot(df2[select_columns])
            plt.title("Distance Plot")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(line_size)
            line_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with options[2]:
            hist_slider = st.slider(label="Number of histogram Bins", min_value=5, max_value=100, value=15)
            hist_size, ax = plt.subplots(figsize=(width, height))
            sns.histplot(df2[select_columns], bins=hist_slider, kde=True)
            plt.title("Histogram Plot")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(hist_size)
            hist_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with options[3]:
            scatter_size, ax = plt.subplots(figsize=(width, height))
            sns.scatterplot(df2[select_columns])
            plt.title("Scatter Plot")
            buffer = BytesIO()
            st.pyplot(scatter_size)
            scatter_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='scatter chart.png',
                mime='image/png'
            )
        with options[4]:
            boxplot_size, ax = plt.subplots(figsize=(width, height))
            sns.boxplot(df2[select_columns])
            plt.title("Box Plot")
            buffer = BytesIO()
            st.pyplot(boxplot_size)
            boxplot_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box plot chart.png',
                mime='image/png'
            )
        with options[5]:
            heat_size, ax = plt.subplots(figsize=(width, height))
            sns.kdeplot(df2[select_columns], common_grid=True)
            plt.grid()
            plt.title("Kernel Distribution Estimation Plot")
            buffer = BytesIO()
            st.pyplot(heat_size)
            heat_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='kernal distribution estimation chart.png',
                mime='image/png'
            )
