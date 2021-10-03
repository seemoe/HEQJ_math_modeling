# 依赖
import threading
import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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
	while len(people) > 0:
		if len(people)>(x**2):
			checknow=[people[x*i:(x+1)*i] for i in np.arange()]
			del people[0:x**2]
	# leng=len(people)
	# a,b=numful(leng) # b=a+1
	# lst=[]
	# k=-1
	# count=1
	# if sum(people)==0:
	# 	return 1
	# for i in range(a):
	# 	lst.append([])
	# 	for j in range(b):
	# 		k+=1
	# 		lst[i].append(people[k] if k<leng else 0)
	# tx=[]
	# ty=[]
	# for i in range(a):
	# 	count+=1
	# 	if sum(lst[i])>0:
	# 		tx.append(i)
	# for i in range(b):
	# 	count+=1
	# 	if sum([lst[z][i] for z in range(a)])>0:
	# 		ty.append(i)
	# if (len(tx) and len(ty))>1:
	# 	return count+len(tx)*len(ty)
	# else:
	# 	return count

# sorted_people = lambda n : [0 for i in range(n-1)]+[random.randint(0,1) for i in range(int(n*0.05))]
generate= lambda y,o : [0 for i in np.arange(int(y*o+0.5))]+[(1 if np.random.randint(0,101) <=80 else 0) for j in np.arange(int(y*o))]


def rand( lst ):
	leng=len(lst)
	for i in np.arange(leng):
		o=np.random.randint(0,leng)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

def start(x,y):
	# x 一组几人 y 总共几人
	ori=generate(y,0.05)
	people=rand(ori)
	return x,y,check(people,x)

#########################

begin=1000
end=1100

zlist=np.zeros([26,end-begin+1],np.int32)
xlist=np.arange(5,31)
ylist=np.arange(begin,end+1)

def get(x,y):
	return zlist[x-5][y-begin]

def main():
	# x 一组几人(-5) y 总共几人(-1000) content 检测次数
	global xlist
	global ylist
	global zlist
	for y in np.arange(begin,end+1):
		th_lst=[]
		for x in np.arange(5,31):
			th_lst.append(Thread(start,(x,y)))
			th_lst[-1].start()
		for i in np.arange(len(th_lst)):
			while th_lst[i].is_alive():
				time.sleep(0.1)
			th_lst[i].join()
			x,y,z=th_lst[i].get_result()
			zlist[x-5][y-begin]=z
	x,y = np.meshgrid(xlist, ylist)
	z=np.array( list([get(i,j) for i in xlist] for j in ylist) )
	print(z)
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.plot_surface(x,y,z,rstride = 1, cstride = 1,cmap='rainbow')
	ax.set_xlabel('group')
	ax.set_ylabel('total')
	ax.set_zlabel('count')
	plt.show()


# 运行

if __name__=="__main__":
	main()
	print("====================\nOperation completed!")