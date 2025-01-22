# TitanicProject
This code contains the survival rates of the passengers who survived the Titanic accident by age, gender and passenger class.

-------------------------------------------------------------------------------------------------------------------------------

Titanic Dataset Analysis

This project includes visualization using SQL queries and Dash on the Titanic dataset.
The project was created to visualize the age distribution of Titanic passengers, survival rate and other different analyses.

Project Content

titanic.csv: Titanic Dataset.
TitanicQueries.db: File containing SQL queries of the Titanic dataset.
Titanic_DashApp.py: Application created using Dash to visualize the data.

Installation and Running Instructions

1. Software Required for Installation
You need the following software to use this project:

Python
pip (Python package manager)

2. Required Python Libraries
You can install the necessary libraries with the following commands via the terminal:

pip install dash
pip install plotly
pip install pandas

3. Running the Project
a) Download the project folder.

b) Go to the project folder in the terminal or command line:
cd TitanicProject

c) Type the following command to run the application:
python Titanic_DashApp.py

d) After running, a local connection URL will appear in the terminal (for example, http://127.0.0.1:8050).

e) You can view the application by going to this URL using your browser.

Running SQL Queries

SQL queries are available in the TitanicQueries.db file. To run these queries:

You can use a SQL tool (for example, PostgreSQL, MySQL Workbench, or SQLite).
You can load the Titanic dataset into the database and run the queries.

About Dash Visualization

The Dash application includes the following analyses and visualizations:

Survival rate by passenger class (for example, 1st, 2nd class) (Bar chart)
Survival rate by gender (Histogram)
Survival status by age (Histogram)

-------------------------------------------------------------------------------------------------------------------------------

Titanic Dataset Analysis

Bu proje, Titanic veri kümesi üzerinde SQL sorguları ve Dash kullanılarak görselleştirme yapılmasını kapsar.
Proje, Titanic yolcularının yaş dağılımını, hayatta kalma oranını ve diğer farklı analizleri görsele dökmek için yapılmıştır.


Proje İçeriği

titanic.csv:Titanic Dataset.
TitanicQueries.db: Titanic veri kümesi'nin SQL sorgularını içeren dosya.
Titanic_DashApp.py: Dash kullanılarak oluşturulan, verilerin görselleştirildiği uygulama.


Kurulum ve Çalıştırma Talimatları

1. Kurulum için gerekli Yazılımlar
Bu projeyi kullanabilmek için aşağıdaki yazılımlara ihtiyacınız var:

Python
pip (Python paket yöneticisi)


2. Gerekli Python Kütüphaneleri
Terminal üzerinden aşağıdaki komutlarla gerekli kütüphaneleri kurabilirsiniz:

pip install dash
pip install plotly
pip install pandas


3. Projeyi Çalıştırma
a) Proje klasörünü indirin.

b) Terminal veya komut satırında proje klasörüne gidin:
cd TitanicProject

c) Uygulamayı çalıştırabilmek için aşağıdaki komutu yazın:
python Titanic_DashApp.py

d) Çalıştırıldıktan sonra terminalde yerel bir bağlantı URL'si gözükecek (örneğin, http://127.0.0.1:8050).

e) Tarayıcınızı kullanıp bu URL'ye giderek uygulamayı görüntüleyebilirsiniz.



SQL Sorgularını Çalıştırma

SQL sorguları TitanicQueries.db dosyasında mevcuttur. Bu sorguları çalıştırabilmek için:

Bir SQL aracı (örneğin, PostgreSQL, MySQL Workbench veya SQLite) kullanabilirsiniz.
Titanic veri kümesini veri tabanına yükleyip sorguları çalıştırıp kullanabilirsiniz.


Dash Görselleştirme Hakkında

Dash uygulaması, şu analizleri ve görselleştirmeleri içerir:

Yolcu sınıfına(1st, 2nd class gibi) göre hayatta kalma oranı (Bar grafiği)
Cinsiyete göre hayatta kalma oranı (Histogram)
Yaşlara göre hayatta kalma durumu (Histogram)
