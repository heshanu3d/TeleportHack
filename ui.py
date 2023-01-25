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
                dpg.add_checkbox(label=name, callback=_config, user_data=item, before=kwargs['before'],
                                 default_value=dpg.get_item_configuration(item)[name])
        else:
            for name in names:
                dpg.add_checkbox(label=name, callback=_config, user_data=item,
                                 default_value=dpg.get_item_configuration(item)[name])

    else:

        if 'before' in kwargs:
            dpg.push_container_stack(dpg.add_table(header_row=False, before=kwargs['before']))
        else:
            dpg.push_container_stack(dpg.add_table(header_row=False))

        for i in range(columns):
            dpg.add_table_column()

        for i in range(int(len(names) / columns)):

            with dpg.table_row():
                for j in range(columns):
                    dpg.add_checkbox(label=names[i * columns + j],
                                     callback=_config, user_data=item,
                                     default_value=dpg.get_item_configuration(item)[names[i * columns + j]])
        dpg.pop_container_stack()


def show_debug_editor(is_show: Boolean) -> int:
    if is_show:
        dpg.show_style_editor()
        demo.show_demo()
        # dpg.show_font_manager()
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

            # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (226, 226, 226), category=dpg.mvThemeCat_Core)
            # dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_Header, (226, 226, 226, 255))
            #
            # dpg.add_theme_color(dpg.mvThemeCol_Button, (226, 226, 226, 255))
            #
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (200, 200, 200, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (140, 140, 140, 140))
            # dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (170, 170, 170, 255))
            #
            # dpg.add_theme_color(dpg.mvThemeCol_Tab, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (226, 226, 226, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (198, 232, 255, 255))
            # dpg.add_theme_color(dpg.mvThemeCol_TabActive, (153, 209, 255, 255))

    dpg.bind_theme(global_theme)

    themes.append(global_theme)
    themes.append(border_theme)


def set_font(debug: Boolean):
    size = 20
    with dpg.font_registry():
        with dpg.font('NotoSansSC-Regular.otf', size, default_font=True) as simple_chinese_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        if debug:
            for file_name in os.listdir(os.path.curdir):
                if re.match('.*\.(ttf|TTF|otf)', file_name):
                    print(file_name)
                    with dpg.font(file_name, size):
                        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
    dpg.bind_font(simple_chinese_font)


class TeleportDict():
    def __init__(self):
        self._dict = {}

    def insert(self, key, value):
        if not key in self._dict:
            self._dict[key] = value
        else:
            multi_value = []
            if type(self._dict[key]) == list:
                multi_value = [v for v in self._dict[key]]
            elif type(self._dict[key]) == int:
                multi_value = [self._dict[key]]
            multi_value.append(value)
            self._dict[key] = multi_value

    def get(self, key):
        if key in self._dict.keys():
            return self._dict[key]
        else:
            return None

    def modify(self, key, old_value, new_value):
        value = self.get(key)
        modified_value = []
        if type(value) == 'list':
            modified_value = [v for v in value if v != old_value]
            modified_value.append(new_value)
            self._dict[key] = modified_value
        else:
            self._dict[key] = new_value

    def delete(self, key):
        # if key in self._dict.keys():
        self._dict.pop(key)

    def clear(self):
        self._dict.clear()

    def traverse(self):
        for k, v in self._dict.items():
            print(k, v)


def load_list_view(file_name: str, table_id : int):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) % 4 != 0:
            print(f"{file_name} lines count wrong")
            return
        for i in range(int(len(lines) / 4)):
            row = dpg.add_table_row(parent=table_id)
            for j in range(4):
                if j > 0:
                    f = float(lines[i * 4 + j])
                    dpg.add_text("%0.3f" % f, parent=row)
                else:
                    # dpg.add_text(lines[i*4 + j])
                    btn = dpg.add_button(label=lines[i * 4 + j], width=300, callback=teleport_cb, parent=row)
                    # data = [lines[i*4 + j + 1], lines[i*4 + j + 2], lines[i*4 + j + 3]]
                    # dpg.set_item_user_data(btn, data)
                    teleport_dict.insert(lines[i * 4 + j].strip(), btn)


