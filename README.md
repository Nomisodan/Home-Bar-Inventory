# Multi-Location Home Bar Inventory Manager

## Video Demo URL:

## Project Overview

This is a Python-based inventory management system designed to track items stored across multiple locations in a home (pantry/dry storage, wine room, fridge, freezer, and shelf). The backend provides core functionality for adding, removing, and moving items between locations while maintaining a global inventory view. This system is built as a foundation for future mobile app development.

## Features

- **Multi-Location Tracking**: Manage inventory across 5 distinct storage locations
- **Item Operations**: Add, remove, and transfer items between locations
- **Global Inventory View**: See total quantities across all locations
- **Data Persistence**: All data saved to JSON format for easy portability
- **Robust Error Handling**: Comprehensive validation and meaningful error messages
- **Backend Architecture**: Clean, reusable functions ready for mobile app integration

## Project Structure

project/
├── project.py # Main application with all core functions
├── test_project.py # Pytest test suite with 5+ test cases
├── inventory.json # Data storage (auto-created on first run)
├── requirements.txt # Project dependencies (pytest)
└── README.md # This file

## How to Run

### Installation
```bash
pip install -r requirements.txt

python project.py