# -*- coding: utf-8 -*-

"""
Copyright (c) 2023 Colin Curtain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Colin Curtain (ccbogel)
https://github.com/ccbogel/QualCoder
"""

import logging
import os
import sys
import traceback

from PyQt6 import QtGui, QtWidgets, QtCore

from .GUI.ui_dialog_colour_selector import Ui_Dialog_colour_selector


path = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger(__name__)


def exception_handler(exception_type, value, tb_obj):
    """ Global exception handler useful in GUIs.
    tb_obj: exception.__traceback__ """
    tb = '\n'.join(traceback.format_tb(tb_obj))
    text = 'Traceback (most recent call last):\n' + tb + '\n' + exception_type.__name__ + ': ' + str(value)
    print(text)
    logger.error(_("Uncaught exception: ") + text)
    QtWidgets.QMessageBox.critical(None, _('Uncaught Exception'), text)


class TextColor:
    """ Returns light or dark depending on the code color. """

    white_text = [
        "#EB7333", "#E65100", "#C54949", "#B71C1C", "#CB5E3C", "#BF360C",
        "#FA58F4", "B76E95", "#9F3E72", "#880E4F", "#7D26CD",  "#1B5E20",
        "#487E4B", "#1B5E20", "#5E9179", "#AC58FA", "#5E9179", "#9090E3",
        "#6B6BDA", "#4646D1", "#3498DB", "#6D91C6", "#3D6CB3", "#0D47A1",
        "#9090E3"]
    recommendation = "#000000"

    def __init__(self, color):
        if color in self.white_text:
            self.recommendation = "#eeeeee"
        else:
            self.recommendation = "#000000"


colors = [
    "#F5F6CE", "#F2F5A9", "#F4FA58", "#F7FE2E", "#DDE600", "#F8ECE0", "#F6E3CE", "#F5D0A9", "#F7BE81", "#FAAC58",
    "#F5ECCE", "#F3E2A9", "#F5DA81", "#F7D358", "#FACC2E", "#F8E0E0", "#F6CECE", "#F5A9A9", "#F78181", "#FA5858",
    "#F8E6E0", "#F6D8CE", "#F5BCA9", "#F79F81", "#FA8258", "#FADCCC", "#F5B999", "#F09666", "#EB7333", "#E65100",
    "#FFE2CC", "#FFC599", "#FFA866", "#FF8B33", "#FF6F00", "#F0D1D1", "#E2A4A4", "#D37676", "#C54949", "#B71C1C",
    "#F2D6CE", "#E5AE9D", "#D8866D", "#CB5E3C", "#BF360C", "#E7CEDB", "#CF9EB8", "#B76E95", "#9F3E72", "#880E4F",
    "#F8E0E6", "#F6CED8", "#F5A9BC", "#F7819F", "#FA5882", "#F8E0F7", "#F6CEF5", "#F5A9F2", "#F781F3", "#FA58F4",
    "#E4D3F5", "#CAA8EB", "#B07CE1", "#9651D7", "#7D26CD", "#ECE0F8", "#E3CEF6", "#D0A9F5", "#BE81F7", "#AC58FA",
    "#D1DED2", "#A3BEA5", "#769E78", "#487E4B", "#1B5E20", "#DEE9E4", "#BED3C9", "#9EBDAE", "#7EA793", "#5E9179",
    "#CEF6E3", "#A9F5D0", "#81F7BE", "#58FAAC", "#00FF7F", "#E0F8E0", "#CEF6CE", "#A9F5A9", "#81F781", "#58FA58",
    "#D0F5A9", "#BEF781", "#ACFA58", "#9AFE2E", "#80FF00", "#CEF6F5", "#A9F5F2", "#81F7F3", "#58FAF4", "#00F0F0",
    "#DADAF5", "#B5B5EC", "#9090E3", "#6B6BDA", "#4646D1", "#CEE3F6", "#A9D0F5", "#81BEF7", "#3498DB", "#5882FA",
    "#CEDAEC", "#9EB5D9", "#6D91C6", "#3D6CB3", "#0D47A1", "#E8E8E8", "#D8D8D8", "#C8C8C8", "#B8B8B8", "#A8A8A8"
    ]

