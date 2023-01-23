Blender Spacing Tool (BST)
Software: Blender 3.4.1
Author: Aryn Taylor
Date 20-01-2023

The Blender Spacing Tool (BST v1.0) is a custom Python scripted 
plugin for Blender that allows the user to space an array of 
instantiated objects along a curve or path. 

This plugin has been designed to improve the process of arraying 
an object along a curve, and has been inspired by a similar feature 
present in 3DsMax.

How to use:

This addon should be used in the following way:

    1. Create or import your object (eg. a stair post)

    2. Draw a curve

    3. Either press the "Add Path Point button, or goto 
       Add>Mesh>Single Vert>Add Singe Vert, or you can also
       goto Add>Mesh and select a Plane, Cube, etc.

       This will define the Path Point position and will be
       used to instantiate our object in the next step!

    4. Select the object, then the curve, and finally the Path
       Point, and press the "Array Along Path" button. This
       will array your object along the path by instantiating
       the object onto the arrayed path points.

    5. At this point an Operator Menu will pop up in the bottom
       left-hand corner. You can manipulate the values to
       achieve your desired effect.

    6. If you ever wish to manipulate these values again please
       note the modifiers will be accessible in the modifiers
       tab on the path point.