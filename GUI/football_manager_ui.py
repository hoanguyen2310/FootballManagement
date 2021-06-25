# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_football_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtChart import QChart, QChartView, QPieSeries
import matplotlib.pyplot as plt


class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.layoutVerLeft = QVBoxLayout()
        self.items = 0
        self.flag = 0
        self._data = {}
        self.lstClear = ['Xóa tất cả', 'Lựa chọn dòng']

        self.table          = QTableWidget()
        self.labelImage     = QLabel()
        self.layoutHor      = QHBoxLayout(self)
        self.layoutHLeft    = QVBoxLayout()
        self.layoutHRight   = QVBoxLayout()

        self.lineEditName   = QLineEdit()
        self.lineEditBirth  = QDateEdit()
        self.lineEditPos    = QLineEdit()
        self.lineEditClub   = QLineEdit()
        self.lineEditNumber = QLineEdit()
        self.comboBoxClear  = QComboBox()

        self.buttonAdd      = QPushButton('Thêm')
        self.buttonQuit     = QPushButton('Thoát')
        self.buttonPlot     = QPushButton('Vẽ biểu đồ')
        self.buttonEdit     = QPushButton('Bật/Tắt Chỉnh Sửa')
        self.buttonSaveImg  = QPushButton('Lưu Biểu Đồ')
        self.buttonSaveFile = QPushButton('Lưu Database')
        self.buttonClear    = QPushButton('Xóa')


        # Layout Horizontal Left
        self.layoutHorizonLeft()
        # Layout Horizontal Right
        self.layoutHorizonRight()

        self.layoutHor.addLayout(self.layoutHLeft)
        self.layoutHor.addLayout(self.layoutHRight)
        self.setLayout(self.layoutHor)

        self.fill_table()

    def layoutHorizonLeft(self):
        # Define Widget as you want
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Họ và Tên', 'Ngày Sinh', 'Vị Trí', 'Câu Lạc Bộ', 'Số Áo'))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Define Vertical Box
        layoutVerLeft = QVBoxLayout()
        # Image add Widget
        layoutVerLeft.addWidget(self.labelImage, alignment=Qt.AlignCenter)
        self.labelImage.setPixmap(QPixmap('football-manager-2021.jpg'))
        # Table add Widget
        layoutVerLeft.addWidget(self.table)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # Add Layout
        self.layoutHLeft.addLayout(layoutVerLeft)
        # Set Layout
        # self.setLayout(self.layoutHLeft)

    def layoutHorizonRight(self):
        # Define Verical Box
        layoutVerRight = QVBoxLayout()

        # Tạo combo box clear
        self.comboBoxClear.addItems(self.lstClear)
        self.comboBoxClear.setEditable(True)
        self.comboBoxClear.setFixedHeight(25)

        lineEditComboClear = self.comboBoxClear.lineEdit()
        lineEditComboClear.setAlignment(Qt.AlignCenter)
        lineEditComboClear.setReadOnly(True)

        # Cài đặt độ cao của các button
        # self.buttonAdd.setFixedHeight(25)
        # self.buttonQuit.setFixedHeight(25)
        # self.buttonPlot.setFixedHeight(25)
        # self.buttonEdit.setFixedHeight(25)
        # self.buttonSaveImg.setFixedHeight(25)
        # self.buttonSaveFile.setFixedHeight(25)
        # self.buttonClear.setFixedHeight(25)

        # Set button Thêm = False, để user nhập đầy đủ thông tin mới cho nhấn vào
        self.buttonAdd.setEnabled(False)

        # Khoảng cách giữa các khung nhập
        layoutVerRight.setSpacing(5)

        # Khung nhập thông tin
        # Họ Tên
        layoutVerRight.addWidget(QLabel('Họ và Tên'))
        layoutVerRight.addWidget(self.lineEditName)
        self.lineEditName.setMaxLength(25)
        # Năm Sinh
        layoutVerRight.addWidget(QLabel('Năm Sinh'))
        layoutVerRight.addWidget(self.lineEditBirth)
        self.lineEditBirth.setDisplayFormat("dd/MM/yyyy")
        self.lineEditBirth.setCalendarPopup(True)
        self.lineEditBirth.setMinimumDate(QDate(1900, 1, 1))
        self.lineEditBirth.setMaximumDate(QDate(2100, 1, 1))
        self.lineEditBirth.setDateTime(QtCore.QDateTime.currentDateTime())
        # Vị Trí
        layoutVerRight.addWidget(QLabel('Vị Trí'))
        layoutVerRight.addWidget(self.lineEditPos)
        self.lineEditPos.setMaxLength(20)
        # Câu Lạc Bộ
        layoutVerRight.addWidget(QLabel('Câu Lạc Bộ'))
        layoutVerRight.addWidget(self.lineEditClub)
        self.lineEditClub.setMaxLength(25)
        # Số áo
        layoutVerRight.addWidget(QLabel('Số Áo Thi Đấu'))
        layoutVerRight.addWidget(self.lineEditNumber)
        self.lineEditNumber.setValidator(QIntValidator())
        self.lineEditNumber.setMaxLength(2)

        # Nút nhấn lựa chọn chức năng
        layoutRight_AddEdit = QHBoxLayout()
        layoutRight_AddEdit.addWidget(self.buttonAdd)
        layoutRight_AddEdit.addWidget(self.buttonEdit)
        layoutRight_Clear = QHBoxLayout()
        layoutRight_Clear.addWidget(self.comboBoxClear)
        layoutRight_Clear.addWidget(self.buttonClear)
        layoutRight_PlotQuit = QHBoxLayout()
        layoutRight_PlotQuit.addWidget(self.buttonPlot)
        layoutRight_PlotQuit.addWidget(self.buttonQuit)
        layoutRight_Save = QHBoxLayout()
        layoutRight_Save.addWidget(self.buttonSaveImg)
        layoutRight_Save.addWidget(self.buttonSaveFile)

        # Set layout theo thứ tự từ trên xuống
        layoutVerRight.addLayout(layoutRight_AddEdit)
        layoutVerRight.addLayout(layoutRight_Clear)
        layoutVerRight.addLayout(layoutRight_Save)
        layoutVerRight.addLayout(layoutRight_PlotQuit)

        # chart widget
        chartView = QChartView()
        chartView.setRenderHint(QPainter.Antialiasing)
        layoutVerRight.addWidget(chartView)

        # Add Layout
        self.layoutHRight.addLayout(layoutVerRight)
        # Set Layout
        # self.setLayout(self.layoutHRight)

        self.buttonQuit.clicked.connect(self.quit_message)
        self.buttonPlot.clicked.connect(self.graph_chart)
        self.buttonAdd.clicked.connect(self.add_entry)
        self.buttonEdit.clicked.connect(self.edit_database)
        self.buttonSaveImg.clicked.connect(self.export_img)
        self.buttonSaveFile.clicked.connect(self.export_db_file)
        self.buttonClear.clicked.connect(self.comboBox_Clear)

        self.lineEditName.textChanged[str].connect(self.check_disable)
        self.lineEditPos.textChanged[str].connect(self.check_disable)
        self.lineEditClub.textChanged[str].connect(self.check_disable)
        self.lineEditNumber.textChanged.connect(self.check_disable)

    def datetime(self):
        import datetime as dt
        time_zone = dt.datetime.now()
        current_time = (time_zone.strftime("%X")).replace(":", ".")
        time_file = time_zone.strftime("_%d-" + "%m-" + "%y_" + current_time)

        return time_file

    def edit_database(self):
        if self.flag == 0:
            self.table.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
            self.flag = 1
        else:
            self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def check_disable(self):
        if self.lineEditName.text() and \
                self.lineEditPos.text() and \
                self.lineEditClub.text() and \
                self.lineEditNumber.text():
            self.buttonAdd.setEnabled(True)
        else:
            self.buttonAdd.setEnabled(False)

    def fill_table(self, data=None):
        data = self._data if not data else data
        len(self._data)
        for name, birth, position, club, number in data.items():
            nameItem = QTableWidgetItem(name)
            nameItem.setTextAlignment(Qt.AlignLeft)

            birthItem = QTableWidgetItem(birth)
            birthItem.setTextAlignment(Qt.AlignCenter)

            positionItem = QTableWidgetItem(position)
            positionItem.setTextAlignment(Qt.AlignCenter)

            clubItem = QTableWidgetItem(club)
            clubItem.setTextAlignment(Qt.AlignCenter)

            numberItem = QTableWidgetItem(number)
            numberItem.setTextAlignment(Qt.AlignCenter)

            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, nameItem)
            self.table.setItem(self.items, 1, birthItem)
            self.table.setItem(self.items, 2, positionItem)
            self.table.setItem(self.items, 3, clubItem)
            self.table.setItem(self.items, 4, numberItem)
            self.items += 1

    def add_entry(self):
        name = self.lineEditName.text()
        birth = self.lineEditBirth.text()
        position = self.lineEditPos.text()
        club = self.lineEditClub.text()
        number = self.lineEditNumber.text()

        try:
            # Add vào database table
            name = QTableWidgetItem(name)
            name.setTextAlignment(Qt.AlignCenter)
            birth = QTableWidgetItem('{}'.format(str(birth)))
            birth.setTextAlignment(Qt.AlignCenter)
            position = QTableWidgetItem(position)
            position.setTextAlignment(Qt.AlignCenter)
            club = QTableWidgetItem(club)
            club.setTextAlignment(Qt.AlignCenter)
            number = QTableWidgetItem(number)
            number.setTextAlignment(Qt.AlignCenter)

            # Thêm vào database table
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, name)
            self.table.setItem(self.items, 1, birth)
            self.table.setItem(self.items, 2, position)
            self.table.setItem(self.items, 3, club)
            self.table.setItem(self.items, 4, number)
            self.items += 1

            self.lineEditName.setText('')
            self.lineEditPos.setText('')
            self.lineEditClub.setText('')
            self.lineEditNumber.setText('')

        except ValueError:
            print("Something goes wrong")

    def clear_all_db(self):
        self.table.setRowCount(0)
        self.items = 0

        chart = QChart()
        self.chartView.setChart(chart)

    def clear_select_row(self):
        index_list = []
        if len(self.table.selectionModel().selectedRows()) > 0:
            for model_index in self.table.selectionModel().selectedRows():
                index = QtCore.QPersistentModelIndex(model_index)
                index_list.append(index)

            for index in index_list:
                self.table.removeRow(index.row())
                self.items -= 1

            if self.items <= 0:
                self.items = 0
        else:
            self.clear_all_db()

    def comboBox_Clear(self):
        if self.comboBoxClear.currentIndex() == 0:
            self.clear_all_db()
        else:
            self.clear_select_row()

    def quit_message(self, event):
        reply = QMessageBox.question(
            self, "Cảnh Báo",
            "Bạn có thực sự muốn thoát? Vui lòng lưu trước khi thoát.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        if reply == QMessageBox.Close:
            app.quit()
        elif QMessageBox.Save:
            self.export_db_file()
        else:
            pass

    def graph_chart(self):
        series = QPieSeries()

        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            val = float(self.table.item(i, 1).text().replace('$', ''))
            series.append(text, val)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignTop)
        self.chartView.setChart(chart)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Football Manager Application"))
        self.buttonThem.setText(_translate("self", "Thêm"))
        self.buttonChinhSua.setText(_translate("self", "Sửa"))
        self.buttonXoaDuLieu.setText(_translate("self", "Xóa Database"))
        self.buttonVeBieuDo.setText(_translate("self", "Vẽ Biểu Đồ"))
        self.buttonThoat.setText(_translate("self", "Thoát"))
        self.buttonXuat.setText(_translate("self", "Xuất Dữ Liệu"))

        self.FirstAndLastName.setText(_translate("self", "Họ và tên"))
        self.BirthDayName.setText(_translate("self", "Ngày tháng năm sinh"))
        self.PositionName.setText(_translate("self", "Vị trí"))
        self.ClubName.setText(_translate("self", "Đội tuyển"))

        self.copyright.setText(_translate("self", "Copyright © 2021 by Hoa Nguyen | All Rights Reserved."))

    def export_db_file(self):
        import pandas as pd
        flag_db_save = False
        try:
            if self.table.rowCount() > 0:
                my_dict = {self.table.horizontalHeaderItem(0).text(): [],
                           self.table.horizontalHeaderItem(1).text(): [],
                           self.table.horizontalHeaderItem(2).text(): [],
                           self.table.horizontalHeaderItem(3).text(): [],
                           self.table.horizontalHeaderItem(4).text(): []}

                for columnNumber in range(self.table.columnCount()):
                    for rowNumber in range(self.table.rowCount()):
                        my_dict[self.table.horizontalHeaderItem(columnNumber).text()].append(
                            self.table.item(rowNumber, columnNumber).text())
                df = pd.DataFrame(my_dict, columns=[self.table.horizontalHeaderItem(0).text(),
                                                    self.table.horizontalHeaderItem(1).text(),
                                                    self.table.horizontalHeaderItem(2).text(),
                                                    self.table.horizontalHeaderItem(3).text(),
                                                    self.table.horizontalHeaderItem(4).text()])
                time_file = self.datetime()
                f_name = "export_database" + time_file
                ext = ".csv"
                path_file = f_name + ext
                df.to_csv(path_file, encoding='utf-8', index=False, header=True)
                flag_db_save = True

        finally:
            self.showMsg(flag_db_save)

    def export_img(self):
        time_file = self.datetime()
        f_name = "export_image" + time_file
        ext = ".png"
        path_file = f_name + ext
        plt.savefig(path_file)

    def showMsg(self, flag=True):
        if flag:
            QMessageBox.about(self, "Save Complete", "Tập tin của bạn đã save hoàn tất.")
        else:
            QMessageBox.warning(self, "Error", "Tập tin của bạn chưa được save.")


