import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuration de la page avec un arrière-plan noir
st.set_page_config(page_title="Financial and Performance Metrics Dashboard", layout="wide")

# Appliquer le thème sombre avec des améliorations pour la barre latérale et le tableau
st.markdown(
    """
    <style>
    /* Changer la couleur de fond de toute l'application */
    .stApp {
        background-color: #000000;
    }
    
    /* Changer la couleur de la barre latérale */
    section[data-testid="stSidebar"] {
        background-color: #000000;
        color: #FFFFFF;
    }

    /* Couleur du texte et des titres */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #FFFFFF;
    }

    /* Améliorer le style du tableau */
    .dataframe {
        background-color: #000000;
        color: #FFFFFF;
        border: 1px solid #FFFFFF;
        border-radius: 5px;
    }

    table {
        margin: 25px auto;
        border-collapse: collapse;
        border-radius: 12px;
        background-color: #000000;
        overflow: hidden;
        max-width: 80%;
    }

    th, td {
        padding: 10px 15px;
        text-align: left;
        color: #FFFFFF;
    }

    th {
        background-color: #333333;
    }

    td {
        background-color: #000000;
    }

    tr:nth-child(even) td {
        background-color: #1a1a1a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Charger les données
df = pd.read_csv('clean_data2.csv')

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select an option", ["Overview", "Correlation Analysis", "League-Wise Analysis", "Financial Performance"])

# Section Overview
if option == "Overview":
    st.title("Financial and Performance Metrics Dashboard")

    # 1. Dataset Data Types
    st.subheader("1. Dataset Data Types")

    # Calculer la distribution des types de données
    dtype_counts = df.dtypes.value_counts()

    # Trier les types de données par fréquence
    dtype_counts = dtype_counts.sort_values(ascending=False)

    # Définir les couleurs pour les 1er et 2e types de données les plus fréquents dans le graphique à barres
    bar_colors = ['#FFC300' if i == 1 else '#FF5733' if i == 0 else '#28B463' for i in range(len(dtype_counts))]

    # Définir les valeurs d'explosion pour les 1er et 2e types de données les plus fréquents dans le camembert
    explode_values = [0.1 if i == 1 else 0.2 if i == 0 else 0 for i in range(len(dtype_counts))]

    # Créer une grille 1x2 pour les graphiques
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    plt.style.use('dark_background')

    # Bar Chart sur la première grille (1, 1)
    bars = axes[0].bar(dtype_counts.index.astype(str), dtype_counts, color=bar_colors)
    axes[0].set_xlabel('Data Types', fontsize=12, color='white')
    axes[0].set_ylabel('Count', fontsize=12, color='white')
    axes[0].set_title('Distribution of Data Types (Bar Chart)', fontsize=14, fontweight='bold', color='white')
    axes[0].set_facecolor('black')  # Set the background of the bar chart to black

    # Annotate each bar with its height (count) in bold
    for bar in bars:
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{int(height)}', 
                     ha='center', fontsize=12, fontweight='bold', color='white')

    # Set labels below each bar
    axes[0].set_xticks(range(len(dtype_counts)))
    axes[0].set_xticklabels(dtype_counts.index.astype(str), fontsize=12, color='white')

    # Pie Chart sur la deuxième grille (1, 2)
    wedges, texts, autotexts = axes[1].pie(dtype_counts, labels=dtype_counts.index.astype(str), autopct='%1.1f%%', startangle=140, 
                                           colors=['#FF5733', '#FFC300', '#28B463', '#3498DB', '#9B59B6', '#E74C3C'], 
                                           explode=explode_values, shadow=True)
    axes[1].set_title('Distribution of Data Types (Pie Chart)', color='white', fontsize=14, fontweight='bold')

    # Make percentage labels bold in the pie chart
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    # Ajuster la mise en page
    plt.tight_layout()
    
    # Afficher les graphiques
    st.pyplot(fig)

    # 2. Summary Statistics (Categorical)
    st.subheader("2. Summary Statistics (Categorical)")

    # 2.1 League Column
    st.subheader("2.1 League Column")

    # Plot for 'league' column
    plt.figure(figsize=(6, 4))
    plt.style.use('dark_background')

    # Define color shades for high, medium, and small categories
    high_color = '#FF5733'    # Bright red-orange for high values
    medium_color = '#FFC300'  # Golden yellow for medium values
    small_color = '#28B463'   # Fresh green for small values

    # Function to determine color based on value
    def get_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color

    # Get the counts for each category
    counts = df['league'].value_counts()

    # Calculate the thresholds for small, medium, and high categories
    thresholds = [counts.quantile(0.33), counts.quantile(0.66)]

    # Create the count plot
    bar_plot = sns.countplot(y=df['league'], order=counts.index)

    # Manually color the bars based on their count
    for p in bar_plot.patches:
        count = int(p.get_width())
        color = get_color(count, thresholds)
        p.set_color(color)

        # Add numbers on each bar
        bar_plot.annotate(f'{count}', xy=(count, p.get_y() + p.get_height() / 2),
                          xytext=(-10, 0), textcoords='offset points',
                          ha='center', va='center', fontsize=12, color='white', fontweight='bold')

    # Set title and labels with white color
    plt.title('Frequency of League', fontsize=14, fontweight='bold', color='white')
    plt.xlabel('Count', fontsize=12, color='white')
    plt.ylabel('League', fontsize=12, color='white')

    # Adjust layout and display the plot
    plt.tight_layout()
    st.pyplot(plt)

    # 2.2 Competition Column
    st.subheader("2.2 Competition Column")

    # Plot for 'competition' column
    plt.figure(figsize=(6, 4))
    plt.style.use('dark_background')

    # Get the counts for each category
    counts = df['competition'].value_counts()

    # Calculate the thresholds for small, medium, and high categories
    thresholds = [counts.quantile(0.33), counts.quantile(0.66)]

    # Create the count plot
    bar_plot = sns.countplot(y=df['competition'], order=counts.index)

    # Manually color the bars based on their count
    for p in bar_plot.patches:
        count = int(p.get_width())
        color = get_color(count, thresholds)
        p.set_color(color)

        # Add numbers on each bar
        bar_plot.annotate(f'{count}', xy=(count, p.get_y() + p.get_height() / 2),
                          xytext=(-10, 0), textcoords='offset points',
                          ha='center', va='center', fontsize=12, color='white', fontweight='bold')

    # Set title and labels with white color
    plt.title('Frequency of Competition', fontsize=14, fontweight='bold', color='white')
    plt.xlabel('Count', fontsize=12, color='white')
    plt.ylabel('Competition', fontsize=12, color='white')

    # Adjust layout and display the plot
    plt.tight_layout()
    st.pyplot(plt)

    # 2.3 Position Column
    st.subheader("2.3 Position Column")

    # Plot for 'position' column
    plt.figure(figsize=(6, 4))
    plt.style.use('dark_background')

    # Get the counts for each category
    counts = df['position'].value_counts()

    # Calculate the thresholds for small, medium, and high categories
    thresholds = [counts.quantile(0.33), counts.quantile(0.66)]

    # Create the count plot
    bar_plot = sns.countplot(y=df['position'], order=counts.index)

    # Manually color the bars based on their count
    for p in bar_plot.patches:
        count = int(p.get_width())
        color = get_color(count, thresholds)
        p.set_color(color)

        # Add numbers on each bar
        bar_plot.annotate(f'{count}', xy=(count, p.get_y() + p.get_height() / 2),
                          xytext=(-10, 0), textcoords='offset points',
                          ha='center', va='center', fontsize=12, color='white', fontweight='bold')

    # Set title and labels with white color
    plt.title('Frequency of Position', fontsize=14, fontweight='bold', color='white')
    plt.xlabel('Count', fontsize=12, color='white')
    plt.ylabel('Position', fontsize=12, color='white')

    # Adjust layout and display the plot
    plt.tight_layout()
    st.pyplot(plt)

    # 2.4 First Tier Column
    st.subheader("2.4 First Tier Column")

    # Plot for 'first_tier' column
    plt.figure(figsize=(6, 4))
    plt.style.use('dark_background')

    # Get the counts for each category
    counts = df['first_tier'].value_counts()

    # Calculate the thresholds for small, medium, and high categories
    thresholds = [counts.quantile(0.33), counts.quantile(0.66)]

    # Create the count plot
    bar_plot = sns.countplot(y=df['first_tier'], order=counts.index)

    # Manually color the bars based on their count
    for p in bar_plot.patches:
        count = int(p.get_width())
        color = get_color(count, thresholds)
        p.set_color(color)

        # Add numbers on each bar
        bar_plot.annotate(f'{count}', xy=(count, p.get_y() + p.get_height() / 2),
                          xytext=(-10, 0), textcoords='offset points',
                          ha='center', va='center', fontsize=12, color='white', fontweight='bold')

    # Set title and labels with white color
    plt.title('Frequency of First Tier', fontsize=14, fontweight='bold', color='white')
    plt.xlabel('Count', fontsize=12, color='white')
    plt.ylabel('First Tier', fontsize=12, color='white')

    # Adjust layout and display the plot
    plt.tight_layout()
    st.pyplot(plt)

    # 3. Summary Statistics (Numerical)
    st.subheader("3. Summary Statistics (Numerical)")
    # Columns transformations mapping as provided
    columns_transformations = {
        'revenue': 'log_revenue',
        'spent': 'log_spent',
        'net': 'net_cube_root',
        'goals_for': 'sqrt_goals_for',
        'relative': 'log_relative',
        '5_season_agg': 'log_5_season_agg',
        '5_season_net': 'winsorized_5_season_net',
        '5_season_league_agg': 'log_5_season_league_agg',
        '5_season_relative': 'log_5_season_relative',
        'wins': None  # Assuming no transformation was applied to wins
    }

    # Set plot style to dark
    plt.style.use('dark_background')

    # Create subplots for original and transformed distributions and box plots with a black background
    fig, axes = plt.subplots(nrows=len(columns_transformations), ncols=4, figsize=(20, 24), facecolor='black')

    for i, (original_col, transformed_col) in enumerate(columns_transformations.items()):
        # Plot the original distribution
        sns.histplot(df[original_col], kde=True, ax=axes[i, 0], color='skyblue')
        axes[i, 0].set_title(f'Original Distribution of {original_col}')
        axes[i, 0].set_xlabel(original_col)
        axes[i, 0].set_ylabel('Frequency')

        # Plot the transformed distribution (if a transformation exists)
        if transformed_col:
            sns.histplot(df[transformed_col], kde=True, ax=axes[i, 1], color='coral')
            axes[i, 1].set_title(f'Transformed Distribution of {transformed_col}')
            axes[i, 1].set_xlabel(transformed_col)
            axes[i, 1].set_ylabel('Frequency')
        else:
            axes[i, 1].set_visible(False)  # Hide the plot if no transformation

        # Plot the original box plot
        sns.boxplot(x=df[original_col], ax=axes[i, 2], color='lightgreen')
        axes[i, 2].set_title(f'Original Boxplot of {original_col}')
        axes[i, 2].set_xlabel(original_col)

        # Plot the transformed box plot (if a transformation exists)
        if transformed_col:
            sns.boxplot(x=df[transformed_col], ax=axes[i, 3], color='lightcoral')
            axes[i, 3].set_title(f'Transformed Boxplot of {transformed_col}')
            axes[i, 3].set_xlabel(transformed_col)
        else:
            axes[i, 3].set_visible(False)  # Hide the plot if no transformation

    # Adjust layout for better spacing
    plt.tight_layout()

    # Display the plots in Streamlit
    st.pyplot(fig)

    # Correlation Analysis Section
elif option == "Correlation Analysis":
    st.subheader("1. Relationship between Revenue and Spent")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='revenue', y='spent', color='blue', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Spent vs Revenue', color='white')
    plt.xlabel('Revenue', color='white')
    plt.ylabel('Spent', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())
    st.subheader("2. Correlation between Revenue and net Balance")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='revenue', y='net', color='green', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Net vs Revenue', color='white')
    plt.xlabel('Revenue', color='white')
    plt.ylabel('Net', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())
    st.subheader("3. Impact of Spending on Wins")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='spent', y='wins', color='red', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Wins vs Spent', color='white')
    plt.xlabel('Spent', color='white')
    plt.ylabel('Wins', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())
    st.subheader("4. Relationship between Goals Scored and Wins")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='goals_for', y='wins', color='purple', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Wins vs Goals For', color='white')
    plt.xlabel('Goals For', color='white')
    plt.ylabel('Wins', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())
    st.subheader("5. Impact of Goals Conceded on Wins")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='goals_against', y='wins', color='orange', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Wins vs Goals Against', color='white')
    plt.xlabel('Goals Against', color='white')
    plt.ylabel('Wins', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())
    st.subheader("6. Correlation between Relative Spending and Wins")
    # Set up the plotting style and figure size with a black background for the scatter plot
    plt.figure(figsize=(4, 2))
    plt.style.use('dark_background')  # Set the background to black

    # Create the scatter plot
    sns.scatterplot(data=df, x='relative', y='wins', color='cyan', alpha=0.6)

    # Set titles and labels with white color to match the dark background
    plt.title('Wins vs Relative', color='white')
    plt.xlabel('Relative', color='white')
    plt.ylabel('Wins', color='white')

    # Display the scatter plot in Streamlit
    st.pyplot(plt.gcf())

elif option == "League-Wise Analysis":

    st.subheader("1. Average Revenue by League")
    # Aggregate data by league
    league_agg = df.groupby('league').agg({
        'revenue': 'mean',
        'spent': 'mean',
        'net': 'mean',
        'wins': 'mean',
        'goals_for': 'mean',
        'goals_against': 'mean',
        'relative': 'mean'
        }).reset_index()
    # Define color shades for high, medium, and small categories
    high_color = '#FF5733'    # Bright red-orange for high values
    medium_color = '#FFC300'  # Golden yellow for medium values
    small_color = '#28B463'   # Fresh green for small values

    # Calculate the thresholds for small, medium, and high revenue categories
    revenue_thresholds = [
    league_agg['revenue'].quantile(0.33),
    league_agg['revenue'].quantile(0.66)
    ]

    # Function to determine color based on revenue
    def get_revenue_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color

    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='revenue', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their revenue value
    for i, p in enumerate(bar_plot.patches):
        revenue = league_agg['revenue'].iloc[i]
        color = get_revenue_color(revenue, revenue_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its revenue value
        bar_plot.annotate(f'{revenue:.2f}', 
                      xy=(revenue, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Revenue by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Revenue (in million euros)', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())


    st.subheader("2. Average Spending by League")

    # Define color shades for high, medium, and small spending categories
    high_color = '#1f77b4'    # Blue for high values
    medium_color = '#ff7f0e'  # Orange for medium values
    small_color = '#2ca02c'   # Green for small values

    # Calculate the thresholds for small, medium, and high spending categories
    spending_thresholds = [
        league_agg['spent'].quantile(0.33),
        league_agg['spent'].quantile(0.66)
        ]

    # Function to determine color based on spending
    def get_spending_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color
    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='spent', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their spending value
    for i, p in enumerate(bar_plot.patches):
        spending = league_agg['spent'].iloc[i]
        color = get_spending_color(spending, spending_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its spending value
        bar_plot.annotate(f'{spending:.2f}', 
                      xy=(spending, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Spending by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Spending (in million euros)', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

    st.subheader("3. Average Net Balance by League")

    # Define colors for high, medium, and negative net balances
    high_positive_color = '#76c7c0'  # Teal for high positive values
    medium_color = '#ffdd57'         # Yellow for medium values
    negative_color = '#ff6f69'       # Coral Red for negative values

    # Calculate the thresholds for small, medium, and high positive net balances
    positive_thresholds = [
        league_agg['net'].clip(lower=0).quantile(0.33),  # Only consider positive values
        league_agg['net'].clip(lower=0).quantile(0.66)
        ]

    # Function to determine color based on net balance
    def get_net_color(value, thresholds):
        if value < 0:
            return negative_color
        elif value > thresholds[1]:
            return high_positive_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return medium_color  # Default to medium color if thresholds are not met
        
    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='net', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their net balance value
    for i, p in enumerate(bar_plot.patches):
        net_balance = league_agg['net'].iloc[i]
        color = get_net_color(net_balance, positive_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its net balance value
        bar_plot.annotate(f'{net_balance:.2f}', 
                      xy=(net_balance, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Net Balance by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Net Balance (in million euros)', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

    st.subheader("4. Average Wins by League")

    # Define color shades for high, medium, and small win categories
    high_color = '#1f78b4'    # Blue for high values
    medium_color = '#33a02c'  # Green for medium values
    small_color = '#fb9a99'   # Light Pink for small values

    # Calculate the thresholds for small, medium, and high win categories
    win_thresholds = [
        league_agg['wins'].quantile(0.33),
        league_agg['wins'].quantile(0.66)
        ]

    # Function to determine color based on wins
    def get_win_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color
        
    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='wins', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their win value
    for i, p in enumerate(bar_plot.patches):
        wins = league_agg['wins'].iloc[i]
        color = get_win_color(wins, win_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its win value
        bar_plot.annotate(f'{wins:.2f}', 
                      xy=(wins, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Wins by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Wins', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())


    st.subheader("5. Average Goals For by League")

    # Define light color shades for high, medium, and small goals_for categories
    high_color = '#ff9999'    # Light Red for high values
    medium_color = '#99c2ff'  # Light Blue for medium values
    small_color = '#99ff99'   # Light Green for small values

    # Calculate the thresholds for small, medium, and high goals_for categories
    goals_thresholds = [
        league_agg['goals_for'].quantile(0.33),
        league_agg['goals_for'].quantile(0.66)
        ]

    # Function to determine color based on goals_for
    def get_goals_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color
        
    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='goals_for', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their goals_for value
    for i, p in enumerate(bar_plot.patches):
        goals_for = league_agg['goals_for'].iloc[i]
        color = get_goals_color(goals_for, goals_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its goals_for value
        bar_plot.annotate(f'{goals_for:.2f}', 
                      xy=(goals_for, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Goals For by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Goals For', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())


    st.subheader("6. Average Goals Against by League")

    # Define light color shades for high, medium, and small goals_against categories
    high_color = '#ffa07a'    # Light Salmon/Orange for high values
    medium_color = '#ffeb99'  # Light Yellow for medium values
    small_color = '#add8e6'   # Light Blue for small values

    # Calculate the thresholds for small, medium, and high goals_against categories
    goals_against_thresholds = [
        league_agg['goals_against'].quantile(0.33),
        league_agg['goals_against'].quantile(0.66)
        ]

    # Function to determine color based on goals_against
    def get_goals_against_color(value, thresholds):
        if value > thresholds[1]:
            return high_color
        elif value > thresholds[0]:
            return medium_color
        else:
            return small_color

    # Define the figure size and set black background
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')  # Set the background to black

    # Create a barplot without specifying the palette, using errorbar=None to avoid the warning
    bar_plot = sns.barplot(x='goals_against', y='league', data=league_agg, errorbar=None)

    # Manually color the bars based on their goals_against value
    for i, p in enumerate(bar_plot.patches):
        goals_against = league_agg['goals_against'].iloc[i]
        color = get_goals_against_color(goals_against, goals_against_thresholds)
        p.set_facecolor(color)
    
        # Annotate each bar with its goals_against value
        bar_plot.annotate(f'{goals_against:.2f}', 
                      xy=(goals_against, p.get_y() + p.get_height() / 2), 
                      xytext=(5, 0), 
                      textcoords='offset points', 
                      ha='left', va='center', fontsize=10, color='white', fontweight='bold')  # Change annotation color to white

    # Set the title and labels with enhanced font size for clarity
    plt.title('Average Goals Against by League', fontsize=14, color='white')  # Set title color to white
    plt.xlabel('Average Goals Against', fontsize=12, color='white')  # Set x-label color to white
    plt.ylabel('League', fontsize=12, color='white')  # Set y-label color to white

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

elif option == "Financial Performance":

    st.subheader("1. Financial Efficiency Over Time (All Leagues)")

    # Aggregate key financial metrics by season across all leagues
    season_agg = df.groupby('season').agg({
    'revenue': 'mean',
    'spent': 'mean',
    'net': 'mean',
    }).reset_index()

    # Set up the figure size and layout for trend visualizations
    plt.figure(figsize=(14, 8))

    # Plot trends in financial metrics over time
    plt.plot(season_agg['season'], season_agg['revenue'], label='Average Revenue', marker='o', color='#00FFFF')
    plt.plot(season_agg['season'], season_agg['spent'], label='Average Spending', marker='o', color='#39FF14')
    plt.plot(season_agg['season'], season_agg['net'], label='Average Net Balance', marker='o', color='#FF1493')

    # Customize the plot
    plt.title('Trends in Financial Efficiency Over Time (All Leagues)')
    plt.xlabel('Season')
    plt.ylabel('Amount (in million euros)')
    plt.legend()
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

    st.subheader("2. Comparative Analysis: Spain vs. England")

    st.subheader("2.1 Revenue Trends")

    # Filter the data for Spain and England
    spain_england_df = df[df['league'].isin(['Spain', 'England'])]

    # Aggregate financial metrics by season for Spain and England
    spain_england_agg = spain_england_df.groupby(['season', 'league']).agg({
        'revenue': 'mean',
        'spent': 'mean',
        'net': 'mean',
        }).reset_index()


    # Define a new custom color palette
    custom_palette = sns.color_palette(["#2ca02c", "#d62728"])  # Green and Red colors

    # Plot Revenue trends with custom colors
    plt.figure(figsize=(14, 6))
    plt.style.use('dark_background')  # Use a dark background
    sns.lineplot(data=spain_england_agg, x='season', y='revenue', hue='league', marker='o', palette=custom_palette)

    # Customize the plot
    plt.title('Average Revenue Over Time: Spain vs. England', color='white')
    plt.xlabel('Season', color='white')
    plt.ylabel('Average Revenue (in million euros)', color='white')
    plt.grid(True, color='gray')
    plt.legend(title='League', title_fontsize='13', fontsize='11', loc='best', facecolor='black', edgecolor='white', labelcolor=['#2ca02c', '#d62728'])

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

    st.subheader("2.2 Spending Trends")

    # Define a custom color palette with purple and teal
    custom_palette = sns.color_palette(["#9467bd", "#17becf"])  # Purple and Teal colors

    # Plot Spending trends with custom colors
    plt.figure(figsize=(14, 6))
    plt.style.use('dark_background')  # Use a dark background
    sns.lineplot(data=spain_england_agg, x='season', y='spent', hue='league', marker='o', palette=custom_palette)

    # Customize the plot
    plt.title('Average Spending Over Time: Spain vs. England', color='white')
    plt.xlabel('Season', color='white')
    plt.ylabel('Average Spending (in million euros)', color='white')
    plt.grid(True, color='gray')
    plt.legend(title='League', title_fontsize='13', fontsize='11', loc='best', facecolor='black', edgecolor='white', labelcolor=['#9467bd', '#17becf'])

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())

    st.subheader("2.3 Net Balance Trends")

    # Define a custom color palette with dark gray and olive
    custom_palette = sns.color_palette(["#ff6699", "#808000"])  # Pink and Olive colors

    # Plot Net Balance trends with custom colors
    plt.figure(figsize=(14, 6))
    plt.style.use('dark_background')  # Use a dark background
    sns.lineplot(data=spain_england_agg, x='season', y='net', hue='league', marker='o', palette=custom_palette)

    # Customize the plot
    plt.title('Average Net Balance Over Time: Spain vs. England', color='white')
    plt.xlabel('Season', color='white')
    plt.ylabel('Average Net Balance (in million euros)', color='white')
    plt.grid(True, color='gray')
    plt.legend(title='League', title_fontsize='13', fontsize='11', loc='best', facecolor='black', edgecolor='white', labelcolor=['#ff6699', '#808000'])

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())