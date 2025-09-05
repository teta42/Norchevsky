---
slug: glossary
title: "Project Terminology"
---

# Terminology of the Norchevsky Project

This page contains key terms of the project. It serves as a unified reference for developers, scriptwriters and players, so that everyone understands the meaning of key concepts and the role of system components.

---

## General Terms

### System
**Type:** General Term

**Definition:** The Norchevsky Project as a single organism that combines the [Software Part](#software-part), [Intellectual Part](#intellectual-part) and game logic.

**Example:** "The system processes game events and stores the results in the database."

---

### Software Part
**Type:** General Term

**Definition:** All technical components of the project that are not related to AI: engine, databases, maps, interface and other tools.

**Nickname:** "Norchevsky" (in the narrow sense).

**Example:** "The software part calculates character movements and updates the map."

---

### Intelligent part
**Type:** General term

**Definition:** A set of [agents](#agent) that perform all intellectual tasks: data processing, response generation, maintaining the integrity of the game world and developing the plot.

**Nickname:** Agents.

**Example:** "The intellectual part generates text descriptions of events and expands the plot."

---

### Generation cycle
**Type:** General term

**Definition:** The process of a complete response to a user prompt: from its analysis to text generation, identifying key [abstractions](#abstraction) and writing them to the database. The central component of the cycle is the [local agent bed](#local-agent-bed).

**Example:** "Each generation cycle begins with the analysis of the prompt and ends with the creation of abstractions for the database."

---

### Scene
**Type:** General term

**Definition:** The result of the generation cycle is a text block describing the current state of the game world and the consequences of the player's actions.

**Example:** "After the player's request, the system generated a scene describing a village at the foot of the mountains."

---

## Architectural terms

### Component
**Type:** Architecture

**Definition:** A key part of the system, without which the project's operation is impossible or significantly hampered.

**Example:** "The "Agent Person" component is responsible for dialogues with the player."

---

### Module
**Type:** Architecture

**Definition:** An additional part of the system that extends functionality, but is not required for launch.

**Example:** "The combat module adds tactical battles."

---

### Local agent bed
**Type:** Architecture

**Definition:** The central group of agents that is responsible for the current state of the game world: processes prompts, analyzes scene objects, forms responses and abstractions. The local bed is focused on the "present" - the immediate actions of the player and their consequences.

**Example:** "The local agent bed analyzes the player's request and forms a scene, updating the database."

---

### Global Agent Bed
**Type:** Architecture

**Definition:** A group of agents that builds and develops long-term elements of the game world: major storylines, future locations, global changes to the state of the world. The Global Bed thinks about the "medium and distant future."

**Example:** "The Global Agent Bed prepared the structure of the future story arc."

---

### Agent
**Type:** Architecture (AI)

**Definition:** A highly specialized AI component that performs one intellectual function: text generation, data analysis, updating the object database, etc. All agents together make up the [Intellectual Part](#intellectual-part).

**Example:** "The Chronicler Agent analyzes events and adds them to the history of the world."

---

## Game and Logical Terms

### Abstraction
**Type:** Game logic

**Definition:** A key unit of data extracted from the scene text (objects, characters, locations, events). Abstractions are stored in the database, which allows the system to use them in the future and maintain the integrity of the game world.

**Example:** "If a mug is found in the description, the system selects it as an abstraction, saves the description and uses it the next time the mug appears in the game."

---