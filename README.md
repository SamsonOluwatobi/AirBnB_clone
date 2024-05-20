# 0x00. AirBnB clone

## Project Description
Welcome to the AirBnB Clone Project!
This project aims to build a full web application inspired by AirBnB, starting with a command interpreter to manage objects. This first step is crucial as it lays the foundation for subsequent projects, including HTML/CSS templating, database storage, API, and front-end integration.
Command Interpreter Overview
The command interpreter is a tool that allows you to manage objects within the AirBnB ecosystem. It's similar to a shell, but with a specific use case. With this interpreter, you can:
Create new objects (e.g., User, Place)
Retrieve objects from storage (file, database, etc.)
Perform operations on objects (count, compute stats, etc.)
Update object attributes
Destroy objects
Project Goals
The goals of this project include:
Creating a parent class (BaseModel) for initialization, serialization, and deserialization
Establishing a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
Creating classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel
Developing the first abstracted storage engine: File storage
Writing unit tests to validate classes and storage engine

## Command Interpreter
This project includes a command interpreter that allows users to interactively execute commands.

### Starting the Interpreter
To start the command interpreter, simply run the following command:
    ./console.py

### Using the Interpreter
Users can enter various commands to perform specific actions. Here are some examples:
- `greet &lt;name>`: Displays a greeting message with the provided name.
- `help`: Displays a list of available commands and their descriptions.
- `exit`: Exits the interpreter.

### Available Commands
For a full list of available commands and their usage, please refer to the "Commands" section below.

## Commands
- `greet &lt;name>`: Greet the specified user.
- `help`: Display help information.
- `exit`: Exit the interpreter.

## Contributing
Contributions are welcome! Please refer to the "Contributing" section for guidelines.
