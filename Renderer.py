import os
import bpy

cam = bpy.data.objects['Camera']

def EightPointRender():
    rNum = 1
    camX, camY = cam.location.x, cam.location.y

    bpy.context.scene.render.filepath = f"C:/Users/af4fa/Desktop/TestRender/render{rNum}.png"
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.ops.render.render(write_still = True)
    while rNum < 8:
        bpy.ops.render.render(write_still = True)
        if rNum % 2 == 0:
            camX += 2
        else:
            camY += 2
        cam.location.x, cam.location.y = camX, camY
        rNum += 1
        bpy.context.scene.render.filepath = f"C:/Users/af4fa/Desktop/TestRender/render{rNum}.png"
