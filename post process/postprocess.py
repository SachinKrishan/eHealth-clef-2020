outfile=open('output_full.txt','w+')
ans=open('predicted_full.txt','r')
files=open('file_name.txt','r')

fr=files.readlines()
ar=ans.readlines()

for i in range(len(ar)):
    ars=ar[i].split(',')
    for j in range(len(ars)):
        outfile.write(str(fr[i].strip('\n'))+'\t'+str(ars[j]))
        outfile.write('\n')

