Last login: Tue Jun 19 15:04:29 on ttys001
e1z2r10p10% vim 01_player.py
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
Traceback (most recent call last):
  File "01_player.py", line 3, in <module>
    print ("Welcome, {}".format(imput))
NameError: name 'imput' is not defined
e1z2r10p10% vim 01_player.py
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
Welcome, <built-in function input>
e1z2r10p10% vim 01_player.py
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
Traceback (most recent call last):
  File "01_player.py", line 3, in <module>
    print ("Welcome," + name + " ! ")
TypeError: cannot concatenate 'str' and 'builtin_function_or_method' objects
e1z2r10p10% vim 01_player.py   
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
 adffs
Traceback (most recent call last):
  File "01_player.py", line 2, in <module>
    name = input(" ")
  File "<string>", line 1, in <module>
NameError: name 'adffs' is not defined
e1z2r10p10% vim 01_player.py   
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
 chris
Welcome,chris ! 
e1z2r10p10% vim 01_player.py   
e1z2r10p10% python 01_player.py
Hello hacker, what is your name?
 Chris
Welcome,Chris! 
e1z2r10p10% vim 01_player.py   

print ("Hello hacker, what is your name?")
name = raw_input(" ")
print ("Welcome," + name + "! ")

~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
01_player.py                                                  3,28           All
"01_player.py" 4L, 99C
