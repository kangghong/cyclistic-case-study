## Functions for analyzing casual vs member riders
import matplotlib.pyplot as plt


def generate_prop_plot (data, cat1, cat2, season):

    freq_rideable = data.groupby(
        [cat1, cat2]
        ).size().unstack(fill_value=0)
    
    prop_rideable = freq_rideable.div(
        freq_rideable.sum(axis=1), axis=0)*100
    
    print(prop_rideable)
    
    prop_rideable.plot(kind='bar', stacked=True)

    plt.title(f"Proportion of {cat1}, by {cat2} in the {season} (%)")
    plt.xlabel(f"{cat2}")
    plt.ylabel('Percentage')
    plt.legend(title=f"{cat1}")

    plt.show()


