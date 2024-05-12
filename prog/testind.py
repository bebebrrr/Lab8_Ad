#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ind
import sqlite3
import unittest
import pathlib


def created_bd(name_bd):
    file_path = pathlib.Path.cwd() / name_bd

    if file_path.exists and file_path.is_file:
        return True
    return False


def added_train(name_bd, nomer, punkts, time):
    conn = sqlite3.connect(name_bd)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT punkts.punkt_name, nomers.nomer_title, punkts.times_count
            FROM punkts
            INNER JOIN nomers ON nomers.nomer_id = punkts.nomer_id
            WHERE
            punkts.punkt_name = ? and
            nomers.nomer_title = ? and
            punkts.times_count = ?
        """,
        (nomer, punkts, time),
    )
    rows = cursor.fetchall()
    conn.close()

    return bool(rows)


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

    def test_select_all_last(self):
        self.assertEqual(len(ind.select_all("test_bd")[-1]), 3)

    def test_select_all_first(self):
        self.assertEqual(len(ind.select_all("test_bd")[0]), 3)
