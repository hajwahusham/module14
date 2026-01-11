# importing necessary libraries
import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np
dataset = pd.read_csv("visual.csv")

# profit graph
def month_profit():
    plt.plot(dataset["month_number"], dataset["total_profit"], marker='o', 
             linestyle='-', color='pink', ms= 10, mec='r', linewidth='3')
    plt.title("profit per month graph")
    plt.xlabel("month")
    plt.ylabel("profit")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# product sales
def product_sales():
    plt.plot(dataset["month_number"], dataset["bathingsoap"], marker='*', 
             linestyle='-', color='tab:cyan', ms= 10, mec='c', linewidth='1', label='bathing soap')

    plt.plot(dataset["month_number"], dataset["facewash"], marker='^', 
             linestyle='-', color='tab:red', ms= 10, mec='r', linewidth='1', label='facewash')

    plt.plot(dataset["month_number"], dataset["toothpaste"], marker='x', 
             linestyle='-', color='tab:purple', ms= 10, mec='purple', linewidth='1', label='toothpaste')
    
    plt.plot(dataset["month_number"], dataset["facecream"], marker='h', 
             linestyle='-', color='tab:blue', ms= 10, mec='blue', linewidth='1', label='face cream')
    
    plt.plot(dataset["month_number"], dataset["shampoo"], marker='p', 
             linestyle='-', color='tab:olive', ms= 10, mec='olive', linewidth='1', label='shampoo')
    
    plt.plot(dataset["month_number"], dataset["moisturizer"], marker='d', 
             linestyle='-', color='tab:pink', ms= 10, mec='m', linewidth='1', label='moisturiser')




    plt.title("product sales")
    plt.xlabel("month")
    plt.ylabel("sales")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def comparision():
    x = np.arange(len(dataset["month_number"]))

    width = 0.35

    plt.bar(x - width/2, dataset["facewash"], width=width, label="facewash", color="darkblue")
    plt.bar(x + width/2, dataset["facecream"], width=width, label="facecream", color="lightblue")

    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.title("Product Sales per Month")
    plt.legend()
    plt.xticks(x, dataset["month_number"])
    plt.tight_layout()
    plt.show()


# month_profit()
# product_sales()
comparision()