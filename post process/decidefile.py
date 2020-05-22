probfile=open('prob.txt','r')
predicted=open('predicted_full.txt','r')
ans=open('predicted_v1.txt','w+')

pbr=probfile.readlines()
pdr=predicted.readlines()

for i in range(len(pbr)):
    pbrs=str(pbr[i]).split(',')
    pdrs=str(pdr[i]).split(',')
    for j in range(len(pbrs)):
        if (float(pbrs[j]) > 0.002):
            ans.write(str(pdrs[j])+',')
    ans.write('\n')