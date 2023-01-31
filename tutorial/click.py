import dearpygui.dearpygui as dpg

dpg.create_context()

def change_text():
    print("Clicked!")


with dpg.window(width=500, height=300):
    # with dpg.drawlist(width=200, height=200, tag="drawlist"):
    #     dpg.draw_circle([100, 100], 100, fill=[255, 255, 255, 100], tag="Circle_id", parent="drawlist" )
    #
    # with dpg.item_handler_registry(tag="widget handler"):
    #     dpg.add_item_clicked_handler(callback=change_text)
    #
    # dpg.bind_item_handler_registry("drawlist", "widget handler")
    
    with dpg.table(header_row=True, row_background=True, resizable=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, delay_search=True, policy=dpg.mvTable_SizingFixedSame):
        dpg.add_table_column(label="description")
        dpg.add_table_column(label="X")
        dpg.add_table_column(label="Y")
        dpg.add_table_column(label="Z")
        with dpg.table_row(tag='row'):
            for i in range(0, 4):
                dpg.add_text("1")
        with dpg.item_handler_registry(tag="handler"):
            dpg.add_item_clicked_handler(callback=change_text)
        dpg.bind_item_handler_registry("row", "handler")


dpg.create_viewport(title="Viewport name")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()