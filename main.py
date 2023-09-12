import os
import bpy
import math
import time

cam = bpy.data.objects['Camera']

def render(renderNumber):
    bpy.context.scene.render.filepath = f"C:\\Users\\AJF\\OneDrive - Rep Fitness\\Desktop\\BlenderS\\r{renderNumber}.png"
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still = True)

#Y must be greater than 0, it will be the radius of the circle
def center(y: float, z: float) -> None:
    '''Centers the camera on the x axis and moves to y and z coordinates
    params:
        y: Y coordinate of the camera
        z: Z coordinate of the camera
    returns:
        None
    '''
    cam.location.x = 0
    cam.location.y = y
    cam.location.z = z
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(0)
    cam.rotation_euler[1] = cam.rotation_euler[1] + math.radians(0)

def EPR() -> None:
    '''
    Camera orbits at a distance of y set in center() and takes 8 renders 
    returns:
        None
    '''
    r = cam.location.y
    render(0)
    for i in range(8):
        cam.location.x = r * math.cos(math.radians(90 - (45 * (i + 1))))
        cam.location.y = r * math.sin(math.radians(90 - (45 * (i + 1))))
        cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
        render(i + 1)
        

#Coordinates for personal test
center(-20.37, 12.5)
EPR()
