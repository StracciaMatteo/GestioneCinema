from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HOME(object):
    def setupUi(self, HOME):
        HOME.setObjectName("HOME")
        HOME.resize(1075, 594)
        with open("images/stile.qss", "r") as style:
                HOME.setStyleSheet(style.read())
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(HOME)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Titolo = QtWidgets.QLabel(HOME)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titolo.sizePolicy().hasHeightForWidth())
        self.Titolo.setSizePolicy(sizePolicy)
        self.Titolo.setMinimumSize(QtCore.QSize(1055, 100))
        self.Titolo.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Titolo.setFont(font)
        self.Titolo.setStyleSheet("color: rgb(92, 164, 144);")
        self.Titolo.setObjectName("Titolo")
        self.verticalLayout_6.addWidget(self.Titolo)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(HOME)
        self.groupBox_4.setMinimumSize(QtCore.QSize(524, 193))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(0, -10, 61, 41))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/biglietto.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 40, 431, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnAccedi = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi.sizePolicy().hasHeightForWidth())
        self.btnAccedi.setSizePolicy(sizePolicy)
        self.btnAccedi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi.setStyleSheet("")
        self.btnAccedi.setObjectName("btnAccedi")
        self.horizontalLayout_4.addWidget(self.btnAccedi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnAccedi_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_2.sizePolicy().hasHeightForWidth())
        self.btnAccedi_2.setSizePolicy(sizePolicy)
        self.btnAccedi_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_2.setStyleSheet("")
        self.btnAccedi_2.setObjectName("btnAccedi_2")
        self.horizontalLayout_3.addWidget(self.btnAccedi_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.groupBox_3 = QtWidgets.QGroupBox(HOME)
        self.groupBox_3.setMinimumSize(QtCore.QSize(525, 193))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/Ingranaggio.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 40, 431, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnAccedi_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_4.sizePolicy().hasHeightForWidth())
        self.btnAccedi_4.setSizePolicy(sizePolicy)
        self.btnAccedi_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_4.setStyleSheet("")
        self.btnAccedi_4.setObjectName("btnAccedi_4")
        self.horizontalLayout.addWidget(self.btnAccedi_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.btnAccedi_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_3.sizePolicy().hasHeightForWidth())
        self.btnAccedi_3.setSizePolicy(sizePolicy)
        self.btnAccedi_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_3.setStyleSheet("")
        self.btnAccedi_3.setObjectName("btnAccedi_3")
        self.horizontalLayout_2.addWidget(self.btnAccedi_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.groupBox = QtWidgets.QGroupBox(HOME)
        self.groupBox.setMinimumSize(QtCore.QSize(525, 269))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/dipendente.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 40, 431, 201))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.btnAccedi_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_5.sizePolicy().hasHeightForWidth())
        self.btnAccedi_5.setSizePolicy(sizePolicy)
        self.btnAccedi_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_5.setStyleSheet("")
        self.btnAccedi_5.setObjectName("btnAccedi_5")
        self.horizontalLayout_8.addWidget(self.btnAccedi_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.btnAccedi_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_6.sizePolicy().hasHeightForWidth())
        self.btnAccedi_6.setSizePolicy(sizePolicy)
        self.btnAccedi_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_6.setStyleSheet("")
        self.btnAccedi_6.setObjectName("btnAccedi_6")
        self.horizontalLayout_9.addWidget(self.btnAccedi_6)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.btnAccedi_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_7.sizePolicy().hasHeightForWidth())
        self.btnAccedi_7.setSizePolicy(sizePolicy)
        self.btnAccedi_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_7.setStyleSheet("")
        self.btnAccedi_7.setObjectName("btnAccedi_7")
        self.horizontalLayout_10.addWidget(self.btnAccedi_7)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.gridLayout_4.addWidget(self.groupBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.groupBox_2 = QtWidgets.QGroupBox(HOME)
        self.groupBox_2.setMinimumSize(QtCore.QSize(524, 269))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/euro.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 431, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.btnAccedi_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_8.sizePolicy().hasHeightForWidth())
        self.btnAccedi_8.setSizePolicy(sizePolicy)
        self.btnAccedi_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_8.setStyleSheet("")
        self.btnAccedi_8.setObjectName("btnAccedi_8")
        self.horizontalLayout_5.addWidget(self.btnAccedi_8)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.btnAccedi_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_9.sizePolicy().hasHeightForWidth())
        self.btnAccedi_9.setSizePolicy(sizePolicy)
        self.btnAccedi_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_9.setStyleSheet("")
        self.btnAccedi_9.setObjectName("btnAccedi_9")
        self.horizontalLayout_7.addWidget(self.btnAccedi_9)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.btnAccedi_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAccedi_10.sizePolicy().hasHeightForWidth())
        self.btnAccedi_10.setSizePolicy(sizePolicy)
        self.btnAccedi_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAccedi_10.setStyleSheet("")
        self.btnAccedi_10.setObjectName("btnAccedi_10")
        self.horizontalLayout_6.addWidget(self.btnAccedi_10)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Italian, QtCore.QLocale.Italy))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addLayout(self.gridLayout_4)

        self.retranslateUi(HOME)
        QtCore.QMetaObject.connectSlotsByName(HOME)

    def retranslateUi(self, HOME):
        _translate = QtCore.QCoreApplication.translate
        HOME.setWindowTitle(_translate("HOME", "HOME"))
        self.Titolo.setText(_translate("HOME", "Benvenuto nella Home, da qui puoi accedere a tutti i servizi disponibili"))
        self.groupBox_4.setTitle(_translate("HOME", "         Gestione biglietteria"))
        self.btnAccedi.setText(_translate("HOME", "Vendita biglietti"))
        self.btnAccedi_2.setText(_translate("HOME", "Rimborso biglietti"))
        self.label_3.setText(_translate("HOME", "In questa sezione è possibile vendere biglietti ai clienti ed eventualmente rimborsarli. Queste operazioni possono essere effettuate solo in determinate fasce orarie"))
        self.groupBox_3.setTitle(_translate("HOME", "    Gestione attività"))
        self.btnAccedi_4.setText(_translate("HOME", "Inserimento film"))
        self.btnAccedi_3.setText(_translate("HOME", "Visualizza programmazione"))
        self.label_2.setText(_translate("HOME", "In questa sezione è possibile inserire un film nel sistema, assegnare degli spettacoli ad un film e visualizzare e modificare la programmazione"))
        self.groupBox.setTitle(_translate("HOME", "     Gestione dipendenti"))
        self.btnAccedi_5.setText(_translate("HOME", "Inserimento dipendente"))
        self.btnAccedi_6.setText(_translate("HOME", "Lista dipendenti"))
        self.btnAccedi_7.setText(_translate("HOME", "Turni di lavoro"))
        self.label_5.setText(_translate("HOME", "In questa sezione, riservata solo all\'amministratore del cinema, si possono inserire nuovi dipendenti, vedere la lista di quelli attuali per eventualmente modificare i loro dati. Si possono inoltre visualizzare i turni di lavoro"))
        self.groupBox_2.setTitle(_translate("HOME", "    Gestione economica"))
        self.btnAccedi_8.setText(_translate("HOME", "Inserisci spesa/ricavo"))
        self.btnAccedi_9.setText(_translate("HOME", "Visualizza movimenti"))
        self.btnAccedi_10.setText(_translate("HOME", "Visualizza statistiche"))
        self.label_4.setText(_translate("HOME", "In questa sezione è possibile inserire le spese e i ricavi per poter tenere traccia dei movimenti contabili dell\'attivià. E\' inoltre possibile visualizzare statistiche sull\'andamento delle vendite e gli incassi per poter ottimizzare i profitti."))
