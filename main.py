import json
import matplotlib.pyplot as plt

def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def plot_bar_chart(ax, age_groups):
    labels = list(age_groups.keys())
    counts = list(age_groups.values())

    bars = ax.bar(labels, counts, color='#0366d6')
    ax.set_title('Bar Chart: Age Group Distribution', fontsize=14, weight='bold', pad=15)
    ax.set_xlabel('Age Groups', fontsize=12)
    ax.set_ylabel('Number of People', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.grid(axis='x', visible=False)
    ax.tick_params(axis='x', labelrotation=45, labelsize=10)
    ax.tick_params(axis='y', labelsize=11)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    color='#24292e',
                    weight='bold')

def plot_histogram(ax, ages):
    bins = [0,10,20,30,40,50,60,70,80,90]
    ax.hist(ages, bins=bins, color='#24a0ed', edgecolor='white', linewidth=1.2)
    ax.set_title('Histogram: Age Distribution (Continuous)', fontsize=14, weight='bold', pad=15)
    ax.set_xlabel('Age', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.grid(axis='x', visible=False)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=11)
    ax.set_xticks(bins)

def main():
    data = load_data("data.json")  # Assumes data.json is in the same directory as this script
    age_groups = data["age_groups"]
    ages = data["ages"]

    fig, axs = plt.subplots(1, 2, figsize=(14,6), constrained_layout=True)
    plot_bar_chart(axs[0], age_groups)
    plot_histogram(axs[1], ages)
    fig.suptitle('Age Distribution Visualization: Bar Chart and Histogram from JSON Data', fontsize=16, weight='bold', y=1.03)
    plt.show()

if __name__ == "__main__":
    main()

