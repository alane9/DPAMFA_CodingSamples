import maya.cmds as mc
import random

# How to use:
# 1. Open Autodesk Maya
# 2. Open Script Editor and create a new tab (Specify executer source language: Python) 
# 3. Paste this script and run
# 4. The UI window "Create Shapes" will appear
# 5. Adjust parameters and press buttons to generate content
 
# (this is the function that controls shape creation)
def create_shapes():
    # Get values from the UI fields
    xMin = mc.floatFieldGrp("xPosField", query=True, value1=True)
    xMax = mc.floatFieldGrp("xPosField", query=True, value2=True)

    yMin = mc.floatFieldGrp("yPosField", query=True, value1=True)
    yMax = mc.floatFieldGrp("yPosField", query=True, value2=True)

    zMin = mc.floatFieldGrp("zPosField", query=True, value1=True)
    zMax = mc.floatFieldGrp("zPosField", query=True, value2=True)

    sMin = mc.floatFieldGrp("scaleField", query=True, value1=True)
    sMax = mc.floatFieldGrp("scaleField", query=True, value2=True)

    numObjects = mc.intField("numField", query=True, value=True)

    generate_objects(numObjects, xMin, xMax, yMin, yMax, zMin, zMax, sMin, sMax)


#SHAPE GENERATION
def generate_objects(numObjects, xMin, xMax, yMin, yMax, zMin, zMax, sMin, sMax):
    print("Adding shapes...")

    shapes = ['polyCube', 'polySphere', 'polyCone', 'polyCylinder']

    for i in range(numObjects):

        # cycle shape type: cube > sphere > cone > cylinder
        shapeType = i % 4
        shape = shapes[shapeType]

        # create the shape
        if shape == "polyCube":
            mc.polyCube()
        elif shape == "polySphere":
            mc.polySphere()
        elif shape == "polyCone":
            mc.polyCone()
        elif shape == "polyCylinder":
            mc.polyCylinder()

        # random transforms based on UI values
        randX = random.uniform(xMin, xMax)
        randY = random.uniform(yMin, yMax)
        randZ = random.uniform(zMin, zMax)

        randRx = random.uniform(-30, 30)
        randRy = random.uniform(-30, 30)
        randRz = random.uniform(-30, 30)

        randS = random.uniform(sMin, sMax)

        mc.move(randX, randY, randZ)
        mc.rotate(randRx, randRy, randRz)
        mc.scale(randS, randS, randS)


#CLEAR SCENE
def clear_scene():
    for obj in mc.ls(type="transform"):
        if obj not in ["persp", "top", "front", "side"]:
            mc.delete(obj)


# CREATE CAMERA
def create_camera():
    print("Adding camera...")
    cam = mc.camera(name="SceneCamera")[0]

    mc.setAttr(cam + ".translateX", 0)
    mc.setAttr(cam + ".translateY", 5)
    mc.setAttr(cam + ".translateZ", 20)

    return cam


#CREATE LIGHTS
def create_lights():
    print("Adding lights...")

    # Key light
    key = mc.directionalLight(name="keyLight")
    mc.setAttr("keyLight.translateX", 10)
    mc.setAttr("keyLight.translateY", 10)
    mc.setAttr("keyLight.translateZ", 10)

    # Fill light
    fill = mc.directionalLight(name="fillLight")
    mc.setAttr("fillLight.translateX", -10)
    mc.setAttr("fillLight.translateY", 8)
    mc.setAttr("fillLight.translateZ", 12)

    # Back light
    back = mc.directionalLight(name="backLight")
    mc.setAttr("backLight.translateX", 0)
    mc.setAttr("backLight.translateY", 12)
    mc.setAttr("backLight.translateZ", -10)


#RESET VALUES
def reset_values():
    mc.floatFieldGrp("xPosField", e=True, value1=0, value2=5)
    mc.floatFieldGrp("yPosField", e=True, value1=0, value2=5)
    mc.floatFieldGrp("zPosField", e=True, value1=0, value2=5)
    mc.floatFieldGrp("scaleField", e=True, value1=1, value2=5)
    mc.intField("numField", e=True, value=10)
    
    
# (this is the function that controls what the buttons do)
def create_ui():
    if mc.window("shapesUI", exists=True):
        mc.deleteUI("shapesUI")

    window = mc.window("shapesUI", title="Create Shapes", widthHeight=(300, 200))
    mc.columnLayout(adjustableColumn=True)
    
    
    


    # Position control
    mc.text(label="Position")
    mc.floatFieldGrp("xPosField", numberOfFields=2, label="X Position (min/max)", value1=-10, value2=10)
    mc.floatFieldGrp("yPosField", numberOfFields=2, label="Y Position (min/max)", value1=-10, value2=10)
    mc.floatFieldGrp("zPosField", numberOfFields=2, label="Z Position (min/max)", value1=-10, value2=10)

    # Scale control
    mc.text(label="Scale")
    mc.floatFieldGrp("scaleField", numberOfFields=2, label="Scale (min/max)", value1=1, value2=2)

    mc.text(label="Number of Objects")
    mc.intField("numField", value=15)
    
    # buttons
    mc.button(label="Generate Objects", command=lambda *_: create_shapes())
    mc.button(label="Clear Scene", command=lambda *_: clear_scene())
    mc.button(label="Create Camera", command=lambda *_: create_camera())
    mc.button(label="Add 3-Point Lights", command=lambda *_: create_lights())
    mc.button(label="Reset Values", command=lambda *_: reset_values())
    
    
    # Shelf Name
    mc.text(label="Shelf Name")
    mc.textField("shelfNameField")
    
    #Scroll Menu
    mc.scrollLayout("toolScroll", height=150, childResizable=True)
    mc.columnLayout("toolColumn", adjustableColumn=True)

    # List of tools
    tool_list = [
        "Create Cube",
        "Freeze Transforms",
        "Center Pivot",
        "Delete History",
        "Duplicate",
        "Smooth Mesh",
        "Create Sphere",
    ]

    # Checkboxes
    for tool in tool_list:
        mc.checkBox(label=tool, align='left')

    mc.setParent("..")  
    mc.setParent("..")  

 
    
    
    name = mc.textField("shelfNameField", q=True, text=True)
    children = mc.columnLayout("toolColumn", q=True, childArray=True)
    
    # Button to build Shelf

    mc.button(label="Build Shelf", height=40, c=build_shelf)


    mc.showWindow(window)
    
def build_shelf(*args):

    # Get shelf name
    shelf_name = mc.textField("shelfNameField", q=True, text=True)

    if not shelf_name:
        mc.warning("Please enter a shelf name!")
        return
        
    # Checkboxes

    checkboxes = mc.columnLayout("toolColumn", q=True, childArray=True)

    if mc.shelfLayout(shelf_name, exists=True):
        mc.deleteUI(shelf_name)

    new_shelf = mc.shelfLayout(shelf_name, parent="ShelfLayout")

    for cb in checkboxes:
        if mc.checkBox(cb, q=True, v=True):     
            label = mc.checkBox(cb, q=True, label=True)

            mc.shelfButton(
                parent=new_shelf,
                label=label,
                annotation=label,
                image="commandButton.png",
                command=f"print('{label} pressed!')"
            )

    print("Shelf created:", shelf_name)
        


# Launch UI
create_ui()