#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import unittest
import pathlib
from ind import create_db, add_trains, select_all


class indTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("Проверка работы операций с базами данных")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("Конец")

    def test_create_db(self):
        # Проверка существования файла базы данных
        self.assertTrue(create_db("test_bd"), msg="Файл базы данных не найден")

    def test_added_train(self):
        # Подготовка тестовых данных
        name_bd = "test_bd"
        nomer = "T1"
        punkts = "Destination1"
        time = 10

        # Добавление поезда
        add_trains(name_bd, nomer, punkts, time)

        # Проверка, был ли поезд добавлен успешно
        self.assertTrue(add_trains(name_bd, nomer, punkts, time), msg="Поезд не был добавлен")

    def test_select_all(self):
        # Подготовка тестовых данных
        name_bd = "test_bd"
        nomer = "T1"
        punkts = "Destination1"
        time = 10

        # Добавление поезда
        add_trains(name_bd, nomer, punkts, time)

        # Получение всех поездов
        trains = select_all(name_bd)

        # Проверка, был ли добавленный поезд получен
        self.assertEqual(len(trains), 1, msg="Ошибка при получении списка поездов")
        self.assertEqual(trains[0]["nomer"], nomer)
        self.assertEqual(trains[0]["punkt"], punkts)
        self.assertEqual(trains[0]["time"], time)


if __name__ == "__main__":
    unittest.main()
