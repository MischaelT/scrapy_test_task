SHELL := /bin/bash

run_parsing:
	cd films_scraper && scrapy crawl film && python3 main.py
