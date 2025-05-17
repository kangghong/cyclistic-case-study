## Functions for analyzing casual vs member riders
import matplotlib.pyplot as plt

def generate_pie(data, category):

        # Count the occurrences of each membership status
    status_counts = data[f'{category}'].value_counts()

    # Create a pie chart
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)

    # Add a title
    plt.title(f'Proportion of {category}')


'''def generate_prop_plot (data, cat1, cat2, event):

    freq_rideable = data.groupby(
        [cat1, cat2]
        ).size().unstack(fill_value=0)
    
    prop_rideable = freq_rideable.div(
        freq_rideable.sum(axis=1), axis=0)*100
    
    print(prop_rideable)
    
    prop_rideable.plot(kind='bar')

    plt.title(f"Proportion of {cat1}, by {cat2} in the {event} (%)")
    plt.xlabel(f"{cat2}")
    plt.ylabel('Percentage')
    plt.legend(title=f"{cat1}")

    plt.show()'''

def generate_prop_plot(data, cat1, cat2, event, third_category=None, plot_kind='bar', figsize=(10, 6)):
    """
    Generate a proportion plot showing the distribution of cat1 by cat2 within an event.
    
    Parameters:
    - data: DataFrame containing the data.
    - cat1: The main category column.
    - cat2: The subcategory column.
    - event: The event or context for the plot title.
    - third_category: Optional third category column for more detailed grouping.
    - plot_kind: The kind of plot to generate (default is 'bar').
    - figsize: The size of the figure (default is (10, 6)).
    """
    # Step 1: Create the frequency table
    if third_category:
        freq_table = data.pivot_table(
            index=[cat1, third_category],
            columns=cat2,
            aggfunc='size',
            fill_value=0
        ).unstack(fill_value=0)
    else:
        freq_table = data.pivot_table(
            index=cat1,
            columns=cat2,
            aggfunc='size',
            fill_value=0
        )
    
    # Step 2: Convert frequency table to proportion table
    prop_table = freq_table.div(freq_table.sum(axis=1), axis=0) * 100
    
    # Print the proportion table for reference
    print(prop_table)
    
    # Step 3: Plot the proportion table
    prop_table.plot(kind=plot_kind, figsize=figsize, stacked=(plot_kind == 'bar'))
    
    # Step 4: Customize the plot
    if third_category:
        plt.title(f"Proportion of {cat2} by {cat1} and {third_category} in the {event} (%)")
        plt.xlabel(f"{cat1}")
        plt.ylabel('Percentage')
        plt.legend(title=f"{cat2} by {third_category}")
    else:
        plt.title(f"Proportion of {cat1} by {cat2} in the {event} (%)")
        plt.xlabel(f"{cat1}")
        plt.ylabel('Percentage')
        plt.legend(title=f"{cat2}")
    
    # Step 5: Show the plot
    plt.show()


def generate_hist_plot(data, category, subcategory1):

    freq_table = data.groupby([f'{subcategory1}', f'{category}']).size().unstack(fill_value=0)
    prop_table = freq_table.div(freq_table.sum(), axis=1)*100

    prop_table.plot(kind='bar')

    plt.title(f'{category} vs {subcategory1} (%)')
    plt.xlabel(f'{category}')
    plt.ylabel('Percentage')
    plt.legend(title=f'{subcategory1}')

    plt.show()

    


'''def generate_stack_hist (data, category, subcategory):

    freq_table = data.groupby([f'{category}', f'{subcategory}']).size().unstack(fill_value=0)

    prop_table = freq_table.div(freq_table.sum(axis=1), axis=0)*100
    print(prop_table)

    prop_table.plot(kind='bar', stacked=True)

    plt.title(f'Proportion of {category}, by {subcategory} (%)')
    plt.xlabel(f'{subcategory}')
    plt.ylabel('Percentage')
    plt.legend(title=f'{category}')

    plt.show()'''

def plot_pivot_table(data, index, columns, aggfunc, title, xlabel, ylabel, legend_title, figsize=(10, 6), values=None):
    """
    Generate a pivot table and plot it as a bar chart.

    Parameters:
    - data: DataFrame containing the data.
    - values: Column name to aggregate.
    - index: Column name to group by for the index of the pivot table.
    - columns: Column name to group by for the columns of the pivot table.
    - aggfunc: Aggregation function to use (e.g., 'median', 'mean', 'sum').
    - title: Title of the plot.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - legend_title: Title for the legend.
    - figsize: Figure size (default is (10, 6)).
    """

    if aggfunc == 'size':
        pivot_table = data.pivot_table(
            index=index,
            columns=columns,
            aggfunc='size',
            fill_value=0
        )

    pivot_table = data.pivot_table(
        values=values,
        index=index,
        columns=columns,
        aggfunc=aggfunc,
        fill_value=0
    )

    # Step 2: Plot the pivot table
    pivot_table.plot(kind='bar', figsize=figsize)

    # Step 3: Customize the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=legend_title)

    # Step 4: Show the plot
    plt.show()

def generate_stack_hist(data, category, subcategory, third_category=None):
    """
    Generate a stacked bar chart showing the proportion of a category by a subcategory.
    
    Parameters:
    - data: DataFrame containing the data.
    - category: The main category column.
    - subcategory: The subcategory column.
    - third_category: Optional third category column for more detailed grouping.
    """
    # Step 1: Create the frequency table
    if third_category:
        freq_table = data.pivot_table(
            index=[category, third_category],
            columns=subcategory,
            aggfunc='size',
            fill_value=0
        ).unstack(fill_value=0)
    else:
        freq_table = data.pivot_table(
            index=category,
            columns=subcategory,
            aggfunc='size',
            fill_value=0
        )
    
    # Step 2: Convert frequency table to proportion table
    prop_table = freq_table.div(freq_table.sum(axis=1), axis=0) * 100

    # Step 3: Plot the proportion table
    prop_table.plot(kind='bar', stacked=True, figsize=(10, 6))

    # Step 4: Customize the plot
    if third_category:
        plt.title(f'Proportion of {category} by {subcategory} and {third_category} (%)')
        plt.xlabel(f'{subcategory}')
        plt.ylabel('Percentage')
        plt.legend(title=f'{category} by {third_category}')
    else:
        plt.title(f'Proportion of {category} by {subcategory} (%)')
        plt.xlabel(f'{subcategory}')
        plt.ylabel('Percentage')
        plt.legend(title=f'{category}')

    # Step 5: Show the plot
    plt.show()