import  pandas as pd
import numpy as np

header = pd.MultiIndex.from_tuples([("Beam","x"),("Beam","y"),
                                       ("Footing","u"),("Footing","v")])

ind =[np.array(["Moments","Moments","Shear Force","Shear Force"]),
      np.array(["Mx","My","SFx","SFy"])]

data =np.array([[9,4,8,5],[4,4,0,1],[5,7,4,5],[6,6,2,2]])

df = pd.DataFrame(data,columns=header,index=ind)
print(df)

# To slice a multi-index dataframe you can use loc or iloc. With loc, We can specify the sub-columns
#and the sub-rows using tuples:

print(df.loc[("Moments", "My"),("Beam", "x")])
