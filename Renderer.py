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
    initPos = float(cam.location.y)
    rNum = 1
    render(rNum)
    rNum += 1
    cam.location.x = cam.location.y * -.75
    cam.location.y = cam.location.y * .75
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.x = initPos
    cam.location.y = 0
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.y = cam.location.x * .75
    cam.location.x = cam.location.x * .75
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.x = 0
    cam.location.y = -(initPos)
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.x = cam.location.y * .75
    cam.location.y = cam.location.y * .75
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.x = -initPos
    cam.location.y = 0
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)
    rNum += 1
    cam.location.y = cam.location.x * -.75
    cam.location.x = cam.location.x * .75
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
    render(rNum)

def center():
    cam.location.x = 0
    cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(45)

def EPRV2():
    r = cam.location.y
    for i in range(8):
        cam.location.x = r * math.cos(math.radians(45 * i))
        cam.location.y = r * math.sin(math.radians(45 * i))
        cam.rotation_euler[2] = cam.rotation_euler[2] + math.radians(-45)
        render(i + 1)

def test():
    r = 3
    x = 0
    y = 0
    rot = 0
    for i in range(8):
        x = r * math.cos(math.radians(45 * i))
        y = r * math.sin(math.radians(45 * i))
        rot = rot + math.radians(-45)
        render(i + 1)
        print(f"x: {x}, y: {y}")

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