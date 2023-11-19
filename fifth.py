## input概念 ##

## 想得知用戶名子 ##
name = input("請輸入你的名字:")
age = input("請輸入你的年紀:")
print("哈囉" + name + "你的年紀為" + age)

## 做出加減計算機 ##
num_1 = input("請輸入第一個數字")
num_2 = input("請輸入第二個數字")
## 錯誤過程 因為資料型態不一樣 ##
print(num_1 + num_2)

## 將字符轉換成 整數數字 ##
print(int(num_1)+int(num_2))

## 將字符轉換成含有小數的數 ##
print(float(num_1)+float(num_2))