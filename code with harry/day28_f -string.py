letter="hello my name is {1} and i am from {0}"
country="nepal"
name="nischal"
print(letter.format(country,name))
print(f"hello my name is {name} and i am from {country}")
print(f"we use f-string like this : the name is {{name}} and i am from {{country}}")
price=49.099999
text=f"this is the price {price:.2f} doller"
print(text)
print(f"{2*33}")
#f-string works as string as well as integer type float