import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMdiArea,
    QMdiSubWindow, QFrame, QVBoxLayout
)
from PyQt5.QtCore import Qt

import product_module
import service_module
import order_module
import invoice_module
import report_module
import user_module
import help_module
import customer_module  
import delete_product_module
import product_list_module  
import service_manager_module  
import order_manager_module  
import customer_manager_module  
import sales_analysis_module  
import clock_calendar_widget  
import advanced_calculator_module  
import chat_module
import notepad_module
import checklist_module
import discount_tax_calculator
import feedback_form_module

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Verkaufsverwaltungsprogramm")
        self.resize(1500, 700)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        menubar = self.menuBar()
        product_menu = menubar.addMenu("🛒 Produktverwaltung")
        service_menu = menubar.addMenu("🔧 Dienstleistungsverwaltung")
        order_menu = menubar.addMenu("📋 Bestellung registrieren")
        invoice_menu = menubar.addMenu("🖨️ Rechnung drucken")
        report_menu = menubar.addMenu("📊 Verkaufsberichte")
        user_menu = menubar.addMenu("👤 Benutzerverwaltung")
        customer_menu = menubar.addMenu("🏠 Kundenverwaltung")
        help_menu = menubar.addMenu("❓ Hilfe / Anleitung")
        tools_menu = menubar.addMenu("🧮 Werkzeuge")

        exit_action = QAction("🚪 Beenden", self)
        exit_action.triggered.connect(self.close_program)
        menubar.addAction(exit_action)

        self.add_submenu(product_menu, "➕ Produkt hinzufügen", self.show_product_module)
        product_menu.addAction("❌ Produkt löschen", self.show_delete_product_module)
        self.add_submenu(product_menu, "📜 Produkte anzeigen", self.show_product_list)
        self.add_submenu(service_menu, "➕ Dienstleistung hinzufügen", self.show_service_module)
        self.add_submenu(service_menu, "🔄 Dienstleistungsverwaltung", self.show_service_manager)
        self.add_submenu(order_menu, "🆕 Neue Bestellung hinzufügen", self.show_order_module)
        self.add_submenu(order_menu, "📋 Bestellverwaltung", self.show_order_manager)
        self.add_submenu(invoice_menu, "🖨️ Rechnung drucken", self.show_invoice_module)
        self.add_submenu(report_menu, "📄 Verkaufsbericht anzeigen", self.show_report_module)
        self.add_submenu(report_menu, "📊 Verkaufsanalyse", self.show_sales_analysis)
        self.add_submenu(user_menu, "🧑‍💼 Benutzerregistrierung", self.show_user_module)
        self.add_submenu(customer_menu, "➕ Neuen Kunden hinzufügen", self.show_customer_module)
        self.add_submenu(customer_menu, "👥 Kundenverwaltung", self.show_customer_manager)
        self.add_submenu(tools_menu, "🧠 Mit KI chatten", self.show_chat_window)
        self.add_submenu(tools_menu, "📝 Professioneller Notizblock", self.show_notepad)
        self.add_submenu(tools_menu, "📋 Kurze Checkliste", self.show_checklist)
        self.add_submenu(tools_menu, "🔢 Steuer-/Rabattrechner", self.show_calculator_tool)
        self.add_submenu(tools_menu, "💬 Kundenfeedback-Formular", self.show_feedback_form)
        self.add_submenu(help_menu, "❓ Hilfe anzeigen", self.show_help_module)

        # Werkzeuge
        self.add_submenu(tools_menu, "🧠 Erweiterter Rechner", self.show_advanced_calculator)

        # Uhr und Kalender in der unteren rechten Ecke
        self.clock_frame = QFrame(self)
        self.clock_frame.resize(200, 250)
        layout = QVBoxLayout(self.clock_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(clock_calendar_widget.AnalogClock())
        layout.addWidget(clock_calendar_widget.CalendarLabel())
        self.clock_frame.setLayout(layout)
        self.clock_frame.setStyleSheet("""
            background-color: #fdfdfd;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
        """)
        self.update_clock_position()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_clock_position()

    def update_clock_position(self):
        x = self.width() - self.clock_frame.width() - 10
        y = self.height() - self.clock_frame.height() - 10
        self.clock_frame.move(x, y)
        self.clock_frame.raise_()

    def add_submenu(self, menu, title, method=None):
        action = QAction(title, self)
        if method:
            action.triggered.connect(method)
        else:
            action.triggered.connect(lambda: print(f"Operationen '{title}' Noch nicht definiert!"))
        menu.addAction(action)

    def show_subwindow(self, widget):
        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(widget.windowTitle())
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()
