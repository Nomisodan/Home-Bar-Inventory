# Multi-Location Home Bar Inventory Manager

## Video Demo URL
https://youtu.be/F4QXMXu6OA0

## Project Overview
The Multi‑Location Home Bar Inventory Manager is a Python-based backend system designed to track and manage items stored across multiple household locations, such as a pantry/dry storage area, wine room, fridge, freezer, and shelf. The project was inspired by real-world experience working in a restaurant environment, where inventory often exists in several different rooms and must be counted separately while still contributing to a global total. This project recreates that workflow in software, providing a clean, testable backend that can later be expanded into a full mobile application.

The goal of this project is twofold:

Provide a functional inventory management tool that can be used immediately from the command line.

Serve as the backend logic layer for a future GUI or mobile app built in CS50’s Mobile App Development course.

By separating the logic from the interface, the project remains modular, maintainable, and easy to extend.

## Features

## Multi-Location Tracking  
The system manages inventory across five distinct storage locations. Each location maintains its own dictionary of items and quantities, allowing for precise tracking.

## Item Operations  
Users can add new items, remove quantities, or transfer items between locations. All operations include validation to prevent negative quantities or invalid moves.

## Global Inventory View  
The program can compute a combined total of all items across all locations, giving a complete overview of available stock.

## Data Persistence  
Inventory data is stored in a JSON file, making it easy to read, edit, back up, or integrate with other systems. The JSON format also aligns well with future mobile app development.

## Error Handling and Validation  
The system checks for invalid locations, missing items, insufficient quantities, and malformed data. Errors are raised with clear messages to help users understand what went wrong.

## Backend Architecture for Future Expansion  
All core logic is implemented as standalone functions, making the code easy to test and reuse. This structure is ideal for building a React Native or web-based interface later.

## Design Decisions

A JSON-based storage system was chosen because it is lightweight, human-readable, and compatible with both Python and JavaScript. This makes it ideal for future mobile development. The project avoids interactive menus or prompts in main() to keep the backend clean and focused on logic rather than user interface. Instead, main() simply demonstrates functionality by loading the inventory, performing sample operations, and saving the results.

The functions are intentionally small and single-purpose. For example, add_item(), remove_item(), and move_item() each handle one specific task. This makes the code easier to test and reduces the chance of bugs. The global inventory function aggregates data across all locations, which mirrors how real restaurants and bars track total stock.

## Testing Strategy
The project includes a test_project.py file containing multiple pytest test cases. These tests verify that the core functions behave correctly under normal and edge-case conditions. Tests include adding items, removing items, moving items between locations, and ensuring that invalid operations raise appropriate exceptions. By testing the logic independently of the interface, the project ensures reliability and correctness.

## Project Structure

project/
├── project.py          # Main application with all core functions
├── test_project.py     # Pytest test suite with 5+ test cases
├── inventory.json      # Data storage (auto-created on first run)
├── requirements.txt    # Project dependencies (pytest)
└── README.md           # This file

## How to run

## Installation

pip install -r requirements.txt

## Run the program

python project.py



