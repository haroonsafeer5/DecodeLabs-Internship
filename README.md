# Rule-Based AI Chatbot in C++

A lightweight, high-performance C++ command-line chatbot built using core data structures for instant phrase matching and interactive user conversations.

## Features
- **Fast Lookups:** Utilizes `std::unordered_map` for key-value response retrieval.
- **Input Normalization:** Case-insensitive string handling for user queries.
- **Interactive Terminal Loop:** Continuous interaction with custom fallback logic and graceful exit strategies.

## How to Run

### Prerequisites
- GCC/G++ Compiler installed on your system.

### Compilation & Execution
1. Open your terminal in the project directory.
2. Compile the C++ program:
   ```bash
   g++ main.cpp -o chatbot
