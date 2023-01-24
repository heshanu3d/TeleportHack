# coding: utf-8

import os, re
from xmlrpc.client import Boolean
import dearpygui.dearpygui as ui
import dearpygui.demo as demo


def set_theme(show_debug_editor : Boolean):
    with ui.theme() as global_theme:

        # with ui.theme_component(ui.mvAll):
        #     ui.add_theme_color(ui.mvThemeCol_FrameBg, (255, 140, 23), category=ui.mvThemeCat_Core)
        #     ui.add_theme_style(ui.mvStyleVar_FrameRounding, 5, category=ui.mvThemeCat_Core)

        # with ui.theme_component(ui.mvInputInt):
        #     ui.add_theme_color(ui.mvThemeCol_FrameBg, (140, 255, 23), category=ui.mvThemeCat_Core)
        #     ui.add_theme_style(ui.mvStyleVar_FrameRounding, 5, category=ui.mvThemeCat_Core)
        with ui.theme_component(ui.mvAll):
            ui.add_theme_color(ui.mvThemeCol_FrameBg, (226, 226, 226), category=ui.mvThemeCat_Core)
            ui.add_theme_style(ui.mvStyleVar_FrameBorderSize, 1, category=ui.mvThemeCat_Core)
            ui.add_theme_style(ui.mvStyleVar_FrameRounding, 10, category=ui.mvThemeCat_Core)

            ui.add_theme_color(ui.mvThemeCol_Text, (0, 0, 0, 255))
            ui.add_theme_color(ui.mvThemeCol_ChildBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_WindowBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_FrameBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_MenuBarBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_Header, (226, 226, 226, 255))

            ui.add_theme_color(ui.mvThemeCol_ScrollbarBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_ScrollbarGrab, (200, 200, 200, 255))
            ui.add_theme_color(ui.mvThemeCol_ScrollbarGrabActive, (140, 140, 140, 140))
            ui.add_theme_color(ui.mvThemeCol_ScrollbarGrabHovered, (170, 170, 170, 255))

            ui.add_theme_color(ui.mvThemeCol_Tab, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_TableHeaderBg, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_TabHovered, (198, 232, 255, 255))
            ui.add_theme_color(ui.mvThemeCol_TabActive, (153, 209, 255, 255))


    ui.bind_theme(global_theme)

    if show_debug_editor:
        ui.show_style_editor()
        demo.show_demo()
        ui.show_font_manager()
        return 1395
    else:
        return 410

def set_font(debug_mode : Boolean):
    size = 20
    with ui.font_registry():
        with ui.font('NotoSansSC-Regular.otf', size) as simple_chinese_font:
            ui.add_font_range_hint(ui.mvFontRangeHint_Default)
            ui.add_font_range_hint(ui.mvFontRangeHint_Chinese_Simplified_Common)
        if debug_mode:
            for file_name in os.listdir(os.path.curdir):
                if re.match('.*\.(ttf|TTF|otf)', file_name):
                    print(file_name)
                    with ui.font(file_name, size):
                        ui.add_font_range_hint(ui.mvFontRangeHint_Default)
                        ui.add_font_range_hint(ui.mvFontRangeHint_Chinese_Simplified_Common)
    ui.bind_font(simple_chinese_font)

def load_list_view(file_name : str):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if len(lines)%4 != 0:
            print(f"{file_name} lines count wrong")
            return
        for i in range(int(len(lines)/4)):
            with ui.table_row():
                for j in range(4):
                    # ui.add_text(lines[i*4 + j])
                    ui.add_text('测试  厄')

if __name__ == "__main__":
    ui.create_context()

    debug_mode = True
    debug_mode = False


    set_font(debug_mode)
    width = set_theme(debug_mode)

    ui.create_viewport(title="Teleport", width=width, height=900, decorated=True)
    ui.setup_dearpygui()

    with ui.window(label="Example Window", tag="Primary Window"):
        with ui.tab_bar():
            with ui.tab(label="functional"):
                with ui.child_window(width=380, height=500):
                    ui.add_text("list_view")
                    with ui.table(header_row=True, row_background=True,
                                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                                   borders_outerV=True, delay_search=True) as table_id:
                        ui.add_table_column(label="描述")
                        ui.add_table_column(label="X")
                        ui.add_table_column(label="Y")
                        ui.add_table_column(label="Z")
                        load_list_view('favlist.fav')
                        # for i in range(20):
                        #     with ui.table_row():
                        #         for j in range(4):
                        #             ui.add_text(f"行{i} 列{j}")
                        # with ui.table_row():
                        #     ui.add_text("行0 列0")

                with ui.child_window(width=380, height=100):
                    ui.add_text("button region")
                    ui.add_checkbox(label="sync_teleport")
                with ui.child_window(width=380, height=200):
                    ui.add_text("logs:")
            with ui.tab(label="nodes"):
                with ui.child_window(width=380, height=800):
                    ui.add_text("nodes")
            with ui.tab(label="config"):
                with ui.child_window(width=380, height=800):
                    ui.add_text("config")

    ui.show_viewport()
    ui.set_primary_window("Primary Window", True)
    ui.start_dearpygui()
    ui.destroy_context()