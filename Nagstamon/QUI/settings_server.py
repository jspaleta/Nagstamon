# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_server.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settings_server(object):
    def setupUi(self, settings_server):
        settings_server.setObjectName("settings_server")
        settings_server.resize(659, 717)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_server.sizePolicy().hasHeightForWidth())
        settings_server.setSizePolicy(sizePolicy)
        settings_server.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(settings_server)
        self.gridLayout.setObjectName("gridLayout")
        self.label_password = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 8, 0, 1, 1)
        self.input_lineedit_monitor_url = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_monitor_url.setInputMask("")
        self.input_lineedit_monitor_url.setObjectName("input_lineedit_monitor_url")
        self.gridLayout.addWidget(self.input_lineedit_monitor_url, 4, 2, 1, 2)
        self.label_name = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 3, 0, 1, 1)
        self.input_lineedit_username = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_username.setObjectName("input_lineedit_username")
        self.gridLayout.addWidget(self.input_lineedit_username, 6, 2, 1, 1)
        self.input_lineedit_monitor_cgi_url = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_monitor_cgi_url.setObjectName("input_lineedit_monitor_cgi_url")
        self.gridLayout.addWidget(self.input_lineedit_monitor_cgi_url, 5, 2, 1, 2)
        self.input_lineedit_password = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_lineedit_password.setObjectName("input_lineedit_password")
        self.gridLayout.addWidget(self.input_lineedit_password, 8, 2, 1, 1)
        self.input_combobox_type = QtWidgets.QComboBox(settings_server)
        self.input_combobox_type.setObjectName("input_combobox_type")
        self.gridLayout.addWidget(self.input_combobox_type, 1, 2, 1, 1)
        self.input_checkbox_use_proxy = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_use_proxy.setObjectName("input_checkbox_use_proxy")
        self.gridLayout.addWidget(self.input_checkbox_use_proxy, 15, 0, 1, 1)
        self.input_checkbox_use_autologin = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_use_autologin.setObjectName("input_checkbox_use_autologin")
        self.gridLayout.addWidget(self.input_checkbox_use_autologin, 10, 0, 1, 3)
        self.input_checkbox_use_display_name_host = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_use_display_name_host.setObjectName("input_checkbox_use_display_name_host")
        self.gridLayout.addWidget(self.input_checkbox_use_display_name_host, 21, 0, 1, 3)
        self.proxy_groupbox = QtWidgets.QGroupBox(settings_server)
        self.proxy_groupbox.setObjectName("proxy_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.proxy_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_proxy_password = QtWidgets.QLabel(self.proxy_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_password.sizePolicy().hasHeightForWidth())
        self.label_proxy_password.setSizePolicy(sizePolicy)
        self.label_proxy_password.setObjectName("label_proxy_password")
        self.gridLayout_2.addWidget(self.label_proxy_password, 3, 0, 1, 1)
        self.label_proxy_username = QtWidgets.QLabel(self.proxy_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_username.sizePolicy().hasHeightForWidth())
        self.label_proxy_username.setSizePolicy(sizePolicy)
        self.label_proxy_username.setObjectName("label_proxy_username")
        self.gridLayout_2.addWidget(self.label_proxy_username, 2, 0, 1, 1)
        self.input_lineedit_proxy_username = QtWidgets.QLineEdit(self.proxy_groupbox)
        self.input_lineedit_proxy_username.setObjectName("input_lineedit_proxy_username")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_username, 2, 1, 1, 1)
        self.input_lineedit_proxy_address = QtWidgets.QLineEdit(self.proxy_groupbox)
        self.input_lineedit_proxy_address.setObjectName("input_lineedit_proxy_address")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_address, 1, 1, 1, 1)
        self.label_proxy_address = QtWidgets.QLabel(self.proxy_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_proxy_address.sizePolicy().hasHeightForWidth())
        self.label_proxy_address.setSizePolicy(sizePolicy)
        self.label_proxy_address.setObjectName("label_proxy_address")
        self.gridLayout_2.addWidget(self.label_proxy_address, 1, 0, 1, 1)
        self.input_lineedit_proxy_password = QtWidgets.QLineEdit(self.proxy_groupbox)
        self.input_lineedit_proxy_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_lineedit_proxy_password.setObjectName("input_lineedit_proxy_password")
        self.gridLayout_2.addWidget(self.input_lineedit_proxy_password, 3, 1, 1, 1)
        self.input_checkbox_use_proxy_from_os = QtWidgets.QCheckBox(self.proxy_groupbox)
        self.input_checkbox_use_proxy_from_os.setObjectName("input_checkbox_use_proxy_from_os")
        self.gridLayout_2.addWidget(self.input_checkbox_use_proxy_from_os, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.proxy_groupbox, 16, 0, 1, 4)
        self.button_box = QtWidgets.QDialogButtonBox(settings_server)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 25, 3, 1, 1)
        self.label_autologin_key = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_autologin_key.sizePolicy().hasHeightForWidth())
        self.label_autologin_key.setSizePolicy(sizePolicy)
        self.label_autologin_key.setObjectName("label_autologin_key")
        self.gridLayout.addWidget(self.label_autologin_key, 11, 0, 1, 1)
        self.label_server_type = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_server_type.sizePolicy().hasHeightForWidth())
        self.label_server_type.setSizePolicy(sizePolicy)
        self.label_server_type.setObjectName("label_server_type")
        self.gridLayout.addWidget(self.label_server_type, 1, 0, 1, 1)
        self.label_username = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 6, 0, 1, 1)
        self.input_checkbox_force_authuser = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_force_authuser.setObjectName("input_checkbox_force_authuser")
        self.gridLayout.addWidget(self.input_checkbox_force_authuser, 23, 0, 1, 3)
        self.label_monitor_url = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monitor_url.sizePolicy().hasHeightForWidth())
        self.label_monitor_url.setSizePolicy(sizePolicy)
        self.label_monitor_url.setObjectName("label_monitor_url")
        self.gridLayout.addWidget(self.label_monitor_url, 4, 0, 1, 1)
        self.input_checkbox_use_display_name_service = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_use_display_name_service.setObjectName("input_checkbox_use_display_name_service")
        self.gridLayout.addWidget(self.input_checkbox_use_display_name_service, 22, 0, 1, 3)
        self.input_lineedit_name = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_name.setObjectName("input_lineedit_name")
        self.gridLayout.addWidget(self.input_lineedit_name, 3, 2, 1, 2)
        self.label_auth_type = QtWidgets.QLabel(settings_server)
        self.label_auth_type.setObjectName("label_auth_type")
        self.gridLayout.addWidget(self.label_auth_type, 9, 0, 1, 1)
        self.input_lineedit_autologin_key = QtWidgets.QLineEdit(settings_server)
        self.input_lineedit_autologin_key.setText("")
        self.input_lineedit_autologin_key.setObjectName("input_lineedit_autologin_key")
        self.gridLayout.addWidget(self.input_lineedit_autologin_key, 11, 2, 1, 2)
        self.label_monitor_cgi_url = QtWidgets.QLabel(settings_server)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monitor_cgi_url.sizePolicy().hasHeightForWidth())
        self.label_monitor_cgi_url.setSizePolicy(sizePolicy)
        self.label_monitor_cgi_url.setObjectName("label_monitor_cgi_url")
        self.gridLayout.addWidget(self.label_monitor_cgi_url, 5, 0, 1, 1)
        self.input_checkbox_enabled = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_enabled.setObjectName("input_checkbox_enabled")
        self.gridLayout.addWidget(self.input_checkbox_enabled, 0, 0, 1, 4)
        self.input_checkbox_save_password = QtWidgets.QCheckBox(settings_server)
        self.input_checkbox_save_password.setObjectName("input_checkbox_save_password")
        self.gridLayout.addWidget(self.input_checkbox_save_password, 8, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 24, 0, 1, 4)
        self.input_combobox_authentication = QtWidgets.QComboBox(settings_server)
        self.input_combobox_authentication.setObjectName("input_combobox_authentication")
        self.gridLayout.addWidget(self.input_combobox_authentication, 9, 2, 1, 1)

        self.retranslateUi(settings_server)
        QtCore.QMetaObject.connectSlotsByName(settings_server)
        settings_server.setTabOrder(self.input_checkbox_enabled, self.input_combobox_type)
        settings_server.setTabOrder(self.input_combobox_type, self.input_lineedit_name)
        settings_server.setTabOrder(self.input_lineedit_name, self.input_lineedit_monitor_url)
        settings_server.setTabOrder(self.input_lineedit_monitor_url, self.input_lineedit_monitor_cgi_url)
        settings_server.setTabOrder(self.input_lineedit_monitor_cgi_url, self.input_lineedit_username)
        settings_server.setTabOrder(self.input_lineedit_username, self.input_lineedit_password)
        settings_server.setTabOrder(self.input_lineedit_password, self.input_checkbox_save_password)
        settings_server.setTabOrder(self.input_checkbox_save_password, self.input_checkbox_use_autologin)
        settings_server.setTabOrder(self.input_checkbox_use_autologin, self.input_combobox_authentication)
        settings_server.setTabOrder(self.input_combobox_authentication, self.input_lineedit_autologin_key)
        settings_server.setTabOrder(self.input_lineedit_autologin_key, self.input_checkbox_use_proxy)
        settings_server.setTabOrder(self.input_checkbox_use_proxy, self.input_lineedit_proxy_address)
        settings_server.setTabOrder(self.input_lineedit_proxy_address, self.input_lineedit_proxy_username)
        settings_server.setTabOrder(self.input_lineedit_proxy_username, self.input_lineedit_proxy_password)
        settings_server.setTabOrder(self.input_lineedit_proxy_password, self.input_checkbox_use_proxy_from_os)
        settings_server.setTabOrder(self.input_checkbox_use_proxy_from_os, self.input_checkbox_use_display_name_host)
        settings_server.setTabOrder(self.input_checkbox_use_display_name_host, self.input_checkbox_use_display_name_service)
        settings_server.setTabOrder(self.input_checkbox_use_display_name_service, self.input_checkbox_force_authuser)

    def retranslateUi(self, settings_server):
        _translate = QtCore.QCoreApplication.translate
        settings_server.setWindowTitle(_translate("settings_server", "Dialog"))
        self.label_password.setText(_translate("settings_server", "Password:"))
        self.input_lineedit_monitor_url.setText(_translate("settings_server", "https://monitor-server"))
        self.label_name.setText(_translate("settings_server", "Monitor name:"))
        self.input_lineedit_username.setText(_translate("settings_server", "username"))
        self.input_lineedit_monitor_cgi_url.setText(_translate("settings_server", "https://monitor-server/monitor/cgi-bin"))
        self.input_lineedit_password.setText(_translate("settings_server", "1234567890"))
        self.input_checkbox_use_proxy.setText(_translate("settings_server", "Use proxy"))
        self.input_checkbox_use_autologin.setText(_translate("settings_server", "Use autologin"))
        self.input_checkbox_use_display_name_host.setText(_translate("settings_server", "Use display name as host name"))
        self.proxy_groupbox.setTitle(_translate("settings_server", "Proxy:"))
        self.label_proxy_password.setText(_translate("settings_server", "Proxy password:"))
        self.label_proxy_username.setText(_translate("settings_server", "Proxy username:"))
        self.input_lineedit_proxy_username.setText(_translate("settings_server", "proxyusername"))
        self.input_lineedit_proxy_address.setText(_translate("settings_server", "http://proxy:port/"))
        self.label_proxy_address.setText(_translate("settings_server", "Proxy address:"))
        self.input_lineedit_proxy_password.setText(_translate("settings_server", "1234567890"))
        self.input_checkbox_use_proxy_from_os.setText(_translate("settings_server", "Use proxy from OS"))
        self.label_autologin_key.setText(_translate("settings_server", "Autologin Key:"))
        self.label_server_type.setText(_translate("settings_server", "Monitor type:"))
        self.label_username.setText(_translate("settings_server", "Username:"))
        self.input_checkbox_force_authuser.setText(_translate("settings_server", "Only show permitted hosts for \"see all\" users (1.4.0i1 or newer)"))
        self.label_monitor_url.setText(_translate("settings_server", "Monitor URL:"))
        self.input_checkbox_use_display_name_service.setText(_translate("settings_server", "Use display name as service name"))
        self.input_lineedit_name.setText(_translate("settings_server", "Monitor server"))
        self.label_auth_type.setText(_translate("settings_server", "Authentication:"))
        self.label_monitor_cgi_url.setText(_translate("settings_server", "Monitor CGI URL:"))
        self.input_checkbox_enabled.setText(_translate("settings_server", "Enabled"))
        self.input_checkbox_save_password.setText(_translate("settings_server", "Save password"))

