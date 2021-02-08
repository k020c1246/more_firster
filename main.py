import random
import time

#探索対象の数字
key=-1
#探索するリスト
listnum=[]

def l_search(a,key):
  #結果を入れる　先頭だったら0
  index=-1
  #ループの回数
  i=0
  while True:
    if a[i]==key:
      index=i
      break

    if i==len(a)-1:
      break

    i=i+1

  return index

def b_search(a,key):
    pl=0
    pr=len(a)-1

    while True:
      pc=(pl+pr)//2
      if a[pc]==key:
        return pc
      elif a[pc]<key:
        pl=pc+1
      else:
        pr=pc-1
      if pl>pr:
        break

    return -1

#リスト要素数とループ回数
size=10000
loop=100
#リスト生成
for i in range(1,size):
  listnum.append(i)
#key の値をランダム生成
key=random.randint(1,size)

print(key)
print(l_search(listnum,key))
print(b_search(listnum,key))

#線形探索実行
start=time.time()
for i in range(1,loop):
  key=random.randint(1,size)
  l_search(listnum,key)
elapsed_time=time.time()-start
print("time:{0}".format(elapsed_time)+"[sec]")

#2分探索実行
start=time.time()
for i in range(1,loop):
  key=random.randint(1,size)
  b_search(listnum,key)
elapsed_time=time.time()-start
print("time:{0}".format(elapsed_time)+"[sec]")

                 
