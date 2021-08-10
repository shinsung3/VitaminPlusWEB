#pandas
import pandas as pd

# filename = "./TommyJeans_2021_Test_data.xlsx"
# book = openpyxl.load_workbook(filename)

# sheet = book.worksheets[0]

# print(sheet)

# df = pd.read_excel("./TomyJeans_2021_Test_data.xlsx")
# print(df)
index = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="A")
liveTime = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="B")
time = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="C")
memberDiff = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="D")
chat = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="E")
userCode = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="F")
userGroup = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="G")
userId = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="H")
userName = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="I")
userNick = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="J")
phone = pd.read_excel("./TomyJeans_2021_Test_data.xlsx", usecols="K")

