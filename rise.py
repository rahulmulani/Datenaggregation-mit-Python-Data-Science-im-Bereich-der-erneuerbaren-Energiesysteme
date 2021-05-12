import matplotlib.pyplot as plt
import pandas as pd
import os

# empty arrays for saving values
Green = []
Red = []
Orange= []

fig, ax= plt.subplots(figsize=(16, 8), subplot_kw=dict(aspect='equal'))
#path
fileDir = os.path.split(os.getcwd())[0]
fileName = "rahul\.spyder-py3\project\Excel_data.xlsx"
abs_file_path = os.path.join(fileDir, fileName)
data = pd.read_excel(abs_file_path, sheet_name="Sheet3")

#function to filter data accordingly
def RenewableEnergyScore():
    for value in data.RenewableEnergyScore:
        if value >=67  and value <= 100:
            Green.append(float(value))
        elif value >=34  and value <= 66:
            Orange.append(float(value))
        else: 
            Red.append(float(value))
    return len(Green), len(Orange), len(Red)    

################ plot ##########
explode = (0.1, 0.1 ,0.1)
#colors of the pies
pieColors = ("green","orange","red")
#chart specification
##labels of the pies
pieLabels = 'Higher(67-100)','Medium (34-66)','Lower (0-33)'

ax.pie(RenewableEnergyScore(),
        explode = explode,
        colors=pieColors,
        shadow = True,
        autopct='%1.1f%%',
        startangle=90,
        radius=1,
        textprops={'fontsize': 18},
        wedgeprops = { 'linewidth': 3, "edgecolor" :"w" })

legend=ax.legend(pieLabels,
          title="Range of Renewable Energy Score",fontsize =15,
          bbox_to_anchor=(1,1.025), loc="best", markerscale = 2, borderaxespad = 0.5, prop ={"size": 15}, fancybox = True)

plt.setp(legend.get_title(),fontsize='15')
ax.set_title('Renewable Energy Score',fontsize=24)
plt.savefig(fileDir +'/rahul/.spyder-py3/project/RES.png', dpi = 128)
plt.show()