## NF601 - Advanced Programming in Python
## Josefina Baro
## Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

##(5/5 points) Initial comments with your name, class and project at the top of your .py file.
##(5/5 points) Proper import of packages used.
##(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
##Think of some question you would like to solve such as:
##"How many homes in the US have access to 100Mbps Internet or more?"
##"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
##Here are some other great datasets: https://www.kaggle.com/datasets
##(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
##(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
##(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
##(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
##(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
##(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

#######Index(['Distance (ly)', 'Luminosity (L/Lo)', 'Radius (R/Ro)',
#######       'Temperature (K)', 'Spectral Class'],
#######      dtype='object')

stars = pd.read_csv('stardata.csv', index_col=0)

starData = {

        "Ross 154" : "gold" ,
        "Barnard's Star" : "crimson" ,
        "Wolf 359" : "magenta" ,
        "Lalande 21185" : "purple"
        }

for starName, color in starData.items():
    star = stars.loc[starName]
    plt.scatter(star["Distance (ly)"], star["Radius (R/Ro)"], marker = "*", color = color, label = starName)

plt.title("Changing Radius of Stars Across Distances")
plt.xlabel("Distance from Earth in Light-Years")
plt.ylabel("Radius of Star Relative to Sun's Radius")
plt.legend(fontsize ="small" , loc="upper right")
plt.show()

starClassCounts = stars["Spectral Class"].value_counts()

plt.title("Amount of Stars in Star Classes")
plt.bar(starClassCounts.index, starClassCounts.values)
plt.xlabel('Spectral Class')
plt.ylabel('Count')
plt.xticks(fontsize = 6 , rotation=90)
plt.grid(True, axis="y", linestyle = "--", alpha = 0.5)
plt.show()