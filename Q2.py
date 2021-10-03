# 依赖
import threading
import time
import matplotlib.pyplot as plt
import numpy as np

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

# 使用点位检测(x,y)
def check( people , x ):
	ccount=0
	bcount=0
	while len(people) > 0:
		if len(people)>(x**2):
			checknow=[people[x*i:(x+1)*i] for i in np.arange(x)]
			del people[0:x**2]
		else:
			a,b=numful(len(people))
			checknow=[people[a*i:((a+1)*i if (a+1*i) <= len(people) else 0)] for i in np.arange(b)]
			del people[0:len(people)]
		xleng=len(checknow[0])
		yleng=len(checknow)
		tx=[]
		ty=[]
		for i in np.arange(yleng):
			ccount+=1
			bcount+=len(checknow[i])
			if sum(checknow[i]) > 0:
				ty.append(i)
		for i in np.arange(xleng):
			ccount+=1
			lst=[checknow[j][i] for j in np.arange(yleng)]
			bcount+=len(lst)
			if sum(lst) > 0:
				tx.append(i)
		if len(tx)>=2 and len(ty)>=2:
			ccount+=(len(tx)*len(ty))
			bcount+=(len(tx)*len(ty))
	return bcount,ccount

# sorted_people = lambda n : [0 for i in range(n-1)]+[random.randint(0,1) for i in range(int(n*0.05))]
generate= lambda y,o : [0 for i in np.arange(int(y*o+0.5))]+[(1 if np.random.randint(0,101) <=80 else 0) for j in np.arange(int(y*o))]


def rand( lst ):
	leng=len(lst)
	for i in np.arange(leng):
		o=np.random.randint(0,leng)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

peon=50000

def start(x):
	# x 一组几人 peon 总共几人
	bcount=0
	ccount=0
	for i in np.arange(3):
		ori=generate(peon,0.05)
		people=rand(ori)
		rs=check(people,x)
		bcount+=rs[0]
		ccount+=rs[1]
	return (x,bcount/3,ccount/3)

#########################

def main():
	# x 一组几人(-5) bcount 抽血次数 ccount 检测次数
	bcount={}
	ccount={}	
	th_lst=[]
	for x in np.arange(5,31):
		th_lst.append(Thread(start,(x,)))
		th_lst[-1].start()
	for i in np.arange(len(th_lst)):
		while th_lst[i].is_alive():
			time.sleep(0.1)
		th_lst[i].join()
		x,btimes,ctimes=th_lst[i].get_result()
		bcount[x],ccount[x]=btimes,ctimes
	labels = sorted(bcount.keys())
	plt.rcParams['font.sans-serif']=['Microsoft YaHei']
	fig,ax = plt.subplots()
	blist=[bcount[x] for x in labels]
	clist=[ccount[x] for x in labels]
	ax.bar(labels,blist,label="采样次数")
	ax.bar(labels,clist,label="检测次数",bottom=blist)
	ax.set_ylabel('次数（下采样上检测）')
	ax.set_xlabel('组人数')
	# 头
	ax.set_title('总人数为50000时抽血与检测次数和每组人数的关系柱状图')
	plt.show()


# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")