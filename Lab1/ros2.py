import hello_helpers.hello_misc as hm

node = hm.HelloNode.quick_create('my_test_node')
node.move_to_pose({'joint_lift': 0.5})

