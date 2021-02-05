import os

def wait_txt(line):
    with open('result.txt','a') as f:
        f.write(line)

res=[str(i) for i in range(1,1000)]

print(res)
# print(res[1])
# print(res[2])
# print(type(res[2]))
def handle_shanghai():
    with open("xx.txt",encoding='utf-8') as f:
        lines=f.readlines()
        flag_paiming=False
        flag_neirong=False
        flag=False
        for line in lines:
            # print(line)
            # print(type(line))
            line=line.strip()
            if line in res or line=='600+':
                #flag_paiming=True
                #flag_neirong=False
                # wait_txt('\n')
                flag=True
            # else:
            #     pass
            #     #flag_neirong=True
            #     #flag_paiming=False
            if flag:
                wait_txt('\n')
                wait_txt(line)
                wait_txt(" ")
                flag=False
            else:
                wait_txt(line)
                wait_txt(" ")

if __name__=="__main__":
    handle_shanghai()