def teleport_cb(sender, app_data, user_data):
    print(f"----------------------[teleport_cb] execute: ---------------------------\nsender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")
    # print(dpg.get_item_parent(sender))
    # print(dpg.get_item_children(dpg.get_item_parent(sender)))
    children = dpg.get_item_children(dpg.get_item_parent(sender))[1]
    print('children:', children)
    print(dpg.get_item_label(sender).strip())
    row_value = [dpg.get_value(child) for child in children if dpg.get_value(child)]
    print(row_value)
    # for child in children:
    #     print(dpg.get_value(child))


def test_cb(sender, app_data, user_data):
    print("test_cb")
    value = teleport_dict.get('通灵学院-入口')
    if value:
        print(value)
        for v in value:
            parent = dpg.get_item_parent(v)
            dpg.delete_item(parent)
        teleport_dict.delete('通灵学院-入口')
    # teleport_dict.traverse()


def recurse_delete_item(sender):
    children = dpg.get_item_children(sender)
    # print(children)
    children = children[1]
    for child in children:
        recurse_delete_item(child)
        dpg.delete_item(child)
        # print(child)


def refresh_cb():
    children = recurse_delete_item(functional_tab)
    teleport_dict.clear()
    create_functional_tab(functional_tab)
    print(teleport_dict.get('通灵学院-入口'))

    # print(children)
    # for child in dpg.get_item_children(functional_tab):
    #     dpg.delete_item(child)


def create_functional_tab(root):
    dpg.add_text("list_view", parent=root)
    table_id = dpg.add_table(header_row=True, row_background=True, resizable=True,
                   borders_innerH=True, borders_outerH=True, borders_innerV=True,
                   borders_outerV=True, delay_search=True, policy=dpg.mvTable_SizingFixedFit,
                   no_pad_innerX=True,
                   parent=root)
    dpg.add_table_column(label="描述", parent=table_id)
    dpg.add_table_column(label="X", parent=table_id)
    dpg.add_table_column(label="Y", parent=table_id)
    dpg.add_table_column(label="Z", parent=table_id)
    load_list_view('favlist.fav', table_id)


if __name__ == "__main__":
    dpg.create_context()

    debug_mode = True
    debug_mode = False

    teleport_dict = TeleportDict()

    themes = []
    set_font(debug_mode)
    width = show_debug_editor(debug_mode)
    set_theme(themes)
    border_theme = themes[1]

    dpg.create_viewport(title="Teleport", width=width, height=900, decorated=True)
    dpg.setup_dearpygui()

    with dpg.window(label="Example Window", tag="Primary_Window"):
        with dpg.tab_bar():
            with dpg.tab(label="functional"):
                with dpg.child_window(width=600, height=500) as functional_tab:
                    create_functional_tab(functional_tab)
                    # dpg.add_text("list_view")
                    # with dpg.table(header_row=True, row_background=True, resizable=True,
                    #                borders_innerH=True, borders_outerH=True, borders_innerV=True,
                    #                borders_outerV=True, delay_search=True, policy=dpg.mvTable_SizingFixedFit,
                    #                no_pad_innerX=True
                    #                ) as table_id:
                    #     dpg.add_table_column(label="描述")
                    #     dpg.add_table_column(label="X")
                    #     dpg.add_table_column(label="Y")
                    #     dpg.add_table_column(label="Z")
                    #     load_list_view('favlist.fav')

                with dpg.child_window(width=600, height=100):
                    dpg.add_text("button region")
                    sync_teleport = dpg.add_checkbox(label="sync_teleport")
                    dpg.bind_item_theme(sync_teleport, border_theme)
                    dpg.add_input_text(default_value='', width=150)
                    dpg.add_button(label="test_cb", callback=test_cb)
                    dpg.add_button(label="refresh", callback=refresh_cb)
                with dpg.child_window(width=600, height=200):
                    dpg.add_text("logs:")
            with dpg.tab(label="nodes"):
                with dpg.child_window(width=600, height=800):
                    dpg.add_text("nodes")
            with dpg.tab(label="config"):
                with dpg.child_window(width=600, height=800):
                    dpg.add_text("config")

    dpg.show_viewport()
    dpg.set_primary_window("Primary_Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
