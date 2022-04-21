import csv
with open('Data.csv','r') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)   
print("\nThe total number of training instances are :",len(data))

h=['0','0','0','0','0','0']

for row in data :
    if row[-1] == 'yes':
        j=0
        
        for col in row:
            if col != 'yes':
                if col != h[j] and h[j] == '0':
                    h[j] =  col
                elif col != h[j] and h[j] != '0':
                    h[j] = '?'
            j = j + 1
    print(h)
            
print('The Maximally specific hypothesis for the training instance is : ' , h)
