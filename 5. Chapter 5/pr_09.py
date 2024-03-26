#We Cannot Store List inside A Set as they are not Hashable

# s = {8,7,12,"Harry",[1,2]} # Will not Throw an error because tuple or dictionary can be stored inside a set, But we cannot change the value inside tuple(generally).
# s = {8,7,12,"Harry",[1,2]} # --> Throws an error
s = {8,7,12,"Harry",(1,2)}
print(s)
