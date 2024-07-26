import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from .config import config
IMAGES_PATH = config.ARTIFACTS_PATH / 'images'

def plot_density(
        data, 
        x_col,
        hue_col,
        y_label='',
        x_label='',
        title='',
        colors=['lightgrey'],
        hue_order=None,
        export_fig=False,
        filename=False,
        xlim=None
    ):
    sns.set_theme(style='ticks', font_scale=1.5)
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.grid(visible=True, linestyle='--', alpha=1.0)
    ax = sns.kdeplot(
        data=data
        , x=x_col
        , hue=hue_col
        , hue_order=hue_order
        , palette=colors
        , ax=ax
        , fill=True
    )

    _ = ax.set(
        ylabel = (y_label)
        , xlabel = (x_label)
        , title = (title)
        , xlim = xlim
    )

    # Remove os ticks
    ax.tick_params(bottom = False, left=False)

    # Remove os labels dos ticks
    _ = ax.set_yticks([])

    # _ = ax.legend(frameon=False)
    
    # Remove as bordas do quadro
    sns.despine(
        bottom=True
        , left=True
        , right=True
        , top=True)
    plt.show()
    
    if export_fig:
        fig.savefig(
            IMAGES_PATH / f'{filename}.png'
            , dpi=300
            , bbox_inches='tight'
        )
    
def plot_histogram(
        data, 
        x_col,
        y_label='',
        x_label='',
        title='',
        show_percentiles=False,
    ):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax = sns.histplot(
            data=data
            , x=x_col
            , color='lightgrey'
            , ax=ax
    )

    _ = ax.set(
        ylabel = (y_label)
        , xlabel = (x_label)
        , title = (title)
    )
    
    # Calculate the 25th, 50th, and 75th percentiles
    percentile_25 = np.percentile(data[x_col], 25)
    percentile_50 = np.percentile(data[x_col], 50)
    percentile_75 = np.percentile(data[x_col], 75)

    if show_percentiles:
        # Add vertical lines and annotations for percentiles
        ax.axvline(
            x=percentile_25, 
            color='black', 
            linestyle='--', 
            label='25th Percentile'
        )
        ax.axvline(
            x=percentile_50, 
            color='black', 
            linestyle='--', 
            label='50th Percentile'
        
        )
        ax.axvline(
            x=percentile_75, 
            color='black', 
            linestyle='--', 
            label='75th Percentile'
        )

    # Remove as bordas do quadro
    sns.despine(
        bottom=True
        , left=True
        , right=True
        , top=True)
    plt.show()

def plot_boxplot(
        data, 
        y_col,
        y_label='',
        x_label='',
        title='',):
    
    fig, ax = plt.subplots(figsize=(10, 5))
    g = sns.boxplot(
            data=data
            , y=y_col
            , fliersize=0.5
            # , width = 0.5
            # , linewidth=0.5
            , palette=sns.color_palette(['lightgrey'])
            , ax=ax
    )

    _ = g.set(
        ylabel = (y_label)
        , xlabel = (x_label)
        , title = (title)
    )

    # Remove as bordas do quadro
    sns.despine(
        bottom=True
        , left=True
        , right=True
        , top=True)
    plt.show()

    
def plot_times_distribution(
        df_plot, 
        budget_line=None, 
        title='', 
        palette=None,
        legend_visible=True
    ):
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.grid(visible=True, linestyle='--', alpha=0.5)

    ax = sns.kdeplot(
            data=df_plot
            , x='value'
            , hue='variable'
            , ax=ax
            , palette=palette
    )

    _ = ax.set(
            ylabel = ('')
            , xlabel = ('Hours')
            , title = (title)
            , xlim = (0, 175)
            , xticks = np.arange(0, 175, 10)
        )
    # Remove os ticks
    ax.tick_params(bottom = False, left=False)

    # Remove os labels dos ticks
    _ = ax.set_yticks([])
    
    if not budget_line is None:
        ax.axvline(
            x=budget_line, 
            color='black', 
            linestyle='--',
            label='Budget'
        )
        # ax.annotate(
        #     f'{budget_line:.2f}', 
        #     (budget_line, ax.get_ylim()[1]), 
        #     xytext=(5, 10),
        #     textcoords='offset points', 
        #     color='black', 
        #     fontsize=12, 
        #     ha='center'
        # )
    if not legend_visible:
        ax.legend().set_visible(False)
    sns.despine(
        bottom=True
        , left=True
        , right=True
        , top=True
    )

def plot_lineplot(
    df_plot, 
    x_col, 
    y_col,
    hue_col,
    x_label='',
    y_label='',
    title=''
):
    fig, ax = plt.subplots(figsize=(10, 5))
    g = sns.lineplot(
            data=df_plot
            , x=x_col
            , y=y_col
            , hue=hue_col
            , ax=ax
    )

    _ = g.set(
        ylabel = (y_label)
        , xlabel = (x_label)
        , title = (title)
    )

    # Remove as bordas do quadro
    sns.despine(
        bottom=True
        , left=True
        , right=True
        , top=True)
    plt.show()
    