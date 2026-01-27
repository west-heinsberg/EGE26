import matplotlib.pyplot as plt
t = [0,1,2,3,4,5]
v = [2*i for i in t]
x = [i*i for i in t]

plt.plot(t, v)
plt.xlabel("Время (с)")
plt.ylabel("Скорость (м/с)")
plt.show()

plt.plot(t, x)
plt.xlabel("Время (с)")
plt.ylabel("Координата (м)")
plt.show()