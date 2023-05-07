import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
st.set_page_config(page_title="Statistics Graph",
    page_icon="📊",
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
st.sidebar.header("Information About Statistics Graphs.")
graph_option = ["", "Bar Graph", "Barh(Horizontal Bar) Graph", "Histogram Graph",
                "Line Graph", "Box Plot", "Pie Chart", "Heat Map", "Dist Graph","Scatter Plot", "Kde Graph"]
op_column_name = st.sidebar.selectbox("**:green[Brief Description About Graph's]**", graph_option)
if op_column_name == 'Bar Graph':
    st.sidebar.write("**:green[{name}]**: A :red[bar chart] or bar graph is a chart or graph that presents categorical data with rectangular "
                     "bars with heights or lengths proportional to the values that they represent. "
                     "The bars plotted in :red[vertically].".format(name='Bar Graph'))
elif op_column_name == 'Barh(Horizontal Bar) Graph':
    st.sidebar.write("**:green[{name}]**: The :red[barh Graph] is a chart of graph that presents categorical data with rectangular "
                     "bars with heights or lengths proportional to the values that they represent. "
                     "The bars plotted in :red[horizontally]".format(name='Barh(Horizontal Bar) Graph'))
elif op_column_name == 'Histogram Graph':
    st.sidebar.write("**:green[{name}]**: A :red[histogram Graph] is a graph showing frequency distributions. "
                     "It is a graph showing the number of observations within each given interval.".format(name='Histogram Graph'))
elif op_column_name == 'Line Graph':
    st.sidebar.write("**:green[{name}]**: The :red[Line Graph] work out of the box with matplotlib. "
                     "You can have multiple lines in a line chart, change color, "
                     "change type of line and much more. Matplotlib is a Python module for plotting. "
                     "Line charts are one of the many chart types it can create.".format(name='Line Graph'))
elif op_column_name == 'Box Graph':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[box plot] is a very basic plot Boxplots are used to visualize distributions. "
                     "That is very useful when you want to compare data between two groups. "
                     "Sometimes a boxplot is named a box-and-whisker plot. "
                     "Any box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.".format(name='Box Graph'))
elif op_column_name == 'Pie Chart':
    st.sidebar.write("**:green[{name}]**: The :red[Pie Graph] show the size of items (called wedge) in one data series, "
                     "proportional to the sum of the items. The data points in a pie chart are shown as a "
                     "percentage of the whole pie. Matplotlib API has a :red[pie()] function that generates "
                     "a pie diagram representing data in an array.".format(name='Pie Chart'))
elif op_column_name == 'Heat Map':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[Heat Map] is often desirable to show data which depends on two independent "
                     "variables as a color coded image plot. This is often referred to as a heatmap. "
                     "If the data is categorical, this would be called a categorical heatmap. "
                     "Matplotlib's imshow function makes production of such plots particularly easy.".format(name='Heat Map'))
elif op_column_name == 'Dist Graph':
    st.sidebar.write("**:green[{name}]**:  The seaborn :red[Distplot] or distribution plot, depicts the variation in the data distribution. "
                     "Seaborn Distplot represents the overall distribution of continuous data variables. "
                     "The Seaborn module along with the Matplotlib module is used to depict "
                     "the distplot with different variations in it.".format(name='Dist Graph'))
elif op_column_name == 'Scatter Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[scatter plot] displays data between two continuous data. "
                     "It shows how one data variable affects the other variable. "
                     "A scatter plot can display data in different types of plots, both 2D and 3D.". format(name='Scatter Plot'))
elif op_column_name == 'Kde Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[Kde plot] is a Kernel Distribution Estimation Plot which depicts "
                     "the probability density function of the continuous or non-parametric data variables"
                     " i.e. we can plot for the univariate or multiple variables altogether". format(name='Kde Plot'))
