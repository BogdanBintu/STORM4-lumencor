# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hal4000-detached.ui'
#
# Created: Fri Jul 24 07:45:30 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(240, 822)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(240, 0))
        MainWindow.setMaximumSize(QtCore.QSize(240, 10000))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../HAL-4000.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 10000))
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.settingsGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.settingsGroupBox.setMinimumSize(QtCore.QSize(50, 40))
        self.settingsGroupBox.setMaximumSize(QtCore.QSize(231, 16777215))
        self.settingsGroupBox.setObjectName(_fromUtf8("settingsGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.settingsGroupBox)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.settingsScrollArea = QtGui.QScrollArea(self.settingsGroupBox)
        self.settingsScrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setObjectName(_fromUtf8("settingsScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 210, 170))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.settingsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.settingsScrollArea, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.settingsGroupBox)
        self.filmGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filmGroupBox.sizePolicy().hasHeightForWidth())
        self.filmGroupBox.setSizePolicy(sizePolicy)
        self.filmGroupBox.setMinimumSize(QtCore.QSize(150, 261))
        self.filmGroupBox.setObjectName(_fromUtf8("filmGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.filmGroupBox)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.shuttersLabels = QtGui.QLabel(self.filmGroupBox)
        self.shuttersLabels.setObjectName(_fromUtf8("shuttersLabels"))
        self.verticalLayout_2.addWidget(self.shuttersLabels)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.widget = QtGui.QWidget(self.filmGroupBox)
        self.widget.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_9.addWidget(self.widget)
        self.shuttersText = QtGui.QLabel(self.filmGroupBox)
        self.shuttersText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shuttersText.setObjectName(_fromUtf8("shuttersText"))
        self.horizontalLayout_9.addWidget(self.shuttersText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.directoryLabel = QtGui.QLabel(self.filmGroupBox)
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.verticalLayout_2.addWidget(self.directoryLabel)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.widget_2 = QtGui.QWidget(self.filmGroupBox)
        self.widget_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_10.addWidget(self.widget_2)
        self.directoryText = QtGui.QLabel(self.filmGroupBox)
        self.directoryText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.directoryText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.directoryText.setObjectName(_fromUtf8("directoryText"))
        self.horizontalLayout_10.addWidget(self.directoryText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.autoIncCheckBox = QtGui.QCheckBox(self.filmGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoIncCheckBox.sizePolicy().hasHeightForWidth())
        self.autoIncCheckBox.setSizePolicy(sizePolicy)
        self.autoIncCheckBox.setChecked(True)
        self.autoIncCheckBox.setObjectName(_fromUtf8("autoIncCheckBox"))
        self.verticalLayout_2.addWidget(self.autoIncCheckBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filenameEdit = QtGui.QLineEdit(self.filmGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.horizontalLayout.addWidget(self.filenameEdit)
        self.indexSpinBox = QtGui.QSpinBox(self.filmGroupBox)
        self.indexSpinBox.setMaximumSize(QtCore.QSize(55, 16777215))
        self.indexSpinBox.setMinimum(1)
        self.indexSpinBox.setMaximum(9999)
        self.indexSpinBox.setObjectName(_fromUtf8("indexSpinBox"))
        self.horizontalLayout.addWidget(self.indexSpinBox)
        self.extensionComboBox = QtGui.QComboBox(self.filmGroupBox)
        self.extensionComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extensionComboBox.setObjectName(_fromUtf8("extensionComboBox"))
        self.horizontalLayout.addWidget(self.extensionComboBox)
        self.filetypeComboBox = QtGui.QComboBox(self.filmGroupBox)
        self.filetypeComboBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.filetypeComboBox.setObjectName(_fromUtf8("filetypeComboBox"))
        self.horizontalLayout.addWidget(self.filetypeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.widget_3 = QtGui.QWidget(self.filmGroupBox)
        self.widget_3.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_11.addWidget(self.widget_3)
        self.filenameLabel = QtGui.QLabel(self.filmGroupBox)
        self.filenameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.horizontalLayout_11.addWidget(self.filenameLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.modeLabel = QtGui.QLabel(self.filmGroupBox)
        self.modeLabel.setObjectName(_fromUtf8("modeLabel"))
        self.horizontalLayout_4.addWidget(self.modeLabel)
        self.modeComboBox = QtGui.QComboBox(self.filmGroupBox)
        self.modeComboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.modeComboBox.setObjectName(_fromUtf8("modeComboBox"))
        self.modeComboBox.addItem(_fromUtf8(""))
        self.modeComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.modeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lengthLabel = QtGui.QLabel(self.filmGroupBox)
        self.lengthLabel.setObjectName(_fromUtf8("lengthLabel"))
        self.horizontalLayout_5.addWidget(self.lengthLabel)
        self.lengthSpinBox = QtGui.QSpinBox(self.filmGroupBox)
        self.lengthSpinBox.setMaximum(1000000)
        self.lengthSpinBox.setObjectName(_fromUtf8("lengthSpinBox"))
        self.horizontalLayout_5.addWidget(self.lengthSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.framesLabel = QtGui.QLabel(self.filmGroupBox)
        self.framesLabel.setObjectName(_fromUtf8("framesLabel"))
        self.horizontalLayout_6.addWidget(self.framesLabel)
        self.framesText = QtGui.QLabel(self.filmGroupBox)
        self.framesText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.framesText.setObjectName(_fromUtf8("framesText"))
        self.horizontalLayout_6.addWidget(self.framesText)
        self.sizeLabel = QtGui.QLabel(self.filmGroupBox)
        self.sizeLabel.setObjectName(_fromUtf8("sizeLabel"))
        self.horizontalLayout_6.addWidget(self.sizeLabel)
        self.sizeText = QtGui.QLabel(self.filmGroupBox)
        self.sizeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sizeText.setObjectName(_fromUtf8("sizeText"))
        self.horizontalLayout_6.addWidget(self.sizeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.autoShuttersCheckBox = QtGui.QCheckBox(self.filmGroupBox)
        self.autoShuttersCheckBox.setChecked(True)
        self.autoShuttersCheckBox.setObjectName(_fromUtf8("autoShuttersCheckBox"))
        self.horizontalLayout_7.addWidget(self.autoShuttersCheckBox)
        self.saveMovieCheckBox = QtGui.QCheckBox(self.filmGroupBox)
        self.saveMovieCheckBox.setChecked(True)
        self.saveMovieCheckBox.setObjectName(_fromUtf8("saveMovieCheckBox"))
        self.horizontalLayout_7.addWidget(self.saveMovieCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addWidget(self.filmGroupBox)
        self.mosaicGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.mosaicGroupBox.setObjectName(_fromUtf8("mosaicGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mosaicGroupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.objectiveLabel = QtGui.QLabel(self.mosaicGroupBox)
        self.objectiveLabel.setObjectName(_fromUtf8("objectiveLabel"))
        self.horizontalLayout_8.addWidget(self.objectiveLabel)
        self.objectiveText = QtGui.QLabel(self.mosaicGroupBox)
        self.objectiveText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.objectiveText.setObjectName(_fromUtf8("objectiveText"))
        self.horizontalLayout_8.addWidget(self.objectiveText)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.mosaicGroupBox)
        self.notesGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesGroupBox.sizePolicy().hasHeightForWidth())
        self.notesGroupBox.setSizePolicy(sizePolicy)
        self.notesGroupBox.setMinimumSize(QtCore.QSize(50, 200))
        self.notesGroupBox.setMaximumSize(QtCore.QSize(231, 200))
        self.notesGroupBox.setObjectName(_fromUtf8("notesGroupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.notesGroupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.notesEdit = QtGui.QTextEdit(self.notesGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesEdit.sizePolicy().hasHeightForWidth())
        self.notesEdit.setSizePolicy(sizePolicy)
        self.notesEdit.setMinimumSize(QtCore.QSize(20, 37))
        self.notesEdit.setMaximumSize(QtCore.QSize(10000, 10000))
        self.notesEdit.setObjectName(_fromUtf8("notesEdit"))
        self.horizontalLayout_3.addWidget(self.notesEdit)
        self.verticalLayout_3.addWidget(self.notesGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionShutter = QtGui.QAction(MainWindow)
        self.actionShutter.setObjectName(_fromUtf8("actionShutter"))
        self.actionDirectory = QtGui.QAction(MainWindow)
        self.actionDirectory.setObjectName(_fromUtf8("actionDirectory"))
        self.actionIllumination = QtGui.QAction(MainWindow)
        self.actionIllumination.setObjectName(_fromUtf8("actionIllumination"))
        self.actionStage = QtGui.QAction(MainWindow)
        self.actionStage.setObjectName(_fromUtf8("actionStage"))
        self.actionFocus_Lock = QtGui.QAction(MainWindow)
        self.actionFocus_Lock.setObjectName(_fromUtf8("actionFocus_Lock"))
        self.actionSpot_Counter = QtGui.QAction(MainWindow)
        self.actionSpot_Counter.setObjectName(_fromUtf8("actionSpot_Counter"))
        self.actionSwitch_Test = QtGui.QAction(MainWindow)
        self.actionSwitch_Test.setObjectName(_fromUtf8("actionSwitch_Test"))
        self.actionMisc_Controls = QtGui.QAction(MainWindow)
        self.actionMisc_Controls.setObjectName(_fromUtf8("actionMisc_Controls"))
        self.actionProgression = QtGui.QAction(MainWindow)
        self.actionProgression.setObjectName(_fromUtf8("actionProgression"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionShutter)
        self.menuFile.addAction(self.actionDirectory)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HAL-4000", None))
        self.settingsGroupBox.setTitle(_translate("MainWindow", "Settings", None))
        self.filmGroupBox.setTitle(_translate("MainWindow", "Film", None))
        self.shuttersLabels.setText(_translate("MainWindow", "Shutter Sequence:", None))
        self.shuttersText.setText(_translate("MainWindow", "asdf", None))
        self.directoryLabel.setText(_translate("MainWindow", "Directory:", None))
        self.directoryText.setText(_translate("MainWindow", "asdf", None))
        self.autoIncCheckBox.setText(_translate("MainWindow", "Increment Automatically", None))
        self.filenameLabel.setText(_translate("MainWindow", "asdf", None))
        self.modeLabel.setText(_translate("MainWindow", "Mode:", None))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "Run Till Abort", None))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "Fixed Length", None))
        self.lengthLabel.setText(_translate("MainWindow", "Length:", None))
        self.framesLabel.setText(_translate("MainWindow", "Frames:", None))
        self.framesText.setText(_translate("MainWindow", "asdf", None))
        self.sizeLabel.setText(_translate("MainWindow", "Size:", None))
        self.sizeText.setText(_translate("MainWindow", "asdf", None))
        self.autoShuttersCheckBox.setText(_translate("MainWindow", "Run Shutters", None))
        self.saveMovieCheckBox.setText(_translate("MainWindow", "Save Movie", None))
        self.mosaicGroupBox.setTitle(_translate("MainWindow", "Mosaic", None))
        self.objectiveLabel.setText(_translate("MainWindow", "Objective:", None))
        self.objectiveText.setText(_translate("MainWindow", "asdf", None))
        self.notesGroupBox.setTitle(_translate("MainWindow", "Notes", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionSettings.setText(_translate("MainWindow", "New Settings", None))
        self.actionShutter.setText(_translate("MainWindow", "New Shutter Sequence", None))
        self.actionDirectory.setText(_translate("MainWindow", "Set Working Directory", None))
        self.actionIllumination.setText(_translate("MainWindow", "Illumination", None))
        self.actionStage.setText(_translate("MainWindow", "Stage", None))
        self.actionFocus_Lock.setText(_translate("MainWindow", "Focus Lock", None))
        self.actionSpot_Counter.setText(_translate("MainWindow", "Spot Counter", None))
        self.actionSwitch_Test.setText(_translate("MainWindow", "Switch Test", None))
        self.actionMisc_Controls.setText(_translate("MainWindow", "Misc. Controls", None))
        self.actionProgression.setText(_translate("MainWindow", "Progressions", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))