# www.color-blindness.com/coblis-color-blindness-simulator/
# https://imagecolorpicker.com/en
colors_red_weak = [
    "#FBF4D0", "#FAF2B3", "#FBF598", "#1E1D03", "#232105", "#F6EDE0", "#F2E4CF", "#EAD4AB", "#E5C584", "#E0B75B",
    "#F6ECCE", "#F3E2A9", "#F2DB81", "#F1D559", "#F1D02F", "#EFE3E2", "#E6D3D1", "#D5B5B0", "#C7978C", "#BD7C66",
    "#F3E8E1", "#EBDBD0", "#DFC4AD", "#D5AD87", "#CD9860", "#F0DFCE", "#DFC19D", "#CFA46B", "#C08939", "#B2710F",
    "#F6E5CD", "#EBCC9C", "#E0B56B", "#D69F38", "#CC8B0F", "#E4D5D3", "#C8AEA9", "#AD877E", "#966454", "#854626",
    "#E8D9D0", "#D0B6A1", "#B89373", "#A37343", "#905615", "#DCD2DD", "#B7A6BD", "#937C9E", "#705481", "#563264",
    "#EEE3E8", "#E5D4DB", "#D3B6C3", "#C398AC", "#B77D96", "#ECE4F9", "#E1D5F9", "#CAB8FA", "#B69CFB", "#A582FB",
    "#DAD6F7", "#B2AFF0", "#8489EC", "#3764E5", "#2D45BF", "#E6E2F9", "#D6D2F9", "#B4B2FB", "#8F90FC", "#5F71FD",
    "#DBDBD0", "#B5B9A2", "#8F9775", "#697648", "#44561E", "#E6E7E3", "#CCCFC7", "#B1B8AB", "#96A190", "#7C8A75",
    "#E6EFDF", "#D5EACA", "#C6E8B7", "#B7E7A4", "#9AE977", "#F1F3DD", "#E8EFCA", "#D8E9A4", "#C9E67B", "#BBE652",
    "#EBEDA6", "#E6EC7D", "#E0EC54", "#DAED36", "#D0EC00", "#E4F0F1", "#D2EBEC", "#C1E9EB", "#B1EAEA", "#89DFE5",
    "#D9DAF5", "#AFB7ED", "#8393E6", "#4C71E0", "#1951C0", "#D8E0F4", "#BACCF2", "#9AB9F3", "#6091D6", "#4F83FB",
    "#D4D8EB", "#A6B3D7", "#798EC4", "#486AB1", "#05489D", "#EBE7E8", "#DAD7D8", "#CAC7C8", "#BAB7B8", "#AAA7A8"
    ]

colors_red_blind = [
    "#FFF3D0", "#FFF0B9", "#FFF1BC", "#FFF4CC", "#F9DD00", "#F5EDE0", "#EFE5CF", "#E4D6AC", "#DAC985", "#D1BD5D",
    "#F7EBCE", "#F3E2A9", "#F0DC82", "#EED659", "#EBD22F", "#EAE4E3", "#DCD7D3", "#C3BCB3", "#ACA492", "#9B906E",
    "#F0E9E1", "#E5DDD1", "#D3C9AF", "#C2B58B", "#B3A464", "#EAE1CF", "#D2C69F", "#BCAD6F", "#A7963D", "#948418",
    "#F1E7CE", "#F1E7CE", "#CEBC6D", "#BEAA3B", "#AF9C18", "#DDD7D5", "#B9B3AC", "#979183", "#7B735A", "#695F2C",
    "#E3DBD1", "#C4BAA3", "#A69B76", "#8C7F47", "#766919", "#D6D4DE", "#A9ABC0", "#7E84A4", "#55618A", "#394770",
    "#E9E5E9", "#DBD7DD", "#BFBDC8", "#A5A5B4", "#9192A1", "#E6E6FB", "#D4D9FC", "#B2C1FF", "#91ABFF", "#749AFF",
    "#D4D8F8", "#A4B4F4", "#6B90F3", "#006FED", "#0057B7", "#E2E3FA", "#CFD4FA", "#A3B6FF", "#7399FF", "#337FFF",
    "#E1D9CF", "#BFB6A1", "#9D9373", "#7C7146", "#5B511D", "#EBE5E2", "#D3CDC6", "#BCB5AA", "#A49D8E", "#8D8673",
    "#F4EBDD", "#EFE3C7", "#EDDFB2", "#EDDC9F", "#F2DC73", "#FAF0DC", "#F7EAC8", "#F3E2A1", "#F2DC78", "#F3DA4F",
    "#FBE8A4", "#FCE57B", "#FEE452", "#FFE43A", "#FDE100", "#F1ECEF", "#EAE5E9", "#E6E2E6", "#E4E0E5", "#D7D5DF",
    "#D8DAF5", "#ACB8EE", "#7B95E7", "#3A74E3", "#0057B7", "#DEDEF3", "#C3C9F1", "#A8B6F1", "#798ED2", "#4A84FC",
    "#D7D7EA", "#ABB2D7", "#7F8DC3", "#4F69B0", "#00499B", "#ECE7E7", "#DCD7D7", "#CBC7C7", "#BBB7B7", "#ABA7A8"
    ]

colors_green_weak = [
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"
    ]

colors_green_blind = [
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#",
    "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"
    ]

COLS = 10
ROWS = 12


def color_matcher(hex_color):
    """ Match a colour similar to a color in the colors list.
    Used with REFI import """

    if len(hex_color) != 7:
        return "#D8D8D8"  # light gray
    test_r = int(hex_color[1:3], 16)
    test_g = int(hex_color[3:5], 16)
    test_b = int(hex_color[5:7], 16)

    best_match = ["#D8D8D8", 255.0]  # light gray default, colour difference
    for c in colors:
        r = int(c[1:3], 16)
        g = int(c[3:5], 16)
        b = int(c[5:7], 16)
        diff = (abs(r - test_r) + abs(g - test_g) + abs(b - test_b)) / 3
        if diff < best_match[1]:
            best_match = [c, diff]
    return best_match[0]


