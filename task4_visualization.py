import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1 — Setup (2 marks)
# Load data/trends_analysed.csv into a DataFrame
df = pd.read_csv("data/trends_analysed.csv")
df

# Create a folder called outputs/ if it doesn't exist
os.makedirs("outputs" , exist_ok=True)

# Use plt.savefig() before any plt.show() on all charts

# --------------------------------------------------------------------------

# 2 — Chart 1: Top 10 Stories by Score (6 marks)
# Create a horizontal bar chart showing the top 10 stories by score
# Use the story title on the y-axis (shorten titles longer than 50 characters)
# Add a title and axis labels
# Save as outputs/chart1_top_stories.png
top_10_score = df.sort_values(by='score',ascending=False).head(10)

top_10_score['short_title'] = top_10_score['title'].apply(lambda x : x[:30]  if len(x) > 30 else x)
# print(top_10_score)

plt.figure(figsize=(10,6))

sns.barplot(data = df , x = top_10_score['score'], y = top_10_score['short_title'] , palette='Set2' )

plt.title("Top 10 stories by score" , fontsize = 18 ,fontweight = "bold")
plt.xlabel("Score" , fontsize = 16)
plt.ylabel("Title" , fontsize = 16)
plt.grid(alpha = 0.3)
plt.tight_layout()



plt.savefig("outputs/chart1_top_posts.png")

plt.show()


# ---------------------------------------------------------------------------------

# 3 — Chart 2: Stories per Category (6 marks)
# Create a bar chart showing how many stories came from each category
# Use a different colour for each bar
# Add a title and axis labels
# Save as outputs/chart2_categories.png

category_story= df['subreddit'].value_counts().reset_index()

category_story.Columns = ['subreddit' , 'count']

plt.figure(figsize=(8,6))

sns.barplot(data = category_story , x = 'subreddit' , y= 'count' , palette= 'Set1')

plt.title("Stories came from each category" , fontsize = 18 ,fontweight = "bold")
plt.xlabel("Category" , fontsize = 16)
plt.ylabel("Count" , fontsize = 16)
plt.grid(alpha = 0.3)
plt.tight_layout()


plt.savefig("outputs/chart2_categories.png")

plt.show()


# --------------------------------------------------------------------------------

# 4 — Chart 3: Score vs Comments (6 marks)
# Create a scatter plot with score on the x-axis and num_comments on the y-axis
# Colour the dots differently for popular vs non-popular stories (use the is_popular column)
# Add a legend, title, and axis labels
# Save as outputs/chart3_scatter.png

df

plt.figure(figsize=(10,6))

sns.scatterplot(data =df, x = 'score' , y = 'num_comments' , hue='is_popular')

plt.title("Score vs Comments (Popularity Analysis", fontsize = 18 ,fontweight = "bold")
plt.xlabel("Score" , fontsize = 16)
plt.ylabel("Num_Comments" , fontsize = 16)
plt.grid(alpha = 0.3)
plt.tight_layout()


plt.savefig("outputs/chart3_scatter.png")

plt.show()


# ----------------------------------------------------------------------------

# Bonus — Dashboard (+3 marks)
# Combine all 3 charts into one figure:

# Use plt.subplots(1, 3) or plt.subplots(2, 2) to lay them out together
# Add an overall title: "TrendPulse Dashboard"
# Save as outputs/dashboard.png

plt.figure(figsize=(14, 10))
plt.suptitle("TrendPulse Dashboard", fontsize=18, fontweight="bold")

plt.subplot(2,2,1)

sns.barplot(data = df , x = top_10_score['score'], y = top_10_score['short_title'] , palette='Set2' )
plt.title("Top 10 stories by score" , fontsize = 14)
plt.xlabel("Score" , fontsize = 12)
plt.ylabel("Title" , fontsize = 12)
plt.grid(alpha = 0.3)
plt.tight_layout()

plt.subplot(2,2,2)
sns.barplot(data = category_story , x = 'subreddit' , y= 'count' , palette= 'Set1')
plt.title("Stories came from each category" , fontsize = 14 )
plt.xlabel("Category" , fontsize = 12)
plt.ylabel("Count" , fontsize = 12)
plt.grid(alpha = 0.3)
plt.tight_layout()

# 3 - Chart
plt.subplot(2,2,3)
sns.scatterplot(data =df, x = 'score' , y = 'num_comments' , hue='is_popular')
plt.title("Score vs Comments (Popularity Analysis", fontsize = 14 )
plt.xlabel("Score" , fontsize = 12)
plt.ylabel("Num_Comments" , fontsize = 12)
plt.grid(alpha = 0.3)
plt.tight_layout()

plt.savefig("outputs/dashboard.png")

plt.tight_layout()
plt.show()

print("Dashboard printed successfully")