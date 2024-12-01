# Learning Tasks for Backend Basics

This document provides a structured list of exercises to help you learn key concepts of TCP/IP and backend development using Python.

## Task 1: Run the Basic Server and Client
1. Start the server (`src/server.py`) in one terminal:
   ```bash
   python src/server.py
   ```
2. Start the client (`examples/simple_client.py`) in another terminal:
   ```bash
   python examples/simple_client.py
   ```
3. Verify that the client receives the welcome message from the server.

## Task 2: Handle Multiple Clients
Modify the `server.py` script to:
1. Support multiple clients simultaneously using the `threading` module.
2. Each client should receive a unique session ID and a personalized message.
3. Ensure all client connections are handled properly without crashing the server.

## Task 3: Enhance Error Handling
1. Add error handling in `client.py` to gracefully manage:
   - Server unavailability (e.g., when the server is offline).
   - Unexpected disconnections during communication.
2. Log all errors to the console.

## Task 4: Logging and Configuration Management
1. Create a `utils/` module with:
   - A `logger.py` file for logging server and client events to a file.
   - A `config.py` file for centralizing configuration settings like host and port.

## Task 5: Create Unit Tests
1. Write unit tests for the server and client:
   - Test server response to a mock client connection.
   - Test client behavior when the server is unavailable.
2. Place test files in the `tests/` directory.

## Task 6: Implement Protocol Improvements
1. Upgrade the server to use a custom communication protocol:
   - Define message structures (e.g., include headers for message type and length).
   - Implement message parsing and validation on both server and client sides.
2. Update the client to support the new protocol.

## Task 7: Advanced Features (Optional)
1. Add encryption for messages exchanged between server and client using the `ssl` module.
2. Implement authentication (e.g., clients must provide a valid token before accessing the server).
