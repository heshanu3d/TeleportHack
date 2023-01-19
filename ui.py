from xmlrpc.client import Boolean
import dearpygui.dearpygui as ui
# from pip import main

def set_font(show_editor : Boolean):
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
            ui.add_theme_color(ui.mvThemeCol_Tab, (226, 226, 226, 255))
            ui.add_theme_color(ui.mvThemeCol_TabHovered, (198, 232, 255, 255))
            ui.add_theme_color(ui.mvThemeCol_TabActive, (153, 209, 255, 255))
    ui.bind_theme(global_theme)
    if show_editor:
        ui.show_style_editor()
        return 1395
    else:
        return 395

if __name__ == "__main__":
    ui.create_context()

    # width = set_font(True)
    width = set_font(False)
    ui.create_viewport(title="Teleport", width=width, height=850, decorated=True)
    ui.setup_dearpygui()

    with ui.window(label="Example Window", tag="Primary Window"):
        with ui.tab_bar():
            with ui.tab(label="functional"):
                with ui.child_window(width=380, height=500):
                    ui.add_text("list_view")
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