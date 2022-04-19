import pandas as pd
import glob

# identifying all response files
path = input("Path to folder that has response csvs: ")
filenames = glob.glob(path + "\*.csv")

# loads the data from response csv
big_df = pd.DataFrame()
col_names = ["Full Name (First Name & Surname)", "Student ID"]
for name in filenames:
	df = pd.read_csv(name, usecols=col_names)
	big_df = pd.concat([big_df, df], ignore_index=True)

# for checking if member has shown up in past activities or not
name_set = set()
name_id = []
def cond(data):
	name = data.get("Full Name (First Name & Surname)")
	conds = []

	conds.append(isinstance(name, str))
	conds.append(name not in name_set)
	return len(conds) != 0 and all(conds)

# making a list of all names
for _, data in big_df.iterrows():
	name = data.get("Full Name (First Name & Surname)")
	stuid = data.get("Student ID")

	if cond(data):
		name_set.add(name)
		name_id.append((name, int(stuid)))

# sort names and IDs
sorted_nid = sorted(name_id, key=lambda o: o[1])

# committee names to be skipped, check every term
cmts_names = []
with open("ssc_scripts\\resources\\committee_list.txt") as f:
	next(f)
	for line in f:
		cmts_names.append(line.strip())

# writing to a csv file
names = []
ids = []
for i, (name, sid) in enumerate(sorted_nid):
	if name not in cmts_names:
		names.append(name.strip())
		ids.append(sid)
df = pd.DataFrame({
	"names": names,
	"ids": ids
})
df.to_csv("out.csv", index=False)