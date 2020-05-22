import csv

predicted=open('predicted_full.txt','w+')
probfile=open('prob.txt','w+')


labels=open('labels.txt','r')
lr=labels.readlines()

with open('results.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        f=row['files']
        prob=row['probabilities']
        p=prob.split(', ')
        l1=[p[b[0]] for b in sorted(enumerate(p),reverse=True,key=lambda i:i[1])]
        l=[b[0] for b in sorted(enumerate(p),reverse=True,key=lambda i:i[1])]
        for i in range(5):
            #probfile.write(l1[i])
            predicted.write(str(lr[l[i]].strip('\n'))+',')
        predicted.write('\n')
        
        probfile.write(str(sorted(p[0:5],reverse=True)))
        probfile.write('\n')        