st.sidebar.markdown("---")
st.sidebar.header("Visualization Width and Height.")
st.sidebar.write("**:green[Set Width and Height of Given Graph]**")
width = st.sidebar.slider("Plot Width", 1, 45, 10)
height = st.sidebar.slider("Plot Height", 1, 40, 4)
st.header(":green[Qualitative Statistics or Quantitative Statistics Analysis]")
st.markdown("---")
st.cache(persist=True)
if "df" in st.session_state:
    df = st.session_state.df
    st.subheader("Visualization for **:green[Categorical]** and **:green[Numerical Data]** of Given **:red[CSV File]** ")
    missing_value_dataset = df.isna().sum()
    missing_value_ascen_dataset = df.isna().sum().sort_values()
    df_missing_percentage = df.isna().sum() / len(df) * 100
    df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
    df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
    missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
    empty_value = df.count()
    df_missing_non_empty_ascending = df.count().sort_values()
    df_missing_non_empty_descending = df.count().sort_values(ascending=False)
    visual_tabs = st.tabs(['Visualization for Missing Value', 'Visualization for Percentage of Missing Value', 'Visualization for Non-Empty Value'])
    with visual_tabs[0]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Graph', 'Box Plot', 'Pie Chart', 'Heat Map'])
        with inner_tabs[0]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='bar')
            buffer = BytesIO()
            st.pyplot(fig)
            fig.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                figure, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(figure)
                figure.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_1)
                fig_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[1]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig_2, ax = plt.subplots(figsize=(width, height))
            plt.title("Horizontal Bar Graph")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='barh')
            buffer = BytesIO()
            st.pyplot(fig_2)
            fig_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                fig_3, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph ")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_3)
                fig_3.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_4, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_4)
                figure.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[2]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_3, ax = plt.subplots(figsize=(width, height))
            plt.title("Histogram Graph")
            dist = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=8)
            graph = missing_val.plot(kind='hist', bins=dist)
            buffer = BytesIO()
            st.pyplot(missing_val_3)
            missing_val_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_4, ax = plt.subplots(figsize=(width, height))
            plt.title("Line Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='line')
            plt.grid()
            buffer = BytesIO()
            st.pyplot(missing_val_4)
            missing_val_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_5, ax = plt.subplots(figsize=(width, height))
            plt.title("Box Plot")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='box')
            buffer = BytesIO()
            st.pyplot(missing_val_5)
            missing_val_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_6, ax = plt.subplots(figsize=(width, height))
            plt.title("Pie Chart")
            graph = missing_val.plot(kind='pie', autopct='%1.1f%%')
            buffer = BytesIO()
            st.pyplot(missing_val_6)
            missing_val_6.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='pie chart.png',
                mime='image/png'
            )
        with inner_tabs[6]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_7, ax = plt.subplots(figsize=(width, height))
            plt.title("Heat Map")
            missing_value_dataset = sns.heatmap(df.corr(), linewidth=0.5, cmap='coolwarm')
            buffer = BytesIO()
            st.pyplot(missing_val_7)
            missing_val_7.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='heat map.png',
                mime='image/png'
            )
    with visual_tabs[1]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Graph', 'Box Plot', 'Pie Chart'])
        with inner_tabs[0]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='bar')
            buffer = BytesIO()
            st.pyplot(missing_plot)
            missing_plot.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_ascend)
                set_ascend.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_descend)
                set_descend.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[1]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_1, ax = plt.subplots(figsize=(width, height))
            plt.title("horizontal Bar Graph")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='barh')
            buffer = BytesIO()
            st.pyplot(missing_plot_1)
            missing_plot_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_ascend_1)
                set_ascend_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_descend_1)
                set_descend_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[2]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_2, ax = plt.subplots(figsize=(width, height))
            his = st.slider(label="Number of  Bins", min_value=5, max_value=100, value=8)
            graph = df_missing_percentage.plot(kind='hist', bins=his)
            plt.title("Histogram Graph")
            buffer = BytesIO()
            st.pyplot(missing_plot_2)
            missing_plot_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_3, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='line')
            plt.title("Line Graph")
            plt.xlabel("Column Name")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(missing_plot_3)
            missing_plot_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            plt.title("Box Plot")
            missing_plot_4, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='box')
            buffer = BytesIO()
            st.pyplot(missing_plot_4)
            missing_plot_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            plt.title("Pie Chart")
            missing_plot_5, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='pie', autopct='%1.1f%%')
            buffer = BytesIO()
            st.pyplot(missing_plot_5)
            missing_plot_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='pie chart.png',
                mime='image/png'
            )
    with visual_tabs[2]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Grah', 'Histogram Graph', 'Line Graph', 'Box lot', 'Pie Chart'])
        with inner_tabs[0]:
            empty_missing, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            graph = empty_value.plot(kind='bar')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing)
            empty_missing.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_count, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                graph = df_missing_non_empty_ascending.plot(kind='bar')
                buffer = BytesIO()
                st.pyplot(empty_missing_count)
                empty_missing_count.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with inner_tab_count[1]:
                empty_missing_count_2, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                graph = df_missing_non_empty_descending.plot(kind='bar')
                buffer = BytesIO()
                st.pyplot(empty_missing_count_2)
                empty_missing_count_2.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[1]:
            empty_missing_1, ax = plt.subplots(figsize=(width, height))
            plt.title("Horizontal Bar Graph")
            graph = empty_value.plot(kind='barh')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_1)
            empty_missing_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_barh, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                graph = df_missing_non_empty_ascending.plot(kind='barh')
                buffer = BytesIO()
                st.pyplot(empty_missing_barh)
                empty_missing_barh.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with inner_tab_count[1]:
                empty_missing_barh_2, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                graph = df_missing_non_empty_descending.plot(kind='barh')
                buffer = BytesIO()
                st.pyplot(empty_missing_barh_2)
                empty_missing_barh_2.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[2]:
            empty_missing_2, ax = plt.subplots(figsize=(width, height))
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            plt.title("Histogram Graph")
            slider = st.slider(label="Number of plot  Bins", min_value=5, max_value=100, value=15)
            graph = empty_value.plot(kind='hist', bins=slider)
            buffer = BytesIO()
            st.pyplot(empty_missing_2)
            empty_missing_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            empty_missing_3, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='line')
            plt.title("Line Graph")
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            plt.grid()
            buffer = BytesIO()
            st.pyplot(empty_missing_3)
            empty_missing_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            empty_missing_4, ax = plt.subplots(figsize=(width, height))
            plt.title("Box Plot")
            graph = empty_value.plot(kind='box')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_4)
            empty_missing_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            empty_missing_5, ax = plt.subplots(figsize=(width, height))
            plt.title("Pie Chart")
            graph = empty_value.plot(kind='pie', autopct='%1.1f%%')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_5)
            empty_missing_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='pie chart.png',
                mime='image/png'
            )
