'''
密码生成器由 N 个槽位组成，槽位的下标为 0~N-1 ，每个槽位存储一个数。起初每个槽位都是 0 。
密码生成器会进行 M 轮计算，每轮计算，小汪会输入两个数 L , R (L<=R),密码生成器会将这两个数作为下标，将两个下标之间（包含）的所有槽位赋值为 i（ i 为当前的轮次， i ∈ [1,M]）。
M轮计算完成后，密码生成器会根据槽位的最终值生成一条密码，密码的生成规则为：
（0*a[0] + 1*a[1] + 2*a[2] + ... + (N-1)*a[N-1]) mod 100000009
'''