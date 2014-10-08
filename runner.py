import tfidf

table = tfidf.tfidf()
f = open("sampleFile.txt", 'r')
terms = f.read().split(" ")
print(terms)
firstDocName = "testDocument"
secondDoc = ["test", "this"]

table.addDocument(firstDocName, terms)
table.addDocument("secondName", secondDoc)

result = table.similarities(["this"])
print(result)
