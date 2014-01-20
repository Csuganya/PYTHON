class student:
 name=" "
 mark=0
 def display(self):
  print("student name is{0}\n student mark is{1}".format(self.name,self.mark))
class sports(student):
 game="Athlet"
 rank=20
 def play(self):
  print("play the game",self.game)
  print("rank",self.rank)
s=sports()
s.display()
s.play()
