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
        self.setWindowTitle("Sales Management Program")
        self.resize(1200, 800)

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        menubar = self.menuBar()
        product_menu = menubar.addMenu("🛒 Product Management")
        service_menu = menubar.addMenu("🔧 Service Management")
        order_menu = menubar.addMenu("📋 Register Order")
        invoice_menu = menubar.addMenu("🖨️ Print Invoice")
        report_menu = menubar.addMenu("📊 Sales Reports")
        user_menu = menubar.addMenu("👤 User Management")
        customer_menu = menubar.addMenu("🏠 Customer Management")
        help_menu = menubar.addMenu("❓ Help / Guide")
        tools_menu = menubar.addMenu("🧮 Tools")

        exit_action = QAction("🚪 Exit", self)
        exit_action.triggered.connect(self.close_program)
        menubar.addAction(exit_action)

        self.add_submenu(product_menu, "➕ Add Product", self.show_product_module)
        product_menu.addAction("❌ Delete Product", self.show_delete_product_module)
        self.add_submenu(product_menu, "📜 Display Products", self.show_product_list)
        self.add_submenu(service_menu, "➕ Add Service", self.show_service_module)
        self.add_submenu(service_menu, "🔄 Service Management", self.show_service_manager)
        self.add_submenu(order_menu, "🆕 Add New Order", self.show_order_module)
        self.add_submenu(order_menu, "📋 Order Management", self.show_order_manager)
        self.add_submenu(invoice_menu, "🖨️ Print Invoice", self.show_invoice_module)
        self.add_submenu(report_menu, "📄 View Sales Report", self.show_report_module)
        self.add_submenu(report_menu, "📊 Sales Analysis", self.show_sales_analysis)
        self.add_submenu(user_menu, "🧑‍💼 User Registration", self.show_user_module)
        self.add_submenu(customer_menu, "➕ Add New Customer", self.show_customer_module)
        self.add_submenu(customer_menu, "👥 Customer Management", self.show_customer_manager)
        self.add_submenu(tools_menu, "🧠 Chat with AI", self.show_chat_window)
        self.add_submenu(tools_menu, "📝 Professional Notepad", self.show_notepad)
        self.add_submenu(tools_menu, "Short Checklist", self.show_checklist)
        self.add_submenu(tools_menu, "🔢 Tax/Discount Calculator", self.show_calculator_tool)
        self.add_submenu(tools_menu, "💬 Customer Feedback Form", self.show_feedback_form)
        self.add_submenu(help_menu, "View Help", self.show_help_module)
        

        # Tools
        self.add_submenu(tools_menu, "Advanced Calculator", self.show_advanced_calculator)

        # Clock and Calendar in the Bottom-Right Corner
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
            action.triggered.connect(lambda: print(f"Operations '{title}' Not yet defined!"))
        menu.addAction(action)

    def show_subwindow(self, widget):
        subwindow = QMdiSubWindow()
        subwindow.setWidget(widget)
        subwindow.setWindowTitle(widget.windowTitle())
        self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def show_product_module(self): self.show_subwindow(product_module.ProductForm())
    def show_delete_product_module(self): self.show_subwindow(delete_product_module.DeleteProductForm())
    def show_product_list(self): self.show_subwindow(product_list_module.ProductList())
    def show_service_module(self): self.show_subwindow(service_module.ServiceForm())
    def show_service_manager(self): self.show_subwindow(service_manager_module.ServiceManager())
    def show_order_module(self): self.show_subwindow(order_module.OrderForm())
    def show_order_manager(self): self.show_subwindow(order_manager_module.OrderManager())
    def show_invoice_module(self): self.show_subwindow(invoice_module.InvoiceForm())
    def show_report_module(self): self.show_subwindow(report_module.ReportForm())
    def show_sales_analysis(self): self.show_subwindow(sales_analysis_module.SalesAnalysis())
    def show_user_module(self): self.show_subwindow(user_module.User_Form())
    def show_customer_module(self): self.show_subwindow(customer_module.CustomerForm())
    def show_customer_manager(self): self.show_subwindow(customer_manager_module.CustomerManager())
    def show_chat_window(self): self.show_subwindow(chat_module.ChatWidget())
    def show_notepad(self): self.show_subwindow(notepad_module.Notepad())
    def show_checklist(self): self.show_subwindow(checklist_module.Checklist())
    def show_calculator_tool(self): self.show_subwindow(discount_tax_calculator.DiscountTaxCalculator())
    def show_feedback_form(self): self.show_subwindow(feedback_form_module.FeedbackForm())
    def show_help_module(self):
        help_window = help_module.HelpForm()
        help_window.exec_()
    def show_advanced_calculator(self): self.show_subwindow(advanced_calculator_module.AdvancedCalculator())

    def close_program(self): 
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





# cd F:\all files\New_folder\main.py
# pip install pyinstaller
# pyinstaller --onefile --windowed your_script.py
# pyinstaller --onefile --windowed --icon=your_icon.ico main.py
# pyinstaller --onefile --windowed --icon=icon.ico main.py