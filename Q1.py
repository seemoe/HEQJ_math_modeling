# 依赖
import threading
import random

# 函数

# get_ltr= lambda o : chr(o+97) # 0 is 'a'

def check( people ):
	pass

sorted_people = lambda n : [0 for i in range(n-1)]+[1 for i in range(int(n*0.05))]

def rand( lst ):
	leng=len(lst)
	for i in range(leng):
		o=random.randint(0,leng-1)
		lst[i],lst[o]=lst[o],lst[i]
	return lst

def main():
	## 主函数
	for n in range(20,31):
		stp=sorted_people(n)
		people=rand(stp)
		check(people)

# 运行

if __name__=="__main__":
	main()