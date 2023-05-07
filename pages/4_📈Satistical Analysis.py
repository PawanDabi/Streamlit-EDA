import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from io import BytesIO
import base64
st.set_page_config(page_title="Statistical Analysis",
    page_icon="📈",
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
st.sidebar.header("Summarizing Statistics Analysis and Graphs.")
options = ["", "Univariate Analysis", "Bivariate Analysis", "Outlier Analysis", "Z-Score Analysis", "IQR Analysis", "Count Graph",
            "Histogram Graph", "Box Graph", "Scatter Graph", "Regression Graph"]
analysis_column = st.sidebar.selectbox("Information About **:green[Univariate]**, **:green[Bivariate]**, **:green[Outlier Analysis]** and           **:green[Graphs]**", options)
if analysis_column == 'Univariate Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Univariate Analysis] refers to the analysis of a single variable. "
                     "In other words, it examines the distribution, central tendency, and variability of a "
                     "single variable in isolation. Examples of univariate analysis include calculating the mean, "
                     "median, and mode of a variable or creating a histogram to visualize "
                     "the distribution of a variable.".format(name='Univariate Analysis'))
elif analysis_column == 'Bivariate Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Bivariate Analysis] refers to the analysis of two variables at the same time. "
                     "It examines the relationship between two variables and how they are associated with each other."
                     " Examples of bivariate analysis include calculating the correlation coefficient between two variables, "
                     "creating a scatter plot to visualize the relationship between two variables, or conducting a chi-square "
                     "test to determine if there is a relationship between two categorical variables.".format(name='Bivariate Analysis'))
elif analysis_column == 'Outlier Analysis':
    st.sidebar.write("**:green[{name}]**: The :red[Outliers] are the extreme values within the dataset. "
                     "That means the outlier data points vary greatly from the expected values—either being much larger"
                     " or significantly smaller. For data that follows a normal distribution, the values that fall more "
                     "than three standard deviations from the mean are typically considered outliers.".format(name='Outlier Analysis'))
elif analysis_column == 'Z-Score Analysis':
    st.sidebar.write("**:green[{name}]** The :red[Z-Score] is the signed number of standard deviations by which the value of an observation "
                     "or data point is above the mean value of what is being observed or measured. These data points which are"
                     " way too far from zero will be treated as the outliers. In most of the cases, "
                     "a threshold of 3 or -3 is used i.e if the Z-score value is greater than or less than 3 or -3 respectively, "
                     "that data point will be identified as outliers.".format(name='Z-Score Analysis'))
elif analysis_column == 'IQR Analysis':
    st.sidebar.write("**:green[{name}]** The :red[Inter-Quartile Range] (IQR) is a measure of statistical dispersion, "
                     "being equal to the difference between 75th and 25th percentiles, "
                     "or between upper and lower quartiles.".format(name='IQR Analysis'))
elif analysis_column == "Count Graph":
    st.sidebar.write("**:green[{name}]** The :red[Count PLot] is a univariate plot that shows "
                        "the comparison of different groups in categorical variables. "
                        "It shows the number of observations per category using bins.". format(name='Count Graph'))
elif analysis_column == "Histogram Graph":
    st.sidebar.write("**:green[{name}]**: The seaborn :red[histogram Plot] is a classic visualization tool that represents the "
                     "distribution of one or more variables by counting the number of "
                     "observations that fall within discrete bins.". format(name='Histogram Graph'))
elif analysis_column == 'Box Graph':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[box Graph] is a very basic plot Boxplots are used to visualize distributions. "
                     "That is very useful when you want to compare data between two groups. "
                     "Sometimes a boxplot is named a box-and-whisker plot. "
                     "Any box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.".format(name='Box Plot'))
elif analysis_column == 'Scatter Graph':
    st.sidebar.write("**:green[{name}]** The seaborn :red[scatter plot] displays data between two continuous data. "
                     "It shows how one data variable affects the other variable. "
                     "A scatter plot can display data in different types of plots, both 2D and 3D.". format(name='Scatter Graph'))
elif analysis_column == 'Regression Graph':
    st.sidebar.write("**:green[{name}]**: The :red[Regression Graph] creates a regression line between 2 parameters and helps to visualize their linear  relationships. ".format(name='Regression Graph'))