class DialogColorSelect(QtWidgets.QDialog):
    """ Dialog to select colour for code.
    Useful site for colours: https://www.tutorialrepublic.com/html-reference/html-color-picker.php
    """

    selected_color = None
    used_colors = []

    def __init__(self, app, code_, parent=None):

        super(DialogColorSelect, self).__init__(parent)
        sys.excepthook = exception_handler
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog_colour_selector()
        self.ui.setupUi(self)
        cur = app.conn.cursor()
        cur.execute("select color, name from code_name order by name")
        self.used_colors = cur.fetchall()
        self.fill_table()
        self.ui.tableWidget.installEventFilter(self)
        self.ui.tableWidget.setFocus()
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowType.WindowContextHelpButtonHint)
        font = 'font: ' + str(app.settings['fontsize']) + 'pt '
        font += '"' + app.settings['font'] + '";'
        self.setStyleSheet(font)
        self.selected_color = code_['color']
        # preset with the current colour
        fg_color = TextColor(code_['color']).recommendation
        style = "QLabel {background-color :" + code_['color'] + "; color : " + fg_color + ";}"
        self.ui.label_colour_old.setStyleSheet(style)
        self.ui.label_colour_old.setAutoFillBackground(True)
        self.ui.label_colour_old.setToolTip(_("Current colour"))
        self.ui.label_colour_old.setText(code_['name'])
        self.ui.label_colour_new.setToolTip(_("New colour"))
        self.ui.label_colour_new.setText(code_['name'])

    def eventFilter(self, object, event):
        """ Using this event filter to apply appearance of several types of colour blindness
        N normal vision
        R Red weak
        Shift R Red blind
        G Green Weak
        Shift G Green blind
        """

        if type(event) == QtGui.QKeyEvent:
            key = event.key()
            mod = event.modifiers()
            if key == QtCore.Qt.Key.Key_N:
                self.fill_table()
                return True
            if key == QtCore.Qt.Key.Key_R and mod == QtCore.Qt.KeyboardModifier.ShiftModifier:
                self.fill_table("red_blind")
                return True
            if key == QtCore.Qt.Key.Key_R:
                self.fill_table("red_weak")
                return True
            if key == QtCore.Qt.Key.Key_G and mod == QtCore.Qt.KeyboardModifier.ShiftModifier:
                self.fill_table("green_blind")
                return True
            if key == QtCore.Qt.Key.Key_G:
                self.fill_table("green weak")
                return True
        return False

    def color_selected(self):
        """ Get colour selection from table widget. """

        x = self.ui.tableWidget.currentRow()
        y = self.ui.tableWidget.currentColumn()
        self.selected_color = colors[x * COLS + y]
        fg_color = TextColor(self.selected_color).recommendation
        style = "QLabel {background-color :" + self.selected_color + "; color : " + fg_color + ";}"
        self.ui.label_colour_new.setStyleSheet(style)
        self.ui.label_colour_new.setToolTip(_("New colour: ") + self.selected_color)
        self.ui.label_colour_new.setAutoFillBackground(True)

    def get_color(self):
        """ Get the selected color from selected table widget cell. """

        return self.selected_color

    def accept(self):
        """ Override accept button. """

        super(DialogColorSelect, self).accept()

    def fill_table(self, color_range="normal"):
        """ Twelve rows of ten columns of colours.
        normal, red weak, red blnd, green weak, green blind
        param:
        color_range: String
        """

        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        for r in range(self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(0)
        self.ui.tableWidget.setColumnCount(COLS)
        self.ui.tableWidget.setRowCount(ROWS)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.horizontalHeader().setVisible(False)
        for row in range(0, ROWS):
            self.ui.tableWidget.setRowHeight(row, 31)
            for col in range(0, COLS):
                self.ui.tableWidget.setColumnWidth(col, 52)
                code_color = colors[row * COLS + col]
                text = ""
                ttip = ""
                for c in self.used_colors:
                    if code_color == c[0]:
                        text = "*"
                        ttip += c[1] + "\n"
                item = QtWidgets.QTableWidgetItem(text)
                item.setToolTip(ttip)
                if color_range == "normal":
                    item.setBackground(QtGui.QBrush(QtGui.QColor(code_color)))
                if color_range == "red_weak":
                    item.setBackground(QtGui.QBrush(QtGui.QColor(colors_red_weak[row * COLS + col])))
                if color_range == "red_blind":
                    item.setBackground(QtGui.QBrush(QtGui.QColor(colors_red_blind[row * COLS + col])))
                    item.setToolTip("rb")
                '''if color_range == "green_weak":
                    item.setBackground(QtGui.QBrush(QtGui.QColor(colors_green_weak[row * COLS + col])))
                if color_range == "green_blind":
                    item.setBackground(QtGui.QBrush(QtGui.QColor(colors_green_blind[row * COLS + col])))'''
                item.setForeground(QtGui.QBrush(QtGui.QColor(TextColor(code_color).recommendation)))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.ui.tableWidget.setItem(row, col, item)
        self.ui.tableWidget.cellClicked.connect(self.color_selected)
