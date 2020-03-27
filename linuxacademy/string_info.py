#!/usr/bin/env python3.7
msg=input("Enter a message:")
print("First character:"+ msg[0])
print("Last character:", msg[len(msg)-1])
print("Last character:", msg[-1])
print("Middle charater:" ,msg[int(len(msg)/2)])
print("Even index characters:", msg[0:len(msg):2])
print("Odd index characters:", msg[1:len(msg):2])
print("Reverse index characters:", msg[::-1])

