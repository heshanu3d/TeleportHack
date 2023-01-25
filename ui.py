# coding: utf-8

import os, re
from xmlrpc.client import Boolean
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def _config(sender, keyword, user_data):

    widget_type = dpg.get_item_type(sender)
    items = user_data

    if widget_type == "mvAppItemType::mvRadioButton":
        value = True

    else:
        keyword = dpg.get_item_label(sender)
        value = dpg.get_value(sender)

    if isinstance(user_data, list):
        for item in items:
            dpg.configure_item(item, **{keyword: value})
    else:
        dpg.configure_item(items, **{keyword: value})

def _add_config_options(item, columns, *names, **kwargs):

    if columns == 1:
        if 'before' in kwargs:
            for name in names:
                dpg.add_checkbox(label=name, callback=_config, user_data=item, before=kwargs['before'], default_value=dpg.get_item_configuration(item)[name])
        else:
            for name in names:
                dpg.add_checkbox(label=name, callback=_config, user_data=item, default_value=dpg.get_item_configuration(item)[name])

    else:

        if 'before' in kwargs:
            dpg.push_container_stack(dpg.add_table(header_row=False, before=kwargs['before']))
        else:
            dpg.push_container_stack(dpg.add_table(header_row=False))

        for i in range(columns):
            dpg.add_table_column()

        for i in range(int(len(names)/columns)):

            with dpg.table_row():
                for j in range(columns):
                    dpg.add_checkbox(label=names[i*columns + j],
                                     callback=_config, user_data=item,
                                     default_value=dpg.get_item_configuration(item)[names[i*columns + j]])
        dpg.pop_container_stack()

def show_debug_editor(is_show : Boolean):
    if is_show:
        dpg.show_style_editor()
        demo.show_demo()
        dpg.show_font_manager()
        return 1395
    else:
        return 630

def set_theme(themes: list):
    with dpg.theme() as border_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 1, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)

    with dpg.theme() as global_theme:

        # with dpg.theme_component(dpg.mvAll):
        #     dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
        #     dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        # with dpg.theme_component(dpg.mvInputInt):
        #     dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
        #     dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        with dpg.theme_component(dpg.mvAll):

            dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)

            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, category=dpg.mvThemeCat_Core)

            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (226, 226, 226), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Header, (226, 226, 226, 255))

            dpg.add_theme_color(dpg.mvThemeCol_Button, (226, 226, 226, 255))

            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (200, 200, 200, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (140, 140, 140, 140))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (170, 170, 170, 255))

            dpg.add_theme_color(dpg.mvThemeCol_Tab, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (226, 226, 226, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (198, 232, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, (153, 209, 255, 255))

    dpg.bind_theme(global_theme)

    themes.append(global_theme)
    themes.append(border_theme)

def set_font(debug_mode : Boolean):
    size = 20
    with dpg.font_registry():
        with dpg.font('NotoSansSC-Regular.otf', size, default_font=True) as simple_chinese_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        if debug_mode:
            for file_name in os.listdir(os.path.curdir):
                if re.match('.*\.(ttf|TTF|otf)', file_name):
                    print(file_name)
                    with dpg.font(file_name, size):
                        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
    dpg.bind_font(simple_chinese_font)

def teleport_cb(sender, data):
    print(sender.id)

def load_list_view(file_name : str):
    with open(file_name, 'r', encoding='utf-8')as file:
        lines = file.readlines()
        if len(lines)%4 != 0:
            print(f"{file_name} lines count wrong")
            return
        for i in range(int(len(lines)/4)):
            with dpg.table_row():
                for j in range(4):
                    if j > 0:
                        f = float(lines[i*4 + j])
                        dpg.add_text("%0.3f" % f)
                    else:
                        # dpg.add_text(lines[i*4 + j])
                        btn = dpg.add_button(label=lines[i*4 + j], width=300, callback=lambda ctrl:teleport_cb(ctrl))

                    # dpg.add_text('测试  厄')

if __name__ == "__main__":
    dpg.create_context()

    debug_mode = True
    # debug_mode = False

    themes = []
    set_font(debug_mode)
    width = show_debug_editor(debug_mode)
    set_theme(themes)
    border_theme = themes[1]

    dpg.create_viewport(title="Teleport", width=width, height=900, decorated=True)
    dpg.setup_dearpygui()

    with dpg.window(label="Example Window", tag="Primary Window"):
        with dpg.tab_bar():
            with dpg.tab(label="functional"):
                with dpg.child_window(width=600, height=500):
                    dpg.add_text("list_view")
                    with dpg.table(header_row=True, row_background=True, resizable=True,
                                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                                   borders_outerV=True, delay_search=True, policy=dpg.mvTable_SizingFixedFit,
                                   no_pad_innerX=True
                                   ) as table_id:
                        dpg.add_table_column(label="描述")
                        dpg.add_table_column(label="X")
                        dpg.add_table_column(label="Y")
                        dpg.add_table_column(label="Z")
                        load_list_view('favlist.fav')

                with dpg.child_window(width=600, height=100):
                    dpg.add_text("button region")
                    sync_teleport = dpg.add_checkbox(label="sync_teleport")
                    dpg.bind_item_theme(sync_teleport, border_theme)
                with dpg.child_window(width=600, height=200):
                    dpg.add_text("logs:")
            with dpg.tab(label="nodes"):
                with dpg.child_window(width=600, height=800):
                    dpg.add_text("nodes")
            with dpg.tab(label="config"):
                with dpg.child_window(width=600, height=800):
                    dpg.add_text("config")

    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()