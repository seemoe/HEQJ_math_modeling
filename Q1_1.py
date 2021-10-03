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

def check( people ):
	count=1
	if sum(people) > 0:
		count+=len(people)
	return count

# sorted_people = lambda n : [0 for i in range(n-1)]+[random.randint(0,1) for i in range(int(n*0.05))]
new_people = lambda n : [(0 if np.random.randint(1,10) <= 15 else 1) for i in range(n)] # 0没得1得

def rand( lst ):
	leng=len(lst)
	for i in np.arange(leng):
		o=np.random.randint(0,leng)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

def start(x,y):
	# stp=sorted_people(n)
	ntp=new_people(n)
	# people=rand(stp)
	people=rand(ntp)
	return x,y,check(people)

def main():
	# x 一组几人(-5) y 总共几人(-1000) content 检测次数
	zlist=np.zeros([26,99001],np.int32)
	xlist=np.arange(1,31)
	ylist=np.arange(1000,100001)
	for y in np.arange(1000,100001,26):
		th_lst=[]
		for x in np.arange(5,31):
			th_lst.append(Thread(start,(x,y)))
			th_lst[-1].start()
		for i in np.arange(len(th_lst)):
			while th_lst[i].is_alive():
				time.sleep(0.1)
			th_lst[i].join()
			x,y,z=th_lst[i].get_result()
			zlist[x-5][y-1000]=z


# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")