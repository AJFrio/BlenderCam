import os
import bpy
import math
import mathutils

cam = bpy.data.objects['Camera']

def render(renderNumber):
    bpy.context.scene.render.filepath = f"C:/Users/af4fa/Desktop/TestRender/render{renderNumber}.png"
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still = True)

def EightPointRender():
    rNum = 1
    camLX, camLY = cam.location.x, cam.location.y
    camRZ = cam.rotation_euler[2]
    render(rNum)
    rNum += 1
    camLX = camLY * .75
    camLY = camLY * .75
    camRZ = camRZ + math.radians(-45)
    render(rNum)
    rNum += 1



    '''
    while rNum < 8:
        bpy.ops.render.render(write_still = True)
        if rNum % 2 == 0:
            camX += 2
        else:
            camY += 2
        cam.location.x, cam.location.y = camX, camY
        rNum += 1
        bpy.context.scene.render.filepath = f"C:/Users/af4fa/Desktop/TestRender/render{rNum}.png"
'''