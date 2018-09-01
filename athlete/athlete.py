"""code goes here"""
class Athlete:

  def __init__(self, distance=0, time=0):
      #get time - seconds
	  self.__total_distance = distance
	  self.__total_time = time
	  self.__speed = 0
	  self.validate_time()

  @property
  def speed(self):
      return self.__speed

  @speed.setter
  def speed(self, value):
      self.__speed = value

  @property
  def total_distance(self):
      return self.__total_distance

  @total_distance.setter
  def total_distance(self, value):
      self.__total_distance = value

  @property
  def total_time(self):
      return self.__total_time

  @total_time.setter
  def total_time(self, value):
      self.__total_time = value

  #función para validar tiempo
  def validate_time(self):
      if self.total_distance == 0 and self.total_time > 0:
          raise Exception('Values are not valid') 
  
  #función para hacer ejercicio
  def new_workout(self, distance, time):
    self.total_distance += distance
    self.total_time += time

  #función para obtener velocidad del atleta
  def speed_record(self):
  	#meters/seconds
    if self.total_time == 0:
        self.__speed = 0
        return self.__speed
    else:
        self.__speed = round(self.total_distance / self.total_time, 2)
        return self.__speed

#Runner class
class Runner(Athlete):
  
  def __init__(self, distance=0, time=0, name=""):
      super().__init__(distance, time)
      self.__name = name
  
  #función run
  def run(self):
  	#return "Ran " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"
  	if self.__name != "":
  	    return "I'm {} and Ran {} meters, time: {} seconds, speed: {} m/s".format(self.__name, self.total_distance, self.total_time, self.speed_record())
  	else:
  		return "I'm a Runner and Ran {} meters, time: {} seconds, speed: {} m/s".format(self.total_distance, self.total_time, self.speed_record())


#Swimmer class
class Swimmer(Athlete):

  def __init__(self, distance=0, time=0, name=""):
      super().__init__(distance, time)
      self.__name = name
  
  #función swim
  def swim(self):
      #return "Swam " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"
      if self.__name != "":
          return "I'm {} and Swam {} meters, time: {} seconds, speed: {} m/s".format(self.__name, self.total_distance, self.total_time, self.speed_record())
      else:
  	  	  return "I'm a Swimmer and Swam {} meters, time: {} seconds, speed: {} m/s".format(self.total_distance, self.total_time, self.speed_record())

#Cyclist class
class Cyclist(Athlete):

  #función ride_bike
  def ride_bike(self):
      #return "Biking " + str(self.total_distance) + " meters, time: " + str(self.total_time) + " seconds, speed: " + str(self.speed_record()) + " m/s"
      #return 'Biking {} meters, time: {} seconds, speed: {} m/s'.format(self.total_distance, self.total_time, self.speed_record())
      if self.__name != "":
          return "I'm {} and Biking {} meters, time: {} seconds, speed: {} m/s".format(self.__name, self.total_distance, self.total_time, self.speed_record())
      else:
  	  	  return "I'm a Biker and Biking {} meters, time: {} seconds, speed: {} m/s".format(self.total_distance, self.total_time, self.speed_record())