class MainWindow(QMainWindow):
    def __init__(self, w):
        super().__init__()

        self.setWindowTitle('Football Manager Application')
        self.resize(1000, 720)

        # Menu Bar
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('File')

        # export to csv file action
        exportDbAction = QAction('Export to CSV', self)
        exportDbAction.setShortcut('Ctrl+E')
        exportDbAction.triggered.connect(self.export_db_file)

        # export to csv file action
        exportImgAction = QAction('Export Image', self)
        exportImgAction.setShortcut('Ctrl+I')
        exportImgAction.triggered.connect(self.export_img)

        # exit action
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.quit_message)

        self.fileMenu.addAction(exportImgAction)
        self.fileMenu.addAction(exportDbAction)
        self.fileMenu.addAction(exitAction)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHoiDap = QtWidgets.QMenu(self.menubar)
        self.menuHoiDap.setObjectName("menuHoiDap")
        self.menuBieuDo = QtWidgets.QMenu(self.menubar)
        self.menuBieuDo.setObjectName("menuBieuDo")
        self.menuTroGiup = QtWidgets.QMenu(self.menubar)
        self.menuTroGiup.setObjectName("menuTroGiup")
        self.setMenuBar(self.menubar)
        # Action thêm xóa sửa
        self.actionThem = QtWidgets.QAction(self)
        self.actionThem.setObjectName("actionThem")
        self.actionThem.setEnabled(False)

        self.actionXoa = QtWidgets.QAction(self)
        self.actionXoa.setObjectName("actionXoa")

        self.actionSua = QtWidgets.QAction(self)
        self.actionSua.setObjectName("actionSua")
        self.actionSua.setEnabled(False)

        self.actionExportImg = QtWidgets.QAction(self)
        self.actionExportImg.setObjectName("actionExportImg")

        self.actionExportDb = QtWidgets.QAction(self)
        self.actionExportDb.setObjectName("actionExportDb")

        # Action thoát
        self.actionThoat = QtWidgets.QAction(self)
        self.actionThoat.setObjectName("actionThoat")
        # Action câu hỏi
        self.actionCauHoi = QtWidgets.QAction(self)
        self.actionCauHoi.setObjectName("actionCauHoi")
        # Action vẽ biểu đồ
        self.actionVeBieuDo = QtWidgets.QAction(self)
        self.actionVeBieuDo.setObjectName("actionVeBieuDo")
        # Action xuất dữ liệu
        self.actionXuatDuLieu = QtWidgets.QAction(self)
        self.actionXuatDuLieu.setObjectName("actionXuatDuLieu")
        # Action liên hệ
        self.actionLienHe = QtWidgets.QAction(self)
        self.actionLienHe.setObjectName("actionLienHe")

        # Trong menu, add các action bên trên
        # menu file
        self.menuFile.addAction(self.actionThem)
        self.menuFile.addAction(self.actionSua)
        self.menuFile.addAction(self.actionXoa)
        self.menuFile.addAction(self.actionExportImg)
        self.menuFile.addAction(self.actionExportDb)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionThoat)
        # menu hỏi đáp
        self.menuHoiDap.addAction(self.actionCauHoi)
        # menu biểu đồ
        self.menuBieuDo.addAction(self.actionVeBieuDo)
        # Menu trợ giúp
        self.menuTroGiup.addAction(self.actionLienHe)

        # Add action cho tiêu đề menu gồm File, hỏi đáp, biểu đồ và trợ giúp
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHoiDap.menuAction())
        self.menubar.addAction(self.menuBieuDo.menuAction())
        self.menubar.addAction(self.menuTroGiup.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # tạo connection tới những chỗ ta click vào
        self.actionThem.triggered.connect(self.add_entry)
        self.actionXoa.triggered.connect(self.clear_all_db)
        self.actionSua.triggered.connect(lambda: self.clicked("Sửa was clicked"))
        self.actionCauHoi.triggered.connect(self.question_answer)
        self.actionLienHe.triggered.connect(self.contact)
        self.actionVeBieuDo.triggered.connect(self.draw_chart)

        self.setCentralWidget(w)

    def question_answer(self):
        import pandas as pd
        cauthu_df = pd.read_csv('ds_cauthu.csv')
        # print("danh sach cau thu")
        # print(cauthu_df)
        # ## Truy van cau thu
        # ## Hoi dap co dieu kien
        # dotuoi = int(input("Cho moc tuoi"))
        # cauthu_gia = cauthu_df[cauthu_df['tuoi'] > dotuoi]
        # print("Cau thu lão tướng tuổi > " + str(dotuoi))
        # print(cauthu_gia)
        # ### cau thu tre
        # cauthu_gia = cauthu_df[cauthu_df['tuoi'] <= dotuoi]
        # print("Cau thu trẻ <= " + str(dotuoi))
        # print(cauthu_gia)
        pass

    def contact(self):
        info = QMessageBox(self)
        # info.setIconPixmap(QPixmap("C:/Users/ThuongLe.LETHUONG/PycharmProjects/FootballManagement/GUI/New_Ronaldo.png"))
        info.setWindowTitle("Contact Information")
        info.setText("Football Manager là phần mềm quản lý cầu thủ\n"
                     "Phần mềm đang trong giai đoạn thử nghiệm\n\n"
                     "---------------------------------------------")
        info.setInformativeText("Mọi chi tiết xin vui lòng liên hệ:"
                                "\nThành viên dự án Football Manager:"
                                "\n\tNguyễn Lê Minh Hòa"
                                "\n\tSđt liên hệ: 0944 886 896")
        info.autoFillBackground()
        info.setIcon(QMessageBox.Information)
        info.setStandardButtons(QMessageBox.Close)
        info.setDefaultButton(QMessageBox.Close)

        x = info.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.menuFile.setTitle(_translate("self", "File"))
        self.menuHoiDap.setTitle(_translate("self", "Hỏi Đáp"))
        self.menuBieuDo.setTitle(_translate("self", "Biểu Đồ"))
        self.menuTroGiup.setTitle(_translate("self", "Trợ Giúp"))

        self.actionThem.setText(_translate("self", "Thêm"))
        self.actionXoa.setText(_translate("self", "Xóa"))
        self.actionSua.setText(_translate("self", "Sửa"))
        self.actionCauHoi.setText(_translate("self", "Chọn câu hỏi"))
        self.actionVeBieuDo.setText(_translate("self", "Chọn Biểu Đồ"))
        self.actionXuatDuLieu.setText(_translate("self", "Xuất Dữ Liệu"))
        self.actionThoat.setText(_translate("self", "Thoát"))
        self.actionThoat.setShortcut('Ctrl+Q')
        self.actionThoat.triggered.connect(self.quit_message)

        self.actionLienHe.setText(_translate("self", "Liên hệ"))

        # Tạo shorcut action Thêm/Xóa/Sửa
        self.actionThem.setText(_translate("MainWindow", "Thêm"))
        self.actionThem.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionThem.triggered.connect(DataEntryForm.add_entry)

        self.actionXoa.setText(_translate("MainWindow", "Xóa"))
        self.actionXoa.setShortcut(_translate("MainWindow", "Ctrl+D"))

        self.actionSua.setText(_translate("MainWindow", "Sửa"))
        self.actionSua.setShortcut(_translate("MainWindow", "Ctrl+E"))

        self.actionExportDb.setText(_translate("MainWindow", "Xuất File"))

        self.actionExportImg.setText(_translate("MainWindow", "Xuất Biểu Đồ"))

    def export_db_file(self):
        import pandas as pd
        my_dict = {w.table.horizontalHeaderItem(0).text(): [],
                   w.table.horizontalHeaderItem(1).text(): [],
                   w.table.horizontalHeaderItem(2).text(): [],
                   w.table.horizontalHeaderItem(3).text(): [],
                   w.table.horizontalHeaderItem(4).text(): []}
        for columnNumber in range(w.table.columnCount() - 1):
            for rowNumber in range(w.table.rowCount()):
                my_dict[w.table.horizontalHeaderItem(columnNumber).text()].append(
                    w.table.item(rowNumber, columnNumber).text())
        df = pd.DataFrame(my_dict, columns=[w.table.horizontalHeaderItem(0).text(),
                                            w.table.horizontalHeaderItem(1).text(),
                                            w.table.horizontalHeaderItem(2).text(),
                                            w.table.horizontalHeaderItem(3).text(),
                                            w.table.horizontalHeaderItem(4).text()])

        time_file = self.datetime()
        f_name = "export_database" + time_file
        ext = ".csv"
        path_file = f_name + ext

        df.to_csv(path_file, encoding='utf-8', index=False, header=True)

    def export_img(self):
        time_file = self.datetime()
        f_name = "export_image" + time_file
        ext = ".png"
        path_file = f_name + ext
        plt.savefig(path_file)

    def fill_table(self, data=None):
        data = self._data if not data else data
        len(self._data)
        for name, birth, position, club, number in data.items():
            nameItem = QTableWidgetItem(name)
            nameItem.setTextAlignment(Qt.AlignLeft)

            birthItem = QTableWidgetItem(birth)
            birthItem.setTextAlignment(Qt.AlignCenter)

            positionItem = QTableWidgetItem(position)
            positionItem.setTextAlignment(Qt.AlignCenter)

            clubItem = QTableWidgetItem(club)
            clubItem.setTextAlignment(Qt.AlignCenter)

            numberItem = QTableWidgetItem(number)
            numberItem.setTextAlignment(Qt.AlignCenter)

            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, nameItem)
            self.table.setItem(self.items, 1, birthItem)
            self.table.setItem(self.items, 2, positionItem)
            self.table.setItem(self.items, 3, clubItem)
            self.table.setItem(self.items, 4, numberItem)
            self.items += 1

    def add_entry(self):
        name = self.lineEditName.text()
        birth = self.lineEditBirth.text()
        position = self.lineEditPos.text()
        club = self.lineEditClub.text()
        number = self.lineEditNumber.text()

        try:
            # Add vào database table
            name = QTableWidgetItem(name)
            name.setTextAlignment(Qt.AlignCenter)
            birth = QTableWidgetItem('{}'.format(str(birth)))
            birth.setTextAlignment(Qt.AlignCenter)
            position = QTableWidgetItem(position)
            position.setTextAlignment(Qt.AlignCenter)
            club = QTableWidgetItem(club)
            club.setTextAlignment(Qt.AlignCenter)
            number = QTableWidgetItem(number)
            number.setTextAlignment(Qt.AlignCenter)

            # Thêm vào database table
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, name)
            self.table.setItem(self.items, 1, birth)
            self.table.setItem(self.items, 2, position)
            self.table.setItem(self.items, 3, club)
            self.table.setItem(self.items, 4, number)
            self.items += 1

            self.lineEditName.setText('')
            self.lineEditPos.setText('')
            self.lineEditClub.setText('')
            self.lineEditNumber.setText('')

        except ValueError:
            print("Something goes wrong")

    def clear_all_db(self):
        self.table.setRowCount(0)
        self.items = 0

        chart = QChart()
        self.chartView.setChart(chart)

    def quit_message(self, event):
        reply = QMessageBox.question(
            self, "Cảnh Báo",
            "Bạn có thực sự muốn thoát? Vui lòng lưu trước khi thoát.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        if reply == QMessageBox.Close:
            app.quit()

    def draw_chart(self):
        series = QPieSeries()

        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            val = float(self.table.item(i, 1).text().replace('$', ''))
            series.append(text, val)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignTop)
        self.chartView.setChart(chart)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = DataEntryForm()
    main = MainWindow(w)
    main.show()

    sys.exit(app.exec_())

# remaning menu bar and draw bieu do and save database