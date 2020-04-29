from sklearn import svm

clf = svm.SVC()
clf.fit([
    [0,0],
    [1,0],
    [0,1],
    [1,1]
],[0,1,1,0])
results = clf.predict([
    [0,0], #0
    [1,0], #1
    [0,1],
    [1,1]
]) #[0, 1]
print(results)
