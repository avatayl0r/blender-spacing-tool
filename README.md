# blender-spacing-tool

**Blender Spacing Tool v1.0 for Blender 3.4.1!**

The Blender Spacing Tool (BST v1.0) is a FREE plugin for Blender that allows the user to space an array of instantiated objects along a curve or path. This plugin has been designed to improve the process of arraying an object along a curve, and has been inspired by a similar feature present in 3DsMax.

This tool allows you to:

+   Create an Array Along a Defined Path with "Array Along Path" button
+   Allow you to customise the spacing on this array, as well as control axis influence
+   Create a new path point with "Add Path Point" button
+   By manipulating the curve, you can change the shape and length of this array in real-time!

**How to use**
This addon should be used in the following way:

+   Create or import your object (eg. a stair post)
+   Draw a curve
+   Either press the "Add Path Point" button, or go to Add>Mesh>Single Vert>Add Single Vert, or you can also go to Add>Mesh       and select a Plane, Cube, etc. (This will define the Path Point position in the 3D space and will be used to instantiate     our object in the next step)
+   Select the object, then the curve, and finally the path point, and press the "Array Along Path" button. This will array       your object along the path by instantiating the object onto the arrayed path points.
+   At this point an Operator Menu will pop up in the bottom left-hand corner. You can manipulate the values to achieve your     desired effect.
+   If you ever wish to manipulate these values again please note the modifiers will be accessible under the modifiers tab on     the path point.
