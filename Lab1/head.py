import hello_helpers.hello_misc as hm
import numpy as np

node = hm.HelloNode.quick_create('my_test_node')



#node.move_to_pose({'joint_head_pan': np.radians(60)}, blocking=True)
node.move_to_pose({'joint_head_tilt': np.radians(60)}, blocking=True)










