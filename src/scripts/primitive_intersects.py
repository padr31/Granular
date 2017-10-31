import bpy
from math import *


def intersects(obj1, obj2):
    obj1_x = obj1.location.x
    obj1_y = obj1.location.y
    obj1_z = obj1.location.z
    
    obj2_x = obj2.location.x
    obj2_y = obj2.location.y
    obj2_z = obj2.location.z
    
    obj1_dim_x = obj1.dimensions.x
    obj1_dim_y = obj1.dimensions.y
    obj1_dim_z = obj1.dimensions.z
    
    obj2_dim_x = obj2.dimensions.x
    obj2_dim_y = obj2.dimensions.y
    obj2_dim_z = obj2.dimensions.z
    
    
    th = 0.05*(((obj1_dim_x+obj1_dim_y + obj1_dim_z)/3 + (obj2_dim_x+obj2_dim_y + obj2_dim_z)/3)/2)
    
    if (fabs(obj1_x - obj2_x)) >= ((obj1_dim_x+obj2_dim_x)/2 + th) or (fabs(obj1_y - obj2_y)) >= ((obj1_dim_y+obj2_dim_y)/2 + th) or (fabs(obj1_z - obj2_z)) >= ((obj1_dim_z+obj2_dim_z)/2 + th):
        return False
    else:
        return True

g = bpy.data.groups["Group.001"]
count = 0
num = 0
for i in g.objects:
    num+=1
    for j in g.objects:
        if i == j:
            continue
        count+=intersects(i, j)
        
print(count)
print(num)        
print((count/(num)))
