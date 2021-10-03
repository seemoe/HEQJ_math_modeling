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
	b=1
	while i*b<n:
		if i<b:
			i+=1
		else:
			b+=1
	return i,b

# 使用二分检测
def check1( people ):
	count=1
	if sum(people) > 0 and len(people)>1:
		count+=check1(people[0:int(len(people)/2)])
		count+=check1(people[int(len(people)/2):len(people)])
	return count

# 使用点位检测(x,y)
def check2( people ):
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
new_people = lambda n : [(0 if random.randint(1,100) <= 15 else 1) for i in range(n)] # 0没得1得

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
	return check1(people),check2(people)

def main():
	## 主函数
	th_lst=[]
	st=1
	et=31
	clist=[0 for i in range(et-st)]
	c2list=[0 for i in range(et-st)]
	repeat=1000
	for t in range(repeat):
		for n in range(st,et):
			th_lst.append(Thread(start,(n,)))
			th_lst[-1].start()
		for i in range(len(th_lst)):
			while th_lst[i].is_alive():
				time.sleep(0.1)
			th_lst[i].join()
			count1,count2=th_lst[i].get_result()
			clist[i]+=count1
			c2list[i]+=count2
		th_lst.clear()
	result=[i/repeat for i in clist]
	result2=[i/repeat for i in c2list]
	# 虚线二分实线点位
	plt.plot([x for x in range(st,et)],result,'m--')
	plt.plot([x for x in range(st,et)],result2,'g-')
	plt.show()
	print(clist)


# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")