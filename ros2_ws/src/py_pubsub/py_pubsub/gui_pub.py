from tkinter import *
from turtle import color
from publisher_member_function import *
import rclpy

def on_click(publisher):
    publisher.publish()

def main(args=None):
    rclpy.init()

    pub = MinimalPublisher()

    root = Tk()
    button = Button(root, bg="red", command=lambda: on_click(pub), padx= 50, pady= 50)
    button.pack()
    label = Label(root, text="Publish My Message", padx= 50, pady= 50)
    label.pack()

    root.mainloop()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
