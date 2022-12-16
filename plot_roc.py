import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('./results/analysis.csv').drop(['Features'], axis=1)
df1 = pd.read_csv('./results/analysis.csv').drop(['Features'], axis=1)

fig, axs = plt.subplots(nrows=2, ncols=3, sharey=True, sharex=True)
fig.tight_layout()

p1 = sns.scatterplot(data=df, x='Components', y='Low/VeryLow', ax=axs[0, 0], hue='PCA Method')
p2 = sns.scatterplot(data=df, x='Components', y='Intermediate', ax=axs[0, 1], hue='PCA Method', legend=False)
p3 = sns.scatterplot(data=df, x='Components', y='High/VeryHigh', ax=axs[0, 2], hue='PCA Method', legend=False)

p4 = sns.scatterplot(data=df1, x='Components', y='Low/VeryLow', ax=axs[1, 0], hue='PCA Method', legend=False)
p5 = sns.scatterplot(data=df1, x='Components', y='Intermediate', ax=axs[1, 1], hue='PCA Method', legend=False)
p6 = sns.scatterplot(data=df1, x='Components', y='High/VeryHigh', ax=axs[1, 2], hue='PCA Method', legend=False)

p1.set_ylabel('AUROC Values')
p2.text(17, 0, 'Pyradiomics', size=25, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
        )
p5.text(17, 1, 'LIFEx', size=25, ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
        )
p4.set_ylabel('AUROC Values')
p4.set_xlabel('')
p5.set_xlabel('Number of Components')
p6.set_xlabel('')
p1.set_title('Low/VeryLow')
p2.set_title('Intermediate')
p3.set_title('High/VeryHigh')

plt.show()