#!/bin/python

from setuptools import setup

setup(  name        = "roomai",
        version     = "1.0.3",
        description = "A toolkit for developing and comparing imperfect information game bots",
        url         = "https://github.com/roomai/RoomAI",
        author      = "AlgorithmDog",
        author_email= "lili1987mail@gmail.com",
        license     = "MIT",
        packages    = ["roomai","roomai.kuhn","roomai.abstract","roomai.texas"],
        zip_safe    = False)
