import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
py.init_notebook_mode(connected=True)
sns.set(style="white", color_codes=True)

import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px  

def get_column_names(data):
    """ This function will be used to extract the column names for numerical and categorical variables
    info from the dataset
    input: dataframe containing all variables
    output: num_vars-> list of numerical columns
            cat_vars -> list of categorical columns"""
        
    num_var = data.select_dtypes(include=['int', 'float']).columns
    print()
    print('Numerical variables are:\n', num_var)
    print('-------------------------------------------------')

    categ_var = data.select_dtypes(include=['category', 'object']).columns
    print('Categorical variables are:\n', categ_var)
    print('-------------------------------------------------') 
    return num_var,categ_var
    
    
def percentage_null_values(data):
    """
    Function that calculates the percentage of missing values in every column of your dataset
    input: data --> dataframe
    """
    null_perc = round(data.isnull().sum() / data.shape[0],3) * 100.00
    null_perc = pd.DataFrame(null_perc, columns=['Percentage_NaN'])
    null_perc= null_perc.sort_values(by = ['Percentage_NaN'], ascending = False)
    return null_perc



## Added by Adeline
def plot_continent_scores(df, continent):
    """Plots happiness scores for countries within a given continent."""
    df_continent = df[df["Continent"] == continent]  # Filter data for the continent

    # Sort countries by score for better visualization
    df_continent = df_continent.groupby("Country or region")["score"].mean().reset_index()
    df_continent = df_continent.sort_values(by="score", ascending=False)

    # Create the plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x="score", y="Country or region", data=df_continent, palette="Greens")

    # Titles and labels
    plt.xlabel("Average Happiness Score")
    plt.ylabel("Country")
    plt.title(f"Happiness Scores in {continent}")

    # Show the plot
    plt.show()

