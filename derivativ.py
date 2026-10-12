import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return x**2 +3*x +5
def df(x):
	return 2*x + 3

x_val=float(input("x=? "))
y_val=f(x_val)
slope=df(x_val)


x_min= x_val - 5
x_max= x_val + 5
x=np.linspace(x_min, x_max, 400)

y=f(x)

tangent_x= np.linspace( x_val - 2, x_val + 2 , 100)
tangent_y=  slope*(tangent_x - x_val) +y_val

plt.figure(figsize=(8 , 6))
plt.plot(x, y, label= "f(x)=x²+3x+5", color='blue')
plt.plot(tangent_x, tangent_y, color='red', linestyle='-', linewidth=2, label=f"Türev (eğim = {slope}")
plt.scatter([x_val], [y_val], color='black', zorder=5)


plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.xlim(x_min,x_max)
plt.title(f"x = {x_val}  türevi")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()