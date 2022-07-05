from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

data = pd.read_csv('carActu1.csv')

def decision(precio, mantenimiento, puertas, personas, cajuela, seguridad):
   x = data.iloc[:, 0:6].values
   y = data.iloc[:, 6].values
   classif = DecisionTreeClassifier()
   classif = classif.fit(x, y)
   num = []
    
   
   num.append([precio, mantenimiento, puertas, personas, cajuela, seguridad])
   pred = np.array(num).reshape((1, -1))
   predict = classif.predict(pred)

   return predict

