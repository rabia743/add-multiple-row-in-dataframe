import pandas as pd
file = {"Name":["Ali","Raza"],
        "Age":[20,29]
        }
d = pd.DataFrame(file)
print(d)
# add new multiple rows method no 1
d.loc[len(d)] = ["Fraz", 20]
d.loc[len(d)] = ["Sana", 35]
print(d)

# add new multiple rows method no 2 using the concat concept
import pandas as pd
data = pd.DataFrame({"Name":["Ali","Raza"],
        "Age":[20,29]
        })
new_row = pd.DataFrame({"Name":["Waseem","Zainab"],
        "Age":[30,25]
        })
data = pd.concat([data, new_row], ignore_index=True)
print(data