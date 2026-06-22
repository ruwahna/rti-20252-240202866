import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create directories if they don't exist
os.makedirs('../06-output/tables', exist_ok=True)
os.makedirs('../06-output/figures', exist_ok=True)

# 1. Read Data
df = pd.read_csv('../04-data/survey_data_signal_sakpole.csv')

# 2. Clean Data (Remove missing and outliers > 100)
df = df.dropna(subset=['SUS_Score'])
df = df[df['SUS_Score'] <= 100]

# Split groups
signal_scores = df[df['Aplikasi'] == 'SIGNAL']['SUS_Score']
sakpole_scores = df[df['Aplikasi'] == 'New Sakpole']['SUS_Score']

# 3. Descriptive Stats
n1, n2 = len(signal_scores), len(sakpole_scores)
m1, m2 = np.mean(signal_scores), np.mean(sakpole_scores)
std1, std2 = np.std(signal_scores, ddof=1), np.std(sakpole_scores, ddof=1)

desc_stats = pd.DataFrame({
    'Aplikasi': ['SIGNAL', 'New Sakpole'],
    'Mean': [round(m1, 2), round(m2, 2)],
    'Standard_Deviation': [round(std1, 2), round(std2, 2)],
    'Sample_Size_n': [n1, n2]
})

def df_to_markdown(dataframe, filename):
    with open(filename, 'w') as f:
        f.write('| ' + ' | '.join(dataframe.columns) + ' |\n')
        f.write('|' + '|'.join(['---'] * len(dataframe.columns)) + '|\n')
        for index, row in dataframe.iterrows():
            f.write('| ' + ' | '.join([str(val) for val in row]) + ' |\n')

df_to_markdown(desc_stats, '../06-output/tables/descriptive_stats.md')

# 4. T-Test Calculations (Manual since no scipy)
var1, var2 = np.var(signal_scores, ddof=1), np.var(sakpole_scores, ddof=1)
dof = n1 + n2 - 2
sp = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / dof)
t_stat = (m1 - m2) / (sp * np.sqrt(1/n1 + 1/n2))
cohens_d = (m1 - m2) / sp

# p-value approximation (very small)
p_value = "< 0.001" if abs(t_stat) > 3.3 else "Calculate manually"

t_test_results = pd.DataFrame({
    'Test': ['Independent T-Test'],
    't_statistic': [round(t_stat, 2)],
    'Degrees_of_Freedom': [dof],
    'p_value': [p_value],
    'Cohens_d': [round(cohens_d, 2)]
})
df_to_markdown(t_test_results, '../06-output/tables/t_test_results.md')

# 5. Visualizations: Bar Chart with Error Bars
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(['SIGNAL', 'New Sakpole'], [m1, m2], yerr=[std1, std2], capsize=10, color=['#4C72B0', '#C44E52'])

# Add horizontal line for SUS industry standard
ax.axhline(y=68, color='r', linestyle='--', label='Batas Kelayakan Minimum (68)')

# Formatting
ax.set_ylabel('Rata-rata Skor SUS')
ax.set_title('Perbandingan Skor Usability: SIGNAL vs New Sakpole')
ax.set_ylim(0, 100)
ax.legend()

# Add text labels
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval - 10, round(yval, 2), ha='center', va='bottom', color='white', fontweight='bold')

plt.tight_layout()
plt.savefig('../06-output/figures/fig_sus_comparison.png', dpi=300)

# 6. Visualizations: Box Plot for Distribution
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.boxplot([signal_scores, sakpole_scores], patch_artist=True)
ax2.set_xticks([1, 2])
ax2.set_xticklabels(['SIGNAL', 'New Sakpole'])
ax2.set_ylabel('Skor SUS')
ax2.set_title('Distribusi Persebaran Skor SUS Responden')
ax2.axhline(y=68, color='r', linestyle='--', label='Batas Kelayakan Minimum (68)')
ax2.legend()
plt.tight_layout()
plt.savefig('../06-output/figures/fig_sus_distribution.png', dpi=300)

print("All outputs generated successfully in 06-output!")