st.cache(persist=True)
if "df2" in st.session_state:
    df2 = st.session_state.df2
    st.subheader("Visualization for **:green[Categorical]** and **:green[Numerical Data]** of Given **:red[Excel DataSet]** ")
    missing_value_dataset = df2.isna().sum()
    missing_value_ascen_dataset = df2.isna().sum().sort_values()
    df_missing_percentage = df2.isna().sum() / len(df2) * 100
    df_missing_percentage_Ascending = df2.isna().sum().sort_values() / len(df2) * 100
    df_missing_percentage_Descending = df2.isna().sum().sort_values(ascending=False) / len(df2) * 100
    missing_value_descen_dataset = df2.isna().sum().sort_values(ascending=False)
    empty_value = df2.count()
    df_missing_non_empty_ascending = df2.count().sort_values()
    df_missing_non_empty_descending = df2.count().sort_values(ascending=False)
    visual_tabs = st.tabs(['Visualization for Missing Value', 'Visualization for Percentage of Missing Value', 'Visualization for Non-Empty Value'])
    with visual_tabs[0]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Graph', 'Box Plot', 'Pie Chart', 'Heat Map'])
        with inner_tabs[0]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='bar')
            buffer = BytesIO()
            st.pyplot(fig)
            fig.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                figure, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(figure)
                figure.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_1)
                fig_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png',
                    key='id1'
                )
        with inner_tabs[1]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig_2, ax = plt.subplots(figsize=(width, height))
            plt.title("Horizontal Bar Graph")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='barh')
            buffer = BytesIO()
            st.pyplot(fig_2)
            fig_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                fig_3, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_3)
                fig_3.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_4, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(fig_4)
                fig_4.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png',
                    key='id2'
                )
        with inner_tabs[2]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_3, ax = plt.subplots(figsize=(width, height))
            plt.title("Histogram Graph")
            dist = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=8)
            graph = missing_val.plot(kind='hist', bins=dist)
            buffer = BytesIO()
            st.pyplot(missing_val_3)
            missing_val_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_4, ax = plt.subplots(figsize=(width, height))
            plt.title("Line Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='line')
            plt.grid()
            buffer = BytesIO()
            st.pyplot(missing_val_4)
            missing_val_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_5, ax = plt.subplots(figsize=(width, height))
            plt.title("Box Plot")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='box')
            buffer = BytesIO()
            st.pyplot(missing_val_5)
            missing_val_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_6, ax = plt.subplots(figsize=(width, height))
            plt.title("Pie Chart")
            graph = missing_val.plot(kind='pie', autopct='%1.1f%%')
            buffer = BytesIO()
            st.pyplot(missing_val_6)
            missing_val_6.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='pie chart.png',
                mime='image/png'
            )
        with inner_tabs[6]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_7, ax = plt.subplots(figsize=(width, height))
            plt.title("Heat Map")
            missing_value_dataset = sns.heatmap(df2.corr(), linewidth=0.5, cmap='coolwarm')
            buffer = BytesIO()
            st.pyplot(missing_val_7)
            missing_val_7.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='heat map.png',
                mime='image/png'
            )
    with visual_tabs[1]:
        inner_tabs = st.tabs(['Bar Graph', 'Horixontal Bar Graph', 'Histogram Graph', 'Line Plot', 'Box Plot', 'Pie chart'])
        with inner_tabs[0]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='bar')
            buffer = BytesIO()
            st.pyplot(missing_plot)
            missing_plot.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_ascend)
                set_ascend.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend, ax = plt.subplots(figsize=(width, height))
                plt.title("sorted Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_descend)
                set_descend.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[1]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_1, ax = plt.subplots(figsize=(width, height))
            plt.title("Horizontal Bar Graph")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='barh')
            buffer = BytesIO()
            st.pyplot(missing_plot_1)
            missing_plot_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_ascend_1)
                set_ascend_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buffer = BytesIO()
                st.pyplot(set_descend_1)
                set_descend_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png',
                    key='id3    '
                )
        with inner_tabs[2]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_2, ax = plt.subplots(figsize=(width, height))
            plt.title("Histogram Graph")
            his = st.slider(label="Number of  Bins", min_value=5, max_value=100, value=8)
            graph = df_missing_percentage.plot(kind='hist', bins=his)
            plt.title("Missing Value Percentage of Histogram")
            buffer = BytesIO()
            st.pyplot(missing_plot_2)
            missing_plot_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_3, ax = plt.subplots(figsize=(width, height))
            plt.title("Line Graph")
            graph = df_missing_percentage.plot(kind='line')
            plt.title("Missing Value Percentage of Line")
            plt.xlabel("Column Name")
            plt.grid()
            buffer = BytesIO()
            st.pyplot(missing_plot_3)
            missing_plot_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_4, ax = plt.subplots(figsize=(width, height))
            plt.title("Box Graph")
            graph = df_missing_percentage.plot(kind='box')
            buffer = BytesIO()
            st.pyplot(missing_plot_4)
            missing_plot_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_5, ax = plt.subplots(figsize=(width, height))
            plt.title("Pie Chart")
            graph = df_missing_percentage.plot(kind='pie', autopct='%1.1f%%')
            buffer = BytesIO()
            st.pyplot(missing_plot_5)
            missing_plot_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='pie chart.png',
                mime='image/png'
            )
    with visual_tabs[2]:
        inner_tabs = st.tabs(['Bar Graph', 'Horizontal Bar Graph', 'Histogram Graph', 'Line Plot', 'Box Plot', 'Pie Chart'])
        with inner_tabs[0]:
            empty_missing, ax = plt.subplots(figsize=(width, height))
            plt.title("Bar Graph")
            graph = empty_value.plot(kind='bar')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buf = BytesIO()
            empty_missing.savefig(buf, format='png', bbox_inches='tight')
            buffer = BytesIO()
            st.pyplot(empty_missing)
            empty_missing.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='bar chart.png',
                mime='image/png'
            )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_count, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                graph = df_missing_non_empty_ascending.plot(kind='bar')
                buffer = BytesIO()
                st.pyplot(empty_missing_count)
                empty_missing_count.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
            with inner_tab_count[1]:
                empty_missing_count_2, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Bar Graph")
                graph = df_missing_non_empty_descending.plot(kind='bar')
                buffer = BytesIO()
                st.pyplot(empty_missing_count_2)
                empty_missing_count_2.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[1]:
            empty_missing_1, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='barh')
            plt.title("Horizontal Bar Graph")
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_1)
            empty_missing_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='horizontal bar chart.png',
                mime='image/png'
            )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_barh, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                graph = df_missing_non_empty_ascending.plot(kind='barh')
                buffer = BytesIO()
                st.pyplot(empty_missing_barh)
                empty_missing_barh.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
            with inner_tab_count[1]:
                empty_missing_barh_2, ax = plt.subplots(figsize=(width, height))
                plt.title("Sorted Horizontal Bar Graph")
                graph = df_missing_non_empty_descending.plot(kind='barh')
                buffer = BytesIO()
                st.pyplot(empty_missing_barh_2)
                empty_missing_barh_2.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
        with inner_tabs[2]:
            empty_missing_2, ax = plt.subplots(figsize=(width, height))
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            slider = st.slider(label="Number of plot  Bins", min_value=5, max_value=100, value=15)
            plt.title("Histogram Chart")
            graph = empty_value.plot(kind='hist', bins=slider)
            buffer = BytesIO()
            st.pyplot(empty_missing_2)
            empty_missing_2.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='histogram chart.png',
                mime='image/png'
            )
        with inner_tabs[3]:
            empty_missing_3, ax = plt.subplots(figsize=(width, height))
            plt.title("Line Graph")
            graph = empty_value.plot(kind='line')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            plt.grid()
            buffer = BytesIO()
            st.pyplot(empty_missing_3)
            empty_missing_3.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='line chart.png',
                mime='image/png'
            )
        with inner_tabs[4]:
            empty_missing_4, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='box')
            plt.title("Box Plot")
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_4)
            empty_missing_4.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_tabs[5]:
            empty_missing_5, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='pie', autopct='%1.1f%%')
            plt.title("Pie Chart")
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buffer = BytesIO()
            st.pyplot(empty_missing_5)
            empty_missing_5.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='Pie chart.png',
                mime='image/png'
            )
