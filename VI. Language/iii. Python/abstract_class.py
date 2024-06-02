# Abstract Class
# Date: 2024-06-02-Sun.
# Reference: https://wikidocs.net/16075
# Reference: https://dojang.io/mod/page/view.php?id=2389
# Reference: https://otzslayer.github.io/python/2021/11/02/abstact-class-in-python.html

from abc import *

class GrandFather(metaclass=ABCMeta):
  def __init__(self, first_name):
    self.first_name = first_name
    self.last_name = 'H'

  @abstractmethod
  def hello(self):
    print('Hello')
    pass

class Father(GrandFather):
  def __init__(self, first_name):
    super().__init__(first_name)
    
  def hello(self):
    super().hello()
    print(f'My name is {self.first_name} {self.last_name}')

def main():
  father = Father(
    first_name='b',
  )

if __name__ == '__main__':
  main()
  
