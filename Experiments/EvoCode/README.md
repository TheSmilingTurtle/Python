# Ok, so this is cool, here are notes for when i actually implement it
basically, make a tree structure of classes which encode the python syntax and can each return what python syntax they are equivalent to. 

so for example:

```py
x = 0
```

would be 

Gene([Op(Var(x), Lit(0))])

where Lit takes a specifc listeral as an argument for construction. Op takes two classes for construction (for simplicity do not perform checks, we dont care if we get 1 = 0 that will just die)

this way we can encode more complex ideas, like:

```py
def f(a, b):
    return a + b
```

we would have 

```py
Gene([
    Func(
        [Var(a), Var(b)], #argument list of Func
        Gene([]), #code to be executed within def, in this case empty
        Op(Var(a), Var(b)) #return 
    )
])
```

This defined a syntax tree. 

we can also define convenience classes, such as:

```py
for i in range(b):
    pass
```

we can have:

```py
Gene([
    For(
        Var(i), 
        Var(b), 
        Gene([Kw(pass)])
    )
])
```

each of these must also come with its own mutate method, such that it can be mutated. this may be recursive and call upon the mutations of its children