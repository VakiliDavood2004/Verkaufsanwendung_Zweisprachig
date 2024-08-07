# 🇩🇪 Verkaufs- und Bestellverwaltungssystem

Eine leistungsstarke Desktop-Anwendung zur Verwaltung von Bestellungen, Kunden, Produkten und Dienstleistungen – mit moderner grafischer Benutzeroberfläche und integrierter lokaler Datenbank.  
Entwickelt mit **Python**, **PyQt5** und **SQLite** – ideal für kleine und mittelständische Unternehmen.

---

## 🚀 Hauptfunktionen

- Erfassung von Bestellungen mit vollständigen Details (Produkte, Dienstleistungen, Kunden)  
- Automatische Berechnung des Gesamtbetrags (Produkt × Menge + Dienstleistungen)  
- Verwaltung von Kunden-, Produkt- und Dienstleistungsdaten  
- Erstellung offizieller Rechnungen und detaillierter Verkaufsberichte  
- Integrierte Tools wie Taschenrechner, Notizblock, Kalender und Chat-Assistent  
- Einfache, schnelle und erweiterbare Benutzeroberfläche – auch für nicht-technische Nutzer geeignet  

---

## 🧩 Modulübersicht

| Modulname | Beschreibung |
|-----------|--------------|
| `main.py` | Einstiegspunkt der Anwendung; lädt das Hauptfenster |
| `order_module.py` | Bestellformular mit Preisberechnung |
| `product_module.py` | Hinzufügen und Bearbeiten von Produktinformationen |
| `customer_module.py` | Hinzufügen und Bearbeiten von Kundendaten |
| `service_module.py` | Hinzufügen und Bearbeiten von Dienstleistungen |
| `order_manager_module.py` | Verwaltung von Bestellungen mit Such- und Löschfunktion |
| `product_list_module.py` | Anzeige der Produktliste in Tabellenform |
| `customer_manager_module.py` | Vollständige Kundenverwaltung |
| `service_manager_module.py` | Verwaltung verfügbarer Dienstleistungen |
| `invoice_module.py` | Erstellung offizieller Rechnungen |
| `report_module.py` | Berichtserstellung basierend auf Filterkriterien |
| `sales_analysis_module.py` | Statistische Verkaufsanalyse mit Diagrammen |
| `discount_tax_calculator.py` | Berechnung von Rabatten und Steuern |
| `advanced_calculator_module.py` | Erweiterter Taschenrechner für manuelle Berechnungen |
| `notepad_module.py` | Interner Notizblock zum Speichern von Texten |
| `clock_calendar_widget.py` | Anzeige von Uhrzeit und Kalender im Programm |
| `chat_module.py` | Einfacher Chat mit Benutzer oder Assistent |
| `feedback_form_module.py` | Formular zur Erfassung von Nutzerfeedback |
| `help_module.py` | Benutzerhilfe für verschiedene Programmteile |
| `delete_product_module.py` | Löschen von Produkten mit Benutzerbestätigung |
| `user_module.py` | Benutzerverwaltung und Zugriffskontrolle (optional) |
| `icon.ico` | Programmsymbol |
| `sales.db` | SQLite-Datenbank mit den Haupttabellen |
| `README.md` | Projektdokumentation für Entwickler und Nutzer |

---

## 🛠️ Installation und Ausführung

### Voraussetzungen:
- Python Version 3.7 oder höher  
- PyQt5-Bibliothek  

### Installation von PyQt5:

```bash
pip install PyQt5
```

### Ausführung der Anwendung:

```bash
python main.py
```

---

## 📌 Hinweise zur Entwicklung

- Alle Formulare basieren auf `QWidget` und lassen sich einfach in `QMainWindow` integrieren  
- Die SQLite-Datenbank wird automatisch erstellt und ist portabel  
- Die modulare Struktur des Codes erleichtert Wartung und Erweiterung  
- Der Code ist übersichtlich, dokumentiert und skalierbar gestaltet  

---

## 👨‍💻 Entwickler

**Davood Vakili**  
Softwareentwickler mit Spezialisierung auf Python, PyQt und modernes UI-Design.  
Offen für internationale Projekte und maßgeschneiderte Softwarelösungen für den deutschen Markt.

---

## 📬 Kontakt

Wenn Sie dieses Projekt nützlich finden oder an einer Weiterentwicklung interessiert sind, freue ich mich über Ihre Nachricht:

