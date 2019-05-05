import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    hashed_password=dict()
    counter=0
    for password in range(0,10000):
        m=hashlib.sha256()
        x=str(password).encode()
        m.update(x)
        hashed=m.hexdigest()
        hashed_password[hashed]=password
    with open(input_file_name) as input_file:
        reader=csv.reader(input_file)
        for row in reader:
            counter+=1
    input_file.close()
    with open(input_file_name) as input_file:
        reader=csv.reader(input_file)
        output_file=open(output_file_name,'a+')
        count=0
        for row in reader:
            count+=1
            if(count==counter):
                output_file.write(row[0]+','+str(hashed_password[row[1]]))
            else:
                output_file.write(row[0]+','+str(hashed_password[row[1]])+'\n')
                
