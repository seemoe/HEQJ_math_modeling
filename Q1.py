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

def check( people ):
	count=1
	if sum(people) > 0:
		count += len(people)
	return count

sorted_people = lambda n : [0 for i in range(n-1)]+[random.randint(0,1) for i in range(int(n*0.05))]

def rand( lst ):
	leng=len(lst)
	for i in range(leng):
		o=random.randint(0,leng-1)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

def start(n):
	stp=sorted_people(n)
	people=rand(stp)
	return check(people)

def main():
	## 主函数
	th_lst=[]
	st=1
	et=31
	clist=[0 for i in range(et-st)]
	repeat=1000
	for t in range(repeat):
		for n in range(st,et):
			th_lst.append(Thread(start,(n,)))
			th_lst[-1].start()
		for i in range(len(th_lst)):
			while th_lst[i].is_alive():
				time.sleep(0.1)
			th_lst[i].join()
			count=th_lst[i].get_result()
			clist[i]+=count
		th_lst.clear()
	result=[i/repeat for i in clist]
	plt.plot([x for x in range(st,et)],result,'m--')
	plt.show()
	print(clist)


# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")