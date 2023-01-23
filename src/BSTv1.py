# Blender Spacing Tool (BST)
# Target Software: Blender 3.4.1
# Author: Aryn Taylor
# Date 22-01-2023

bl_info = {
    "name": "Blender Spacing Tool v1.0",
    "author": "Aryn Taylor",
    "version": (0, 1, 0),
    "blender": (3, 4, 1),
    "location": "View3D > Sidebar > BSTv1.0",
    "description": "Distribute objects based on the "
                   "current selection along a path "
                   "defined by a spline or a pair of points.",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy
from bpy.types import (Panel, Operator)

class MESH_OT_ArrayAlongPath(bpy.types.Operator):
    """Creates an array along a defined path"""
    bl_idname = "mesh.array_along_path"
    bl_label = "Array Along Path"
    bl_options = {'REGISTER', 'UNDO'}

    spacing_X: bpy.props.FloatProperty(
        name="Spacing: X Axis",
        description="Space in units along X between the objects.",
        default= 0, 
        min= 0,
        soft_min= 0
    )

    spacing_Y: bpy.props.FloatProperty(
        name="Spacing: Y Axis",
        description="Space in units along Y between the objects.",
        default= 0, 
        min= 0,
        soft_min= 0
    )

    spacing_Z: bpy.props.FloatProperty(
        name="Spacing: Z Axis",
        description="Space in units along Z between the objects.",
        default= 0, 
        min= 0,
        soft_min= 0
    )

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'
    
    def execute(self, context): 

        numSelectedObj = len(bpy.context.selected_objects)

        if numSelectedObj <= 2:
            self.report({'ERROR'}, "You must select an object, a curve, and a PathPoint.")
            return{'CANCELLED'}

        path_point = bpy.context.active_object
        obj = bpy.context.selected_objects[0]
        path = bpy.context.selected_objects[1]

        if obj == path_point or path == path_point:
            self.report({'ERROR'}, "Active selection must be PathPoint.")
            return{'CANCELLED'}

        if "Array" not in path_point:
            mod = path_point.modifiers.new(name="Array", type='ARRAY')

            mod.use_relative_offset = False
            mod.use_constant_offset = True

            mod.fit_type = 'FIT_CURVE'
            mod.curve = path

        mod.constant_offset_displace[0] = self.spacing_X
        mod.constant_offset_displace[1] = self.spacing_Y
        mod.constant_offset_displace[2] = self.spacing_Z

        if "Curve" not in path_point:
            curve_mod = path_point.modifiers.new(name="Curve", type='CURVE')
            curve_mod.object = path

        obj.parent = path_point

        path_point.instance_type = 'VERTS'
        path_point.show_instancer_for_viewport = False
        path_point.show_instancer_for_render = False

        return{'FINISHED'}

class MESH_OT_AddPathPoint(bpy.types.Operator):
    """Adds a new Path Point in the viewport"""
    bl_idname = "mesh.add_path_point"
    bl_label = "Add Path Point"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context): 
        bpy.ops.mesh.primitive_vert_add()
        vert = bpy.context.active_object

        bpy.ops.object.editmode_toggle(0)

        vert.name = "PathPoint"
        vert.data.name = "PathPoint"
        return{'FINISHED'}

class VIEW3D_PT_blender_spacing_tool(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Spacing Tool'
    bl_label = 'Spacing Tool'

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        col = layout.column(align=True)

        row.operator('mesh.array_along_path',
        text ='Array Along Path',
        icon='MOD_ARRAY')

        col.operator('mesh.add_path_point',
        text='Add Path Point',
        icon='DOT')
            
def register():
    bpy.utils.register_class(MESH_OT_ArrayAlongPath)
    bpy.utils.register_class(MESH_OT_AddPathPoint)
    bpy.utils.register_class(VIEW3D_PT_blender_spacing_tool)

def unregister():
    bpy.utils.unregister_class(MESH_OT_ArrayAlongPath)
    bpy.utils.unregister_class(MESH_OT_AddPathPoint)
    bpy.utils.unregister_class(VIEW3D_PT_blender_spacing_tool)

    if __name__ == '__main__':
        register()