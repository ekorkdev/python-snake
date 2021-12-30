from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

  def __init__(self):
    
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for pos in STARTING_POSITIONS:
      self.add_segments(pos)

  def add_segments(self, pos):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.pu()
    new_segment.goto(pos)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segments(self.segments[-1].pos())

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      self.segments[seg_num].setpos(self.segments[seg_num - 1].pos())
    self.head.fd(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.seth(UP)  

  def down(self):
    if self.head.heading() != UP:
      self.head.seth(DOWN) 

  def right(self):
    if self.head.heading() != LEFT:
      self.head.seth(RIGHT)   

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.seth(LEFT)    