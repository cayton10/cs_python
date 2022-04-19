train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
c=3*10**8

#Turn up the Temperature:
# Fahrenheit to Celcius Conversion
def f_to_c(f_temp):
  return(f_temp - 32) * 5/9
  
print(f_to_c(100))

# Celcius to Fahrenheit Conversion
def c_to_f(c_temp):
  return(c_temp * 9/5) + 32

print(c_to_f(0))
c0_in_fahrenheit = (c_to_f(0))

#Use the Force
def get_force(mass, acceleration):
  return(mass * acceleration)
get_force(train_mass, train_acceleration)


train_force = 226800
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c):
  return mass * c**2

bomb_energy=get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")


#Do the Work
def get_work(mass, acceleration, distance):
  return get_force * train_distance

train_work = train_mass * train_acceleration * train_distance 
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")