import hello_helpers.hello_misc as hm

node = hm.HelloNode.quick_create('my_test_node')

node.stow_the_robot()
node.move_to_pose({'joint_lift': 1.1, 'joint_arm' : 0.5}, blocking=True)



