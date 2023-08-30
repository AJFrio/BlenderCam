import os
import bpy
import Renderer as rd

camPos = bpy.data.objects['Camera'].location


rd.EightPointRender()