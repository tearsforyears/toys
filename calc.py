import numpy as np
import sys

def sympy_integrate():
	from sympy import integrate,Symbol
	x=Symbol("x")
	print(integrate(eval(input("function:")),x))

def sympy_derivative():
	from sympy import diff,Symbol
	x=Symbol("x")
	print(diff(input("function:")))
	
def integrate(f,a,b,n=1000000):
	return np.sum((b-a)/n*f(np.linspace(a,b,n)))

def derivative(f,x0,dx=1e-8):
	return (f(x0+dx)-f(x0))/dx

def main():
	if(len(sys.argv)<2):
		print("use python calc.py <parmeter>")
		print("parmeter:[integ] [sympy_integ] [diff] [sympy_diff]")
	elif sys.argv[1]=="integ":
		a = int(input("botton:"))
		b = int(input("top:"))
		print("integrate:",integrate(eval("lambda x:"+input("function:")),a,b))
	elif sys.argv[1]=="diff":
		x0 = int(input("point:"))
		print("derivative:",derivative(eval("lambda x:"+input("function:")),x0))
	elif sys.argv[1]=="sympy_integ":
		sympy_integrate()
	elif sys.argv[1]=="sympy_diff":
		sympy_derivative()
	else:
		print("parmeter wrong")
if __name__ == '__main__':
	main()