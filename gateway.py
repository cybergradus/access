import random

scale_min = 0.1
scale_max = 2.5

def run():
    print('well, well, well...')
    random_scale = random.uniform(scale_min, scale_max)
    print(f'{random_scale}:random_scale')
    try:
        import maya.cmds as mc
        mc.scale(random_scale, random_scale, random_scale, mc.ls(sl=True))
    except:
        print('exception!')
        pass