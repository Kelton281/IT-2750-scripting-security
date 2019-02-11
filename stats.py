import statistics 
kglistmode = statistics.mode([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])
kglistmean = statistics.mean([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])
kglistmedian = statistics.median([34, 23, 54, 43, 53, 43, 99, 43, 74, 57, 82, 80, 17])

modealert = "this is your mode"
meanalert = "this is your mean"
medianalert = "this is your median"

print(modealert,kglistmode,meanalert,kglistmean,medianalert,kglistmedian)