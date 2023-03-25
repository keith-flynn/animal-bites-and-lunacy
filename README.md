# Animal Bites and Lunacy
![moon-phases](./assets/moon_phases.jpg)
A comparison of animal bite data in Louisville, KY from 2010-2017 with phases of the moon.

---
## Project Overview:
---
- Imports data from CSV files to a SQL database
- Queries SQL database for relevant data
- Cleans data and merges into a Pandas dataframe
- Includes [Tableau dashboard for visualizations](https://public.tableau.com/app/profile/keith.flynn3286/viz/AnimalBitesandLunacy/dashboard_animal_bites_and_lunacy?publish=yes)
---
### Code and Resources Used:
- Python 3.10
- Pandas
- Jupyter Notebook
### To Run the Project:
1. Set up a virtual environment and activate it:
`python -m venv venv`
Windows:
` venv/Scripts/activate`
Mac/Linux:
`source venv/bin/activate`
2. Install requirements.txt
`python3 -m pip install requirements.txt`
3. Run lunacy.ipynb in Jupyter Notebook
---
## Summary
---
The goal of this project is to discover if there is any correlation between animal bites reported in Louisville, KY between October 29th 2009 and September 8th 2017, and the phase of the moon when the bite occurred. The bite dataset contains reports from many other years, but the reporting is inconsistent and missing most of the applicable data points.

---
## Visualizations
---
Tableau Dashboard: [Animal Bites and Lunacy](https://public.tableau.com/app/profile/keith.flynn3286/viz/AnimalBitesandLunacy/dashboard_animal_bites_and_lunacy?publish=yes)

---
## Sources
---
- [Animal Bites](https://www.kaggle.com/datasets/rtatman/animal-bites)
- [Daily Moon Illumination 1800 to 2100](https://www.kaggle.com/datasets/petermenzies/daily-moon-illumination-1800-to-2100)
---
## License
[GNU GENERAL PUBLIC LICENSE](LICENSE)