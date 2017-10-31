import bpy

#Changing all objects in a group to a custom shaped object
group_name = 'Group.001'
linked = False   

chosen = bpy.data.objects["Icosphere"]
mygroup = bpy.data.groups[group_name].objects 
for obj in mygroup:
    if linked :
        obj.data = chosen.data        # linked duplicates
    else :
        l = obj.location.copy()
        obj.data = chosen.data.copy() # Non linked duplicates
        obj.location = l
        obj.scale = chosen.scale