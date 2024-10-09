## NF601 - Advanced Programming in Python
## Josefina Baro
## Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)
##(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
##(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
##(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
##(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
##(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

#######Index(['Distance (ly)', 'Luminosity (L/Lo)', 'Radius (R/Ro)',
#######       'Temperature (K)', 'Spectral Class'],
#######      dtype='object')

stars = pd.read_csv('stardata.csv', index_col=0)

starData = {
        "Ross 154" : "SeaGreen" ,
        "Barnard's Star" : "LightSkyBlue" ,
        "Wolf 359" : "Maroon" ,
        "Lalande 21185" : "LightCoral"
        }

for starName, color in starData.items():
    star = stars.loc[starName]
    plt.scatter(star["Distance (ly)"], star["Radius (R/Ro)"], marker = "*", color = color, edgecolor = 'black' , label = starName, s= 100)

plt.title("Changing Radius of Stars Across Distances" , fontweight = 'bold')
plt.xlabel("Distance from Earth in Light-Years" , fontweight = 'bold')
plt.ylabel("Radius of Star Relative to Sun's Radius" , fontweight = 'bold')
plt.legend(fontsize ="small" , loc="upper right")
plt.savefig("charts/stardata.png")
plt.show()

starClassCounts = stars["Spectral Class"].value_counts()
plt.title("Number of Stars in Spectral Classes" , fontweight = 'bold')
plt.bar(starClassCounts.index, starClassCounts.values, color = 'CornflowerBlue' , edgecolor = 'black')
plt.xlabel('Class' , fontweight = 'bold')
plt.ylabel('Star Count', fontweight = 'bold')
plt.xticks(fontsize = 7 , rotation=90)
plt.grid(True, axis="y", linestyle = "--", alpha = 0.5)
plt.tight_layout()
plt.savefig("charts/starClassCounts.png")
plt.show()