- 📧 E-Mail: vakili.dev@gmail.com  
- 💼 LinkedIn: [linkedin.com/in/davoodvakili](https://linkedin.com/in/davoodvakili)  
- 🌐 GitHub: [github.com/davoodvakili](https://github.com/davoodvakili)  
- 🗣️ Arbeitssprachen: Persisch, Englisch, Deutsch (B1/B2-Niveau)

Ich freue mich auf eine mögliche Zusammenarbeit! 
Ich bin sehr motiviert, praktische Erfahrungen in einem deutschen Unternehmen zu sammeln und suche aktiv nach einer Praktikumsstelle im Bereich Softwareentwicklung. Besonders interessiere ich mich für moderne Technologien, dokumentierte Entwicklungsprozesse und internationale Teamarbeit. Gerne bringe ich meine Kenntnisse in Python, PyQt und UI-Design ein und bin bereit, mich weiterzuentwickeln und Neues zu lernen.

---

# 🇬🇧 Sales and Order Management System

A powerful desktop application for managing orders, customers, products, and services — featuring a modern graphical user interface and an integrated local database.  
Built with **Python**, **PyQt5**, and **SQLite**, ideal for small to medium-sized businesses.

---

## 🚀 Key Features

- Register orders with full details including products, services, and customers  
- Automatically calculate total amount (product × quantity + services)  
- Manage customer, product, and service information  
- Generate official invoices and detailed sales reports  
- Built-in tools such as calculator, notepad, calendar, and chat assistant  
- Simple, fast, and scalable user interface suitable for non-technical users  

---

## 🧩 Module Overview

| Module Name | Description |
|-------------|-------------|
| `main.py` | Entry point of the application; loads the main window |
| `order_module.py` | Order form with total price calculation |
| `product_module.py` | Add and edit product information |
| `customer_module.py` | Add and edit customer information |
| `service_module.py` | Add and edit service information |
| `order_manager_module.py` | Manage orders with search and delete functionality |
| `product_list_module.py` | Display product list in table format |
| `customer_manager_module.py` | Full customer management |
| `service_manager_module.py` | Manage available services |
| `invoice_module.py` | Generate official invoices for orders |
| `report_module.py` | Generate sales reports based on filters |
| `sales_analysis_module.py` | Analyze sales statistics with charts |
| `discount_tax_calculator.py` | Calculate discounts and taxes for orders |
| `advanced_calculator_module.py` | Advanced calculator for manual operations |
| `notepad_module.py` | Internal notepad for saving notes and reminders |
| `clock_calendar_widget.py` | Display clock and calendar inside the app |
| `chat_module.py` | Simple chat interface with user or assistant |
| `feedback_form_module.py` | Collect user feedback via form |
| `help_module.py` | User guide for different sections of the app |
| `delete_product_module.py` | Delete products with user confirmation |
| `user_module.py` | Manage users and access levels (if multi-user setup is needed) |
| `icon.ico` | Application icon |
| `sales.db` | SQLite database containing core tables |
| `README.md` | Project documentation for developers and users |

---

## 🛠️ Installation & Setup

### Requirements:
- Python 3.7 or higher  
- PyQt5 library  

### Install PyQt5:

```bash
pip install PyQt5
```

### Run the application:

```bash
python main.py
```

---

## 📌 Development Notes

- All forms are based on `QWidget` and can be easily integrated into `QMainWindow`  
- SQLite database is auto-generated and portable across systems  
- Modular code structure ensures easy maintenance and feature expansion  
- Code is written with clean structure, documentation, and scalability in mind  

---

## 👨‍💻 Developer

**Davood Vakili**  
Software developer specialized in Python, PyQt, and modern UI design.  
Open to collaboration on international projects and custom software solutions for the German market.

---

## 📬 Contact

If you found this project useful or would like to collaborate on advanced versions, feel free to reach out:

- 📧 Email: vakili.dev@gmail.com  
- 💼 LinkedIn: [linkedin.com/in/davoodvakili](https://linkedin.com/in/davoodvakili)  
- 🌐 GitHub: [github.com/davoodvakili](https://github.com/davoodvakili)  
- 🗣️ Working languages: Persian, English, German (B1/B2 level)

Looking forward to connecting and building great things together!

---

# 🛍️ سیستم مدیریت فروش و سفارش‌ها

نرم‌افزار دسکتاپی قدرتمند برای مدیریت سفارش‌ها، مشتریان، محصولات و خدمات، با رابط کاربری گرافیکی مدرن و پایگاه داده داخلی.  
توسعه‌یافته با استفاده از **Python**، **PyQt5** و **SQLite**، مناسب برای کسب‌وکارهای کوچک و متوسط.

---

## 🚀 ویژگی‌های کلیدی

- ثبت سفارش با جزئیات کامل شامل محصولات، خدمات و مشتریان  
- محاسبه خودکار مبلغ کل سفارش (محصول × تعداد + خدمات)  
- مدیریت اطلاعات مشتریان، محصولات و خدمات  
- صدور فاکتور رسمی و گزارش‌گیری دقیق از فروش‌ها  
- ابزارهای جانبی مانند ماشین‌حساب، دفترچه یادداشت، تقویم و گفت‌وگو  
- رابط کاربری ساده، سریع، قابل توسعه و مناسب برای کاربران غیرتخصصی  

---

## 🧩 ساختار ماژول‌ها

| نام ماژول | عملکرد |
|-----------|--------|
| `main.py` | نقطه شروع برنامه و بارگذاری پنجره اصلی |
| `order_module.py` | فرم ثبت سفارش با محاسبه مبلغ کل |
| `product_module.py` | افزودن و ویرایش اطلاعات محصولات |
| `customer_module.py` | افزودن و ویرایش اطلاعات مشتریان |
| `service_module.py` | افزودن و ویرایش اطلاعات خدمات |
| `order_manager_module.py` | مدیریت سفارش‌ها با قابلیت جستجو و حذف |
| `product_list_module.py` | نمایش لیست محصولات به‌صورت جدولی |
| `customer_manager_module.py` | مدیریت کامل اطلاعات مشتریان |
| `service_manager_module.py` | مدیریت خدمات قابل ارائه |
| `invoice_module.py` | صدور فاکتور رسمی برای سفارش‌ها |
| `report_module.py` | گزارش‌گیری از فروش‌ها بر اساس فیلترهای مختلف |
| `sales_analysis_module.py` | تحلیل آماری فروش‌ها با نمودار و آمار دقیق |
| `discount_tax_calculator.py` | محاسبه تخفیف و مالیات سفارش‌ها |
| `advanced_calculator_module.py` | ماشین‌حساب پیشرفته برای محاسبات دستی |
| `notepad_module.py` | دفترچه یادداشت داخلی برای ذخیره متن‌ها |
| `clock_calendar_widget.py` | نمایش ساعت و تقویم در محیط برنامه |
| `chat_module.py` | گفت‌وگوی ساده با کاربر یا دستیار داخلی |
| `feedback_form_module.py` | فرم دریافت بازخورد از کاربران |
| `help_module.py` | راهنمای استفاده از بخش‌های مختلف برنامه |
| `delete_product_module.py` | حذف محصولات با تأیید کاربر |
| `user_module.py` | مدیریت کاربران و سطح دسترسی (در صورت نیاز) |
| `icon.ico` | آیکون برنامه |
| `sales.db` | پایگاه داده SQLite شامل جداول اصلی |
| `README.md` | مستندات پروژه برای توسعه‌دهندگان و کاربران |

---

## 🛠️ نصب و راه‌اندازی

### پیش‌نیازها:
- Python نسخه ۳.۷ یا بالاتر  
- کتابخانه PyQt5  

### نصب PyQt5:

```bash
pip install PyQt5
```

### اجرای برنامه:

```bash
python main.py
```

---

## 📌 نکات فنی توسعه

- تمام فرم‌ها بر پایه کلاس `QWidget` طراحی شده‌اند و به‌راحتی قابل اتصال به `QMainWindow` هستند.  
- پایگاه داده SQLite به‌صورت خودکار ساخته می‌شود و قابل انتقال به سیستم‌های دیگر است.  
- ساختار ماژولار کدها توسعه، نگهداری و افزودن قابلیت‌های جدید را بسیار آسان می‌کند.  
- کدها با رعایت اصول خوانایی، مستندسازی و قابلیت توسعه طراحی شده‌اند.

---

## 👨‍💻 توسعه‌دهنده

**داوود وکیلی**  
توسعه‌دهنده نرم‌افزار با تخصص در Python، PyQt و طراحی رابط کاربری مدرن.  
مشتاق همکاری در پروژه‌های بین‌المللی و توسعه راه‌حل‌های نرم‌افزاری سفارشی برای بازار آلمان.

---

## 📬 راه‌های ارتباطی

اگر این پروژه برایتان مفید بود، یا قصد توسعه و همکاری در نسخه‌های پیشرفته‌تر آن را دارید، خوشحال می‌شوم در ارتباط باشیم.

- 📧 ایمیل: vakili.dev@gmail.com  
- 💼 لینکدین: [linkedin.com/in/davoodvakili](https://linkedin.com/in/davoodvakili)  
- 🌐 گیت‌هاب: [github.com/davoodvakili](https://github.com/davoodvakili)  
- 🗣️ زبان‌های کاری: فارسی، انگلیسی، آلمانی (سطح B1/B2)
