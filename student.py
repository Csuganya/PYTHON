class student:
 name=" "
 mark=0
 def __init__(self,name,mark):
  self.name=name
  self.mark=mark
  print("constructor called")
 def display(self):
  print("Student name is {0}\n student mark is {1}".format(self.name,self.mark))
  #print("student name %s\n student mark %d",self.name,self.mark)
#s1.name="sam"
#s1.mark=40
#stu=student("sam",80)
#stu.display()
class sports(student):
 game="Athlet"
 rank=20
 def play(self):
  print("play the game",self.game)
  print("rank",self.rank)
s=sports()
s.display()
s.play()
