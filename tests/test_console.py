#!/usr/bin/python3
import unittest
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import sys


class TestConsole(unittest.TestCase):
    """

    """
    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
    
    def test_creat(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        ret = f.getvalue()[:-1]
        self.assertEqual(ret, "** class name missing **")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create blabla")
        ret = f.getvalue()[:-1]
        self.assertEqual(ret, "** class doesn't exist **")

    def test_create_(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        ret = f.getvalue()[:-1]
        self.assertEqual(len(ret), 36)


    def test_create_S(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Gabes"')
            HBNBCommand().onecmd('all State')
        ret = f.getvalue()[:-1]
        self.assertTrue("Gabes" in ret)

    def test_create_i(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State number_rooms=4')
            HBNBCommand().onecmd('all State')
        ret = f.getvalue()[:-1]
        self.assertTrue("'number_rooms': 4" in ret)

    def test_create_f(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State longitude=-122.431297')
            HBNBCommand().onecmd('all State')
        ret = f.getvalue()[:-1]
        self.assertTrue("longitude': -122.431297" in ret)