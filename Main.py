from GUI import init_main_window, init_selection_panel, init_main_label, init_date


# Mainloop of WEATHER.APP
if __name__ == "__main__":
    # Objects Initialization
    root = init_main_window()
    init_selection_panel(root)
    init_date(root)
    init_main_label(root)

    root.mainloop()
