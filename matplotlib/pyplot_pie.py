#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt

def main():
   slice = [7,2,2,13]
   activitis = ["sleeping","working","eating","playing"]
   color = ["m","k","c","r"]

   plt.pie(slice,labels=activitis,colors=color,startangle=90,shadow=True,autopct="%1.1f%%")
   plt.legend()
   plt.title("matplotlib pie")
   plt.show()



if __name__ == "__main__":
    main()
