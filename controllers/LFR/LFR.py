from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
time_step = 32
max_speed = 6.28

#motor
left_motor = robot.getMotor("left wheel motor")
right_motor = robot.getMotor("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

#ir Sensor
right_ir = robot.getDevice('RIGHT')
right_ir.enable(time_step)
left_ir = robot.getDevice('LEFT')
left_ir.enable(time_step)
mid_ir = robot.getDevice('MID')
mid_ir.enable(time_step)

while robot.step(timestep) != -1:
    
    right_ir_val = right_ir.getValue()
    left_ir_val = left_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    
    print("left: {} mid: {} right: {}".format(left_ir_val,mid_ir_val,right_ir_val))
    right_speed= max_speed
    left_speed = max_speed
    if left_ir_val<620 and right_ir_val<620 and mid_ir_val>=620:
         right_motor.setVelocity(-right_speed)
         left_motor.setVelocity(-left_speed)
    if left_ir_val<620 and right_ir_val>=620 and mid_ir_val>=620:
         right_motor.setVelocity(0)
         left_motor.setVelocity(-left_speed)   
    if left_ir_val>=620 and right_ir_val<620 and mid_ir_val>=620:
        right_motor.setVelocity(-right_speed)
        left_motor.setVelocity(0)    
    if left_ir_val>=620 and right_ir_val<620 and mid_ir_val>=620:
        right_motor.setVelocity(-right_speed)
        left_motor.setVelocity(0) 
    if left_ir_val<620 and right_ir_val>=620 and mid_ir_val>=620:
        right_motor.setVelocity(0)
        left_motor.setVelocity(-left_speed)    
    if left_ir_val<620 and right_ir_val<620 and mid_ir_val<620:
         right_motor.setVelocity(-right_speed)
         left_motor.setVelocity(-left_speed)
         
    pass
