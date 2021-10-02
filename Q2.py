# 依赖
import threading
import random
import time
import matplotlib.pyplot as plt

# 多线程重写

class Thread(threading.Thread):
    def __init__(self, func, args=()):
        super(Thread,self).__init__()
        self.func= func
        self.args= args
 
    def run(self):
        self.result= self.func(*self.args)
 
    def get_result(self):
        try:
            return self.result
        except Exception:
            return Exception

# 函数

# get_ltr= lambda o : chr(o+97) # 0 is 'a'

def numful(n):
	i=1
	while i*(i+1)<n:
		i+=1
	return i,i+1

# 使用点位检测(x,y)
def check( people ):
	leng=len(people)
	a,b=numful(leng) # b=a+1
	lst=[]
	k=-1
	count=1
	if sum(people)==0:
		return 1
	for i in range(a):
		lst.append([])
		for j in range(b):
			k+=1
			lst[i].append(people[k] if k<leng else 0)
	tx=[]
	ty=[]
	for i in range(a):
		count+=1
		if sum(lst[i])>0:
			tx.append(i)
	for i in range(b):
		count+=1
		if sum([lst[z][i] for z in range(a)])>0:
			ty.append(i)
	if (len(tx) and len(ty))>1:
		return count+len(tx)*len(ty)
	else:
		return count

# sorted_people = lambda n : [0 for i in range(n-1)]+[random.randint(0,1) for i in range(int(n*0.05))]
new_people = lambda n : [(0 if random.randint(1,100) <= 5 else 1) for i in range(n)] # 0没得1得

def rand( lst ):
	leng=len(lst)
	for i in range(leng):
		o=random.randint(0,leng-1)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

def start(n):
	# stp=sorted_people(n)
	ntp=new_people(n)
	# people=rand(stp)
	people=rand(ntp)
	return check(people),n

def main():
	loop=100000
	th_num=1000
	result={}
	for times in range(0,loop,th_num):
		th_lst=[]
		for i in range(th_num):
			num=random.randint(1000,10000)
			th_lst.append(Thread(start,(num,)))
			th_lst[-1].start()
		for i in range(th_num):
			while th_lst[i].is_alive():
				time.sleep(0.1)
			th_lst[i].join()
			count,num=th_lst[i].get_result()
			if num in result.keys:
				result[num][0]+=count
				result[num][1]+=1
			else:
				result[num]=[count,1]
	xlist=result.keys
	ylist=[x/y for x,y in [result[i] for i in range(len(xlist))]]
	plt.plot(xlist,ylist,'g-')
	plt.show()

# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")