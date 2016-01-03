#!/usr/bin/python
class Parent(object):
  def __init__(self):
    self.value = 5
  def get_name(self,name):
    return name
  def get_value(self):
    return self.value

class Child(Parent):
  def get_value(self):
    return self.value + 1
  def get_name(self,name):
    return name


#c = Child()
#print c.get_value()


if __name__ == "__main__":
  p = Parent()
  print p.get_name(Parent)
  print p.get_value()
  c = Child()
  print c.get_name(Child)
  print c.get_value()
  
