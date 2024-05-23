# Bookstore Inventory Manager

## *Description*
##### Python program that utilizes SQLite to manage a locally stored database with high efficiency. 

## *Table of contents*
* Installation
    * Prerequisites
* Usage
    * Before Starting
        * SQLite Viewer
        * Prepopulation
        * Running
    * Program Usage
        * Emptying Database
        * Populating Database
        * Updating Database
        * Searching Database
* Credits


## *Installation*

##### Run `git clone https://github.com/Calcifer04/Bookstore-Inventory-Manager` in your terminal to clone the files within this repository.

### Prerequisites
#### Make sure you have python installed, if you do not, you can install it here -> https://www.python.org/downloads/

#### Install the  Pyfiglet package by running `pip install pyfiglet` in your terminal. 

> You're all set!

## *Usage*

### Before starting:
#### Using a SQLite database viewer will allow you to view the database table.
#### I recommend using SQLite Viewer which is a free Visual Studio Code extension that enables a live view of this database table.
#### You can find it here > https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer Or you can use their web application here > https://sqliteviewer.app/

* #### The database comes pre-populated with 1 book as example shown below: 
    ![bookstore database](https://github.com/Calcifer04/Bookstore-Inventory-Manager/assets/96597022/33a09cd3-3389-40f3-a918-c794ea1bc213)

* #### When running the program using the command `python bookstore_inventory.py` in your terminal, you will be prompted with a menu shown below:
    ![bookstore menu](https://github.com/Calcifer04/Bookstore-Inventory-Manager/assets/96597022/6c97f776-6a96-45d0-8970-fae1ca5e16f9)

### Emptying Database
* #### To empty the database for your use, delete the already existing example book in the database by entering '3' to "delete book" and enter the ID '1000'.

### Populating Database
* #### To add book records to the database, enter '1' at the menu prompt and the program will ask you for the details of the book you wish to enter.
    * ##### Upon entering these details, the database will be populated. (You may need to refresh your SQLite Viewer to see newly inputted records) Here is an example of a populated database.
    ![bookstore database view](https://github.com/Calcifer04/Bookstore-Inventory-Manager/assets/96597022/10efdcaf-f176-48d4-aa6a-a5d9a6f2717e)
    

### Updating Database
* #### To update a record, enter '2' at the menu prompt. 
    * #### Enter the ID of the book you wish to update and select the criteria you wish to update via entering corresponding number. Enter new criteria.

### Searching Database
#### *If you are using SQLite viewer, searching can be done via viewing the database table.*
* #### To search for a record within the database, enter '4' at the menu prompt.
    * #### Enter the the corresponding number to search via ID, title or author. 
    * #### Enter ID, title or author for book you are searching for.

## *Credits*

##### Credit to https://github.com/Liano-CoGrammar for SQLite insight.