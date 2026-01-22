import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()

robot.arm.move_to(0.5)
robot.lift.move_to(1.0)
robot.push_command()