# LangGraph Functional APIs & Routing

This project demonstrates how to use **LangGraph's Functional APIs** to build dynamic, multi-step workflows and how **Routing** can be applied to control flow between different functions or nodes in the graph.

## 🚀 Overview

LangGraph is a powerful framework that extends the capabilities of LangChain by enabling **stateful, multi-agent, and graph-based workflows**. With **Functional APIs**, developers can define simple functions and use them as graph nodes. **Routing** helps control which path the graph follows next based on logic or user input.

## 📦 Key Features

- 🌐 **Functional API Integration**: Easily use Python functions as LangGraph nodes.
- 🔁 **Dynamic Routing**: Direct the flow of the conversation or tasks based on conditions.
- 🤖 **LLM Integration**: Combine with LLMs to create intelligent agents.
- 🔄 **Looping and Conditional Flows**: Model workflows that loop or branch conditionally.

## 🧱 Components

### Functional Nodes

These are simple Python functions that can be registered as nodes in your graph.

```python
def greet_user(state):
    print("Hello! How can I help you today?")
    return state 
```

## Router Nodes
Routers help you decide which node to call next, based on the current state or input.

```python
def route_based_on_intent(state):
    if state["intent"] == "book_flight":
        return "book_flight_node"
    elif state["intent"] == "get_weather":
        return "weather_node"
    else:
        return "fallback_node"
```

## Example Flow

Start ➡️ Greet User ➡️ Router ➡️ [Book Flight | Get Weather | Fallback]

        