st.sidebar.markdown("---")
st.sidebar.header("Visualization Width and Height.")
st.sidebar.write("**:green[Set Width and Height of Given Graph]**")
width = st.sidebar.slider("Plot Width", 1, 45, 9)
height = st.sidebar.slider("Plot Height", 1, 40 , 4)
if "df" in st.session_state:
    df = st.session_state.df
    st.header("**:green[Univariate]** , **:green[Bivariate]** and **:green[Outlier Analysis]** on Given :red[CSV File ]")
    analysis = st.tabs(['Univariate Analysis (UA)', 'Bivariate Analysis (BA)', 'Outlier Analysis (OA)'])
    with analysis[0]:
        inner_analysis = st.tabs(['Univariate Analysis for Categorical Data', 'Univariate Analysis for Numerical Data'])
        with inner_analysis[0]:
            categorical_columns = df.select_dtypes(include=['object']).columns
            column = st.selectbox("**:green[Select Column ]**", categorical_columns)
            right_col, left_col = st.columns((2,6))
            with right_col:
                st.write("Column Name")
                st.write(df[[column]])
            with left_col:
                st.write("Frequency Table")
                freq_table = pd.crosstab(index=df[column], columns="count")
                st.write(freq_table)
            count_size, ax = plt.subplots(figsize=(width, height))
            plt.title("Count Plot")
            sns.countplot(x=column, data=df)
            buffer = BytesIO()
            st.pyplot(count_size)
            count_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='count chart.png',
                mime='image/png'
            )
        with inner_analysis[1]:
            numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
            column = st.selectbox("**:green[Select Column ]**", numeric_columns)
            right_col, left_col = st.columns((2,5))
            with right_col:
                st.write("Column Name")
                st.write(df[[column]])
            with left_col:
                st.write("Summary Statistics")
                st.write(df[column].describe())
            inner_plot = st.tabs(['Histogram Plot', 'Box Plot'])
            with inner_plot[0]:
                histogram_size, ax = plt.subplots(figsize=(width, height))
                slid = st.slider(label="Number of Plots Bins", min_value=5, max_value=100, value=15)
                plt.hist(df[column], bins=slid)
                plt.title("Histogram Plot")
                buffer = BytesIO()
                st.pyplot(histogram_size)
                histogram_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='histogram chart.png',
                    mime='image/png'
                )
            with inner_plot[1]:
                boxplot_size, ax = plt.subplots(figsize=(width, height))
                plt.title("Box Plot")
                sns.boxplot(df[column])
                buffer = BytesIO()
                st.pyplot(boxplot_size)
                boxplot_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='box chart.png',
                    mime='image/png'
                )
    with analysis[1]:
        inner_ba_analysis = st.tabs(['Numerical Data V/S Numerical Data', 'Numerical Data V/S Categorical Data',
                                     'Categorical Data V/S Categorical Data  '])
        with inner_ba_analysis[0]:
            inner_nn_plot = st.tabs(['Scatter Plot', 'Regression Plot'])
            with inner_nn_plot[0]:
                column1 = st.selectbox("**:green[Select x Column]**", numeric_columns)
                column2 = st.selectbox("**:green[Select y Column]**", numeric_columns)
                right_col, left_col = st.columns((2,5))
                with right_col:
                    st.write("X-Axis Column Name")
                    st.write(df[[column1]])
                with left_col:
                    st.write("Y-Axis Column Name")
                    st.write(df[[column2]])
                plt.title("Scatter Plot")
                scat_size, ax = plt.subplots(figsize=(width, height))
                plt.scatter(df[column1], df[column2])
                plt.title("Scatter Plot")
                buffer = BytesIO()
                st.pyplot(scat_size)
                scat_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='scatter chart.png',
                    mime='image/png'
                )
            with inner_nn_plot[1]:
                column1 = st.selectbox("**:green[Select X Column]**", numeric_columns)
                column2 = st.selectbox("**:green[Select Y Column]**", numeric_columns)
                right_col, left_col = st.columns((2,5))
                with right_col:
                    st.write("X-Axis Column Name")
                    st.write(df[[column1]])
                with left_col:
                    st.write("Y-Axis Column Name")
                    st.write(df[[column2]])
                reg_size, ax = plt.subplots(figsize=(width, height))
                sns.regplot(x=column1, y=column2, data=df)
                plt.title("Regression Plot")
                buffer = BytesIO()
                st.pyplot(reg_size)
                reg_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='regression chart.png',
                    mime='image/png'
                )
        with inner_ba_analysis[1]:
            column1 = st.selectbox("**:green[Select x Column]**  ", numeric_columns)
            column2 = st.selectbox("**:green[Select y Column]**  ", categorical_columns)
            right_col, center_col, left_col = st.columns((2,3,8))
            with right_col:
                st.write("X-Axis Column Name")
                st.write(df[[column1]])
            with center_col:
                st.write("Y-Axis Column Name")
                st.write(df[[column2]])
            with left_col:
                st.write("Summary Statistics by Category")
                summary = df.groupby(column2)[column1].describe()
                st.write(summary)
            box_size_height, ax = plt.subplots(figsize=(width, height))
            sns.boxplot(x=column2, y=column1, data=df)
            plt.title("Box PLot")
            buffer = BytesIO()
            st.pyplot(box_size_height)
            box_size_height.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='boxs chart.png',
                mime='image/png'
            )
        with inner_ba_analysis[2]:
            column1 = st.selectbox("**:green[Select x Column]** ", categorical_columns)
            column2 = st.selectbox("**:green[Select y Column]** ", categorical_columns)
            bar_size, ax = plt.subplots(figsize=(width, height))
            contingency_table = pd.crosstab(index=df[column1], columns=df[column2])
            right_col, center_col, left_col = st.columns((2,3,8))
            with right_col:
                st.write("X Column Name")
                st.write(df[[column1]])
            with center_col:
                st.write("Y Column Name")
                st.write(df[[column2]])
            with left_col:
                st.write("Contingency Table")
                st.write(contingency_table)
            plt.title("Stacked Bar Chart")
            contingency_table.plot(kind="bar", stacked=True)
            plt.xlabel(column1)
            plt.ylabel("Count")
            st.pyplot()
    with analysis[2]:
        outlier_tab = st.tabs(['Z-Score Outlier', 'Inter-Quartile Range  (IQR)  Outlier'])
        with outlier_tab[0]:
            outer_column = st.selectbox(":green[Select a Column]", numeric_columns)
            zscore = (df[outer_column] - df[outer_column].mean()) / df[outer_column].std()
            threshold = 3
            outliers = df[zscore.abs() >= threshold][outer_column]
            right_col, left_col = st.columns((2,6))
            with right_col:
                st.write("Column Name")
                st.write(df[[outer_column]])
            with left_col:
                st.write("No. of :green[Outlier's] in column")
                st.write(outliers.to_frame())
            inner_zscore = st.tabs(['Histogram Z-Score Plot', 'Scatter Z-Score Plot'])
            with inner_zscore[0]:
                outlier_plot, ax = plt.subplots(figsize=(width, height))
                sns.histplot(df[outer_column], kde=True, ax=ax)
                ax.axvline(df[outer_column].mean(), color='r', linestyle='dashed', linewidth=2)
                ax.axvline(df[outer_column].mean() + (threshold * df[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.axvline(df[outer_column].mean() - (threshold * df[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.set_title(f"Histogram of {outer_column}")
                ax.set_xlabel(outer_column)
                ax.set_ylabel("Frequency")
                buffer = BytesIO()
                st.pyplot(outlier_plot)
                outlier_plot.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='histogram z-score chart.png',
                    mime='image/png'
                )
            with inner_zscore[1]:
                outlier_plot_1, ax2 = plt.subplots(figsize=(width, height))
                sns.scatterplot(data=df, x=range(len(df)), y=outer_column, ax=ax2)
                ax2.scatter(outliers.index, outliers, color='r')
                ax2.set_title(f"Scatter Plot of {outer_column}")
                ax2.set_xlabel("Index")
                ax2.set_ylabel(outer_column)
                buffer = BytesIO()
                st.pyplot(outlier_plot_1)
                outlier_plot_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='sorted horizontal bar chart.png',
                    mime='image/png'
                )
    with outlier_tab[1]:
        iqr_column = st.selectbox(":green[ Select a Column]", numeric_columns)
        q1 = df[iqr_column].quantile(0.25)
        q3 = df[iqr_column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        outliers = df[(df[iqr_column] < lower_bound) | (df[iqr_column] > upper_bound)][iqr_column]
        right_col, left_col, center, right = st.columns((2,3,4,6))
        with right_col:
            st.write("Column Name")
            st.write(df[[iqr_column]])
        with left_col:
            st.write("No. of :green[Outlier's] in column")
            st.write(outliers.to_frame())
        with center:
            st.write("The values of outliers is: ")
            st.write("q1: ",q1)
            st.write("q3: ",q3)
            st.write("iqr: ",iqr)
        with right:
            st.write("Outliers Per :green[Row No]: ",outliers)
        inner_zscore = st.tabs(['Box IQR Plot', 'Scatter IQR Plot'])
        with inner_zscore[0]:
            outlier_iqr, ax1 = plt.subplots(figsize=(width, height))
            sns.boxplot(x=df[iqr_column], ax=ax1)
            ax1.set_title(f"Boxplot of {iqr_column}")
            ax1.scatter(x=outliers.index, y=outliers, color='r', label="Outliers")
            buffer = BytesIO()
            st.pyplot(outlier_iqr)
            outlier_iqr.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box iqr chart.png',
                mime='image/png'
            )
        with inner_zscore[1]:
            outlier_iqr_1, ax2 = plt.subplots(figsize=(width, height))
            sns.scatterplot(data=df, x=range(len(df)), y=iqr_column, marker="*", ax=ax2)
            ax2.scatter(outliers.index, outliers, color='r')
            ax2.set_title(f"Scatter Plot of {iqr_column}")
            ax2.set_xlabel("Index")
            ax2.set_ylabel(iqr_column)
            buffer = BytesIO()
            st.pyplot(outlier_iqr_1)
            outlier_iqr_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='scatter iqr chart.png',
                mime='image/png'
            )
if "df2" in st.session_state:
    df2 = st.session_state.df2
    st.header("**:green[Univariate]** , **:green[Bivariate]** and **:green[Outlier Analysis]** on Given :red[Excel File]")
    analysis = st.tabs(['Univariate Analysis (UA)', 'Bivariate Analysis (BA)', 'Outlier Analysis (OA)'])
    with analysis[0]:
        inner_analysis = st.tabs(['Univariate Analysis for Categorical Data', 'Univariate Analysis for Numerical Data'])
        with inner_analysis[0]:
            categorical_columns = df2.select_dtypes(['object']).columns
            column = st.selectbox("**:green[Select Column ]**", categorical_columns)
            right_col, left_col = st.columns((2,6))
            with right_col:
                st.write("Column Name")
                st.write(df2[[column]])
            with left_col:
                st.write("Frequency Table")
                freq_table = pd.crosstab(index=df2[column], columns="count")
                st.write(freq_table)
            count_size, ax = plt.subplots(figsize=(width, height))
            plt.title("Count Plot")
            # cate_size = plt.subplots(figsize=(width, height))
            sns.countplot(x=column, data=df2)
            buffer = BytesIO()
            st.pyplot(count_size)
            count_size.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='count chart.png',
                mime='image/png'
            )
        with inner_analysis[1]:
            numeric_columns = df2.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
            column = st.selectbox("**:green[Select Column ]**", numeric_columns)
            right_col, left_col = st.columns((2,5))
            with right_col:
                st.write("Column Name")
                st.write(df2[[column]])
            with left_col:
                st.write("Summary Statistics")
                st.write(df2[column].describe())
            inner_plot = st.tabs(['Histogram Plot', 'Box Plot'])
            with inner_plot[0]:
                plt.title("Histogram Plot")
                histogram_size, ax = plt.subplots(figsize=(width, height))
                slid = st.slider(label="Number of Plots Bins", min_value=5, max_value=100, value=15)
                plt.hist(df2[column], bins=slid)
                plt.title("Histogram Plot")
                buffer = BytesIO()
                st.pyplot(histogram_size)
                histogram_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='histogram chart.png',
                    mime='image/png'
                )
            with inner_plot[1]:
                plt.title("Box Plot")
                boxplot_size, ax = plt.subplots(figsize=(width, height))
                sns.boxplot(df2[column])
                buffer = BytesIO()
                st.pyplot(boxplot_size)
                boxplot_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='box chart.png',
                    mime='image/png'
                )
    with analysis[1]:
        inner_ba_analysis = st.tabs(['Numerical Data V/S Numerical Data', 'Numerical Data V/S Categorical Data',
                                     'Categorical Data V/S Categorical Data  '])
        with inner_ba_analysis[0]:
            inner_nn_plot = st.tabs(['Scatter Plot', 'Regression Plot'])
            with inner_nn_plot[0]:
                column1 = st.selectbox("**:green[Select x Column]**", numeric_columns)
                column2 = st.selectbox("**:green[Select y Column]**", numeric_columns)
                right_col, left_col = st.columns((2,5))
                with right_col:
                    st.write("X-Axis Column Name")
                    st.write(df2[[column1]])
                with left_col:
                    st.write("Y-Axis Column Name")
                    st.write(df2[[column2]])
                plt.title("Scatter Plot")
                scat_size, ax = plt.subplots(figsize=(width, height))
                plt.scatter(df2[column1], df2[column2])
                plt.title("Scatter Plot")
                buffer = BytesIO()
                st.pyplot(scat_size)
                scat_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='scatter chart.png',
                    mime='image/png'
                )
            with inner_nn_plot[1]:
                column1 = st.selectbox("**:green[Select X Column]**", numeric_columns)
                column2 = st.selectbox("**:green[Select Y Column]**", numeric_columns)
                right_col, left_col = st.columns((2,5))
                with right_col:
                    st.write("X-Axis Column Name")
                    st.write(df2[[column1]])
                with left_col:
                    st.write("Y-Axis Column Name")
                    st.write(df2[[column2]])
                reg_size, ax = plt.subplots(figsize=(width, height))
                sns.regplot(x=column1, y=column2, data=df2)
                plt.title("Regression Plot")
                buffer = BytesIO()
                st.pyplot(reg_size)
                reg_size.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='regression chart.png',
                    mime='image/png'
                )
        with inner_ba_analysis[1]:
            column1 = st.selectbox("**:green[Select x Column]**  ", numeric_columns)
            column2 = st.selectbox("**:green[Select y Column]**  ", categorical_columns)
            right_col, center_col, left_col = st.columns((2,3,8))
            with right_col:
                st.write("X-Axis Column Name")
                st.write(df2[[column1]])
            with center_col:
                st.write("Y-Axis Column Name")
                st.write(df2[[column2]])
            with left_col:
                st.write("Summary Statistics by Category")
                summary = df2.groupby(column2)[column1].describe()
                st.write(summary)
            box_size_height, ax = plt.subplots(figsize=(width, height))
            sns.boxplot(x=column2, y=column1, data=df2)
            plt.title("Box PLot")
            buffer = BytesIO()
            st.pyplot(box_size_height)
            box_size_height.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box chart.png',
                mime='image/png'
            )
        with inner_ba_analysis[2]:
            column1 = st.selectbox("**:green[Select x Column]** ", categorical_columns)
            column2 = st.selectbox("**:green[Select y Column]** ", categorical_columns)
            bar_size, ax = plt.subplots(figsize=(width, height))
            contingency_table = pd.crosstab(index=df2[column1], columns=df2[column2])
            right_col, center_col, left_col = st.columns((2,3,8))
            with right_col:
                st.write("X Column Name")
                st.write(df2[[column1]])
            with center_col:
                st.write("Y Column Name")
                st.write(df2[[column2]])
            with left_col:
                st.write("Contingency Table")
                st.write(contingency_table)
            plt.title("Stacked Bar Chart")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            contingency_table.plot(kind="bar", stacked=True)
            plt.xlabel(column1)
            plt.ylabel("Count")
            st.pyplot()
    with analysis[2]:
        outlier_tab = st.tabs(['Z-Score Outlier', 'Inter-Quartile Range  (IQR)  Outlier'])
        with outlier_tab[0]:
            outer_column = st.selectbox(":green[Select a Column]", numeric_columns)
            zscore = (df2[outer_column] - df2[outer_column].mean()) / df2[outer_column].std()
            threshold = 3
            outliers = df2[zscore.abs() >= threshold][outer_column]
            right_col, left_col = st.columns((2,6))
            with right_col:
                st.write("Column Name")
                st.write(df2[[outer_column]])
            with left_col:
                st.write("No. of :green[Outlier's] in column")
                st.write(outliers.to_frame())
            inner_zscore = st.tabs(['Histogram Z-Score Plot', 'Scatter Z-Score Plot'])
            with inner_zscore[0]:
                outlier_plot, ax = plt.subplots(figsize=(width, height))
                sns.histplot(df2[outer_column], kde=True, ax=ax)
                ax.axvline(df2[outer_column].mean(), color='r', linestyle='dashed', linewidth=2)
                ax.axvline(df2[outer_column].mean() + (threshold * df2[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.axvline(df2[outer_column].mean() - (threshold * df2[outer_column].std()), color='g', linestyle='dashed', linewidth=2)
                ax.set_title(f"Histogram of {outer_column}")
                ax.set_xlabel(outer_column)
                ax.set_ylabel("Frequency")
                buffer = BytesIO()
                st.pyplot(outlie_plot)
                outlier-plot.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='histogram z-score chart.png',
                    mime='image/png'
                )
            with inner_zscore[1]:
                outlier_plot_1, ax2 = plt.subplots(figsize=(width, height))
                sns.scatterplot(data=df2, x=range(len(df2)), y=outer_column, ax=ax2)
                ax2.scatter(outliers.index, outliers, color='r')
                ax2.set_title(f"Scatter Plot of {outer_column}")
                ax2.set_xlabel("Index")
                ax2.set_ylabel(outer_column)
                buffer = BytesIO()
                st.pyplot(outlier_plot_1)
                outllier_plot_1.savefig(buffer, format='png')
                st.download_button(
                    label='Download as PNG',
                    data=buffer.getvalue(),
                    file_name='scatter chart.png',
                    mime='image/png'
                )
    with outlier_tab[1]:
        iqr_column = st.selectbox(":green[ Select a Column]", numeric_columns)
        q1 = df2[iqr_column].quantile(0.25)
        q3 = df2[iqr_column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        outliers = df2[(df2[iqr_column] < lower_bound) | (df2[iqr_column] > upper_bound)][iqr_column]
        right_col, left_col, center, right = st.columns((2,3,4,6))
        with right_col:
            st.write("Column Name")
            st.write(df2[[iqr_column]])
        with left_col:
            st.write("No. of :green[Outlier's] in column")
            st.write(outliers.to_frame())
        with center:
            st.write("The values of outliers is: ")
            st.write("q1: ",q1)
            st.write("q3: ",q3)
            st.write("iqr: ",iqr)
        with right:
            st.write("Outliers Per :green[Row No]: ",outliers)
        inner_zscore = st.tabs(['Box IQR Plot', 'Scatter IQR Plot'])
        with inner_zscore[0]:
            outlier_iqr, ax1 = plt.subplots(figsize=(width, height))
            sns.boxplot(x=df2[iqr_column], ax=ax1)
            ax1.set_title(f"Boxplot of {iqr_column}")
            ax1.scatter(x=outliers.index, y=outliers, color='r', label="Outliers")
            buffer = BytesIO()
            st.pyplot(outlier_iqr)
            outlier_iqr.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='box iqr chart.png',
                mime='image/png'
            )
        with inner_zscore[1]:
            outlier_iqr_1, ax2 = plt.subplots(figsize=(width, height))
            sns.scatterplot(data=df2, x=range(len(df2)), y=iqr_column, marker="*", ax=ax2)
            ax2.scatter(outliers.index, outliers, color='r')
            ax2.set_title(f"Scatter Plot of {iqr_column}")
            ax2.set_xlabel("Index")
            ax2.set_ylabel(iqr_column)
            buffer = BytesIO()
            st.pyplot(outlier_iqr_1)
            outlier_iqr_1.savefig(buffer, format='png')
            st.download_button(
                label='Download as PNG',
                data=buffer.getvalue(),
                file_name='scatter iqr chart.png',
                mime='image/png'
            )
