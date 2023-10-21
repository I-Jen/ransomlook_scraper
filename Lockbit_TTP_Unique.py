lockbit = ["T1078", "T1133", "T1189", "T1190", "T1566", "TA0002", "T1072", "T1078", "T1547", "TA0004", "T1547", "T1027", "T1070.004", "T1480.001", "T1003.001", "T1046", "T1082", "T1614.001", "T1021.001", "T1071.002", "T1572", "TA0010", "T1567", "T1567.002", "T1485", "T1486", "T1489", "T1490", "T1491.001"]

alphv = ["T1566", "T1586", "T1111", "T1098.005", "T1484.002", "T1053.005", "T1219", "T1525", "T1078", "T1135", "T1046", "T1072", "T1021.001", "T1071.001", "T1219", "T1048", "T1486", "T1491.001", "T1490"]

snatch = ["T1590", "T1583.003", "T1133", "T1078", "T1059.003", "T1569.002", "T1133", "T1078.002", "T1583.003", "T1036", "T1070.004", "T1112", "T1562.001", "T1562.009", "T1110.001", "T1012", "T1057", "T1021.001", "T1005", "T1071.001", "T1041", "T1486", "T1490"]

playnews = ["T1078", "T1021.001", "T1059", "T1203", "T1021.001", "T1562", "T1140", "T1070", "T1003", "T1552", "T1033", "T1082", "T1083", "T1135", "T1057", "T1007", "T1021", "T1071", "T1002", "T1048", "T1486", "T1489", "T1490"]

eightbase = ["T1595", "T1598", "T1583", "T1587", "T1566.001", "T1053", "T1059", "T1129", "T1053", "T1547.001", "T1053", "T1547.001", "T1036", "T1070.004", "T1112", "T1202", "T1222", "T1497", "T1562", "T1562.001", "T1562.004", "T1564", "T1564.001", "T1003", "T1056", "T1057", "T1082", "T1083", "T1497", "T1518.001", "T1080", "T1005", "T1056", "T1074", "T1560", "T1071.001", "T1041", "T1485", "T1490"]

# Convert lists to sets
lockbit_set = set(lockbit)
alphv_set = set(alphv)
snatch_set = set(snatch)
playnews_set = set(playnews)
eightbase_set = set(eightbase)

print(len(lockbit))
print(len(alphv))
print(len(snatch))
print(len(playnews))
print(len(eightbase))

print("\n")

print(len(lockbit_set))
print(len(alphv_set))
print(len(snatch_set))
print(len(playnews_set))
print(len(eightbase_set))

# Find elements unique to lockbit set
unique_to_lockbit = lockbit_set.difference(alphv_set, snatch_set, playnews_set, eightbase_set)

# Convert the result back to a list
unique_to_lockbit_list = list(unique_to_lockbit)

# Print the unique elements
print(unique_to_lockbit_list)