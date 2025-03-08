#!/bin/bash
rm -rf allure-results/ allure-report/
pytest -n 4 --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report