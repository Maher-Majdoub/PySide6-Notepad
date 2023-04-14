from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        #file menu
        file_menu = self.addMenu('File')
        self.new_file_act = file_menu.addAction('New')
        self.new_win_act = file_menu.addAction('New Window')
        self.open_file_act = file_menu.addAction('Open...')
        self.save_file_act = file_menu.addAction('Save')
        self.saveas_file_act = file_menu.addAction('Save As...')
        file_menu.addSeparator()
        self.print_act = file_menu.addAction('Print...')
        file_menu.addSeparator()
        self.exit_app_act = file_menu.addAction('Exit')
        
        #edit menu
        edit_menu = self.addMenu('Edit')
        self.undo_act = edit_menu.addAction('Undo')
        self.redo_act = edit_menu.addAction('Redo')
        edit_menu.addSeparator()
        self.cut_act = edit_menu.addAction('Cut')
        self.copy_act = edit_menu.addAction('Copy')
        self.paste_act = edit_menu.addAction('Paste')
        self.delete_act = edit_menu.addAction('Delete')
        edit_menu.addSeparator()
        self.googleit_act = edit_menu.addAction('Google it...')
        self.find_act = edit_menu.addAction('Find...')
        self.find_next_act = edit_menu.addAction('Find Next')
        self.find_previous_act = edit_menu.addAction('Find Previous')
        self.replace_act = edit_menu.addAction('Replace...')
        self.goto_act = edit_menu.addAction('Go To')
        edit_menu.addSeparator()
        self.select_all_act = edit_menu.addAction('Select All')
        self.time_date_act = edit_menu.addAction('Time/Date')
        
        #format menu
        format_menu = self.addMenu('Format')
        self.word_wrap_act = format_menu.addAction('Word Wrap')
        self.word_wrap_act.setCheckable(True)
        self.font_act = format_menu.addAction('Font...')
        
        #view menu
        self.view_menu = self.addMenu('View')
        self.zoom_menu =self.view_menu.addMenu('Zoom')
        self.zoom_in_act = self.zoom_menu.addAction('Zoom In')
        self.zoom_out_act = self.zoom_menu.addAction('Zoom Out')
        self.restore_default_act = self.zoom_menu.addAction('Restore Default Zoom')
        self.status_bar_act = self.view_menu.addAction('Status Bar')
        self.status_bar_act.setChecked(True)
        self.status_bar_act.setCheckable(True)
        
        #help menu
        help_menu = self.addMenu('Help')
        self.help_act = help_menu.addAction('View Help')
        self.send_feedback_act = help_menu.addAction('Send Feedback')
        help_menu.addSeparator()
        self.about_me_act = help_menu.addAction('About Meher')
        

        