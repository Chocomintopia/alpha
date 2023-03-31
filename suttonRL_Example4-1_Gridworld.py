# 2023/3/31 sutton RL Example 4.1 Gridworld
# 动态规划 ch4.1 迭代策略评估

import numpy as np

# 状态空间： {1, 2, ..., 14} 左上角和右下角为终止状态
# 动作空间： {up, down, left, right} 上下左右移动
# 环境的动态特性： 四参数概率分布 p(s',r|s,a) 试图离开方格时状态不变，其余按照动作进行状态转移
# 折扣率： 本次任务无折扣 γ = 1
# 即时奖励： 到达终止状态之前 所有动作的收益均为-1

# 策略： 等概率随机策略 所有动作等可能执行
# 每步更新 化简后： v(i,j) <- 0.25 * ( v(i,j-1) + v(i,j+1) + v(i-1,j) + v(i+1,j) - 4)

# 问题： 迭代策略评估 求随机策略的状态价值函数的近似值 

# 参数
# 精度： theta 用于确定估计量的精度
theta = 0.01

# 初始化一个 m*n 的网格 初始价值函数全 0
# 本题目中为 4*4 的网格
m = 4
n = 4
value = np.zeros([m, n])

# 迭代次数
k = 0

while True:
    k += 1
    print('第',k,'次迭代：')
    delta = 0
    for i in range(m):
        for j in range(n):
            v = value[i,j]

            #更新
            # v(i,j) <- 0.25 * ( v(i,j-1) + v(i,j+1) + v(i-1,j) + v(i+1,j) - 4) （非边界情况）

            # 左上角 / 右下
            if (i==0 and j==0) or (i==m-1 and j==n-1):
                value[i,j] = 0
            # 左下角
            elif i==m-1 and j==0:
                value[i,j] = 0.25 * ( value[i,j] + value[i,j+1] + value[i-1,j] + value[i,j] - 4.0)
            # 右上角-
            elif i==0 and j==n-1:
                value[i,j] = 0.25 * ( value[i,j-1] + value[i,j] + value[i,j] + value[i+1,j] - 4.0)
            # 上侧边界
            elif i==0:
                value[i,j] = 0.25 * ( value[i,j-1] + value[i,j+1] + value[i,j] + value[i+1,j] - 4.0)
            # 左侧边界
            elif j==0:
                value[i,j] = 0.25 * ( value[i,j] + value[i,j+1] + value[i-1,j] + value[i+1,j] - 4.0)
            # 右侧边界
            elif j==n-1:
                value[i,j] = 0.25 * ( value[i,j-1] + value[i,j] + value[i-1,j] + value[i+1,j] - 4.0)
            # 下侧边界
            elif i==m-1:
                value[i,j] = 0.25 * ( value[i,j-1] + value[i,j+1] + value[i-1,j] + value[i,j] - 4.0)
            else:
                value[i,j] = 0.25 * ( value[i,j-1] + value[i,j+1] + value[i-1,j] + value[i+1,j] - 4.0)


            delta = max(delta, abs(v-value[i,j]))

    # 打印当前状态价值函数
    print(value)

    if delta < theta:
        break


# 结果：
# 第 62 次迭代：
# [[  0.         -13.934831   -19.90631084 -21.89687771]
#  [-13.934831   -17.92002909 -19.91316996 -19.91416281]
#  [-19.90631084 -19.91316996 -17.92673135 -13.94529672]
#  [-21.89687771 -19.91416281 -13.94529672   0.        ]]
