import pandas as pd
import glob

path = "D:\\sciso-club\\documents\\trim-report"
filenames = glob.glob(path + "\*.csv")

big_df = pd.DataFrame()
col_names = ["Full Name (First Name & Surname)", "Student ID"]
for name in filenames:
	df = pd.read_csv(name, usecols=col_names)
	big_df = pd.concat([big_df, df], ignore_index=True)

name_set = set()
name_id = []
def cond(data):
	name = data.get("Full Name (First Name & Surname)")
	conds = []

	conds.append(isinstance(name, str))
	conds.append(name not in name_set)
	return len(conds) != 0 and all(conds)

# big_df.to_csv("tmp.csv", index=False)
for _, data in big_df.iterrows():
	name = data.get("Full Name (First Name & Surname)")
	stuid = data.get("Student ID")

	if cond(data):
		name_set.add(name)
		name_id.append((name, int(stuid)))

sorted_nid = sorted(name_id, key=lambda o: o[1])
names = [ o[0] for o in sorted_nid ]
ids = [ o[1] for o in sorted_nid ]
df = pd.DataFrame({
	"names": names,
	"ids": ids
})
df.to_csv("out.csv", index=False)