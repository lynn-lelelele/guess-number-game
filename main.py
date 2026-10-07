"""
正常流程可以顺利走完。
- 空输入、错误输入不会让程序崩溃。
- 菜单选项输入错误后可以重新输入。
- 连续运行两三次，不会出现明显状态混乱。
- 函数名和变量名能看懂。
- 没有大量重复代码。
- README 写清楚：功能、运行方式、已实现内容、待改进内容。
- 自己记录至少 5 个测试案例和测试结果。

"""
# 功能需求

# 1. 程序开始时，随机生成一个 1～100 的整数。
# 2. 玩家最多可以猜 7 次。
# 3. 每次猜完后提示：
#    - 猜小了
#    - 猜大了
#    - 猜对了
# 4. 如果玩家输入的不是整数：
#    - 提示“请输入整数”
#    - 这次输入不计入猜测次数
# 5. 如果 7 次都没有猜中：
#    - 公布正确答案
#    - 询问是否再来一局
# 6. 猜中后：
#    - 显示本次猜了多少次
#    - 询问是否再来一局
# 7. 再来一局只接受：
#    - `y` 或 `Y`：开始新一局
#    - `n` 或 `N`：退出程序
#    - 其他输入：重新询问
# 8. 退出时输出一句结束语。


import random 




while True:
    attempt = 0
    won = False #用来标记成功
    n = random.randint(1,100)
    while attempt < 7:
        try:
            answer = int(input("请输入你猜的数字....."))
        except ValueError:
            print("请输入整数")
            continue

        attempt += 1

        if answer == n:
            print("猜对了")
            print(f"您一共输入{attempt}次")
            won = True
            break
           
        elif answer < n:
            print("猜小了")
            
            
        else:
            print("猜大了")
            



    if not won:
        print(f"正确答案是{n}")
    while True:
        answer2 = input("请问是否要再来一次.....(回答y/n或者Y/N)")

        if answer2 in ("y", "Y", "n", "N"):
            break

        print("请输入 y 或 n")

    if answer2 in ("n", "N"):
        print("游戏结束拉")
        break

#新知识点

#try:
#    做一件可能失败的事
#except 某种失败:
#    失败后的补救办法