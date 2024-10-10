## NF601 - Advanced Programming in Python
## Josefina Baro Franco
## Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)
##(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
##(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.

#######Index(['Distance (ly)', 'Luminosity (L/Lo)', 'Radius (R/Ro)',
#######       'Temperature (K)', 'Spectral Class'],
#######      dtype='object')

stars = pd.read_csv('stardata.csv', index_col=0)
#chose 4 stars to show data for and assigned a color to each
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
plt.bar(starClassCounts.index, starClassCounts.values, color = 'Plum' , edgecolor = 'black')
plt.xlabel('Class' , fontweight = 'bold')
plt.ylabel('Star Count', fontweight = 'bold')
plt.xticks(fontsize = 7 , rotation=90)
plt.grid(True, axis="y",color = 'black', linestyle = "--", alpha = .5)
plt.tight_layout()
plt.savefig("charts/starClassCounts.png")
plt.show()

plt.hist2d(stars["Distance (ly)"], stars["Temperature (K)"], bins=50, cmap= "plasma")
plt.title("Distribution of Star Temps Across Varying Distances from Earth" , fontweight = 'bold')
plt.xlim(0,700)
plt.xlabel("Distance from Earth in Light-Years" , fontweight = 'bold')
plt.ylim(2750,14000)
plt.ylabel("Temperature (K)" , fontweight = 'bold')
plt.colorbar(label= "Number of Stars")
plt.tight_layout()
plt.show()