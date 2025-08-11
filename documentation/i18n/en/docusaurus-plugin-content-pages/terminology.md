---
slug: glossary
title: "Project Terminology"
---

# Terminology of the Norchevsky project

This page contains key terms used in the project. It serves as a single reference point for developers, scriptwriters, and players so that everyone understands the meaning of the concepts used.

---

## General Terms

### System
**Type:** General Term

**Definition:** The entire Norchevsky project as a single entity — [Software part](#software-part), [Intellectual part](#intellectual-part), and game logic.

**Example:** "The system processes game events and stores the results in the database."

---

### Software part
**Type:** General Term

**Definition:** All elements of the project not related to AI and agents: engine, databases, maps, interface.

**Nickname:** "Norchevsky" (in the narrow sense).

**Example:** "The software part calculates character movements and updates the map."

**Related:** [Intellectual part](#intellectual-part).

----

### Intelligent part
**Type:** General term

**Definition:** All AI-based components, including [agents](#agent) that process data and manage the gameplay.

**Nickname:** Agents.

**Example:** "The intellectual part generates text descriptions of events and expands the plot."

**Related:** [LLM](#LLM), [Agent](#agent).

----

## Architectural Terms

### Component
**Type:** Architecture

**Definition:** A mandatory system unit without which the project would be impossible or very difficult to run.

**Example:** "The Map component handles the positioning of objects in the world."

**Related:** [Module](#module).

----

### Module
**Type:** Architecture

**Definition:** An additional system unit that extends functionality, but is not required for the system to run.

**Example:** "The Combat Module adds tactical battles and advanced rules."

**Related:** [Component](#component).

----

### LLM
**Type:** Architecture (AI)

**Definition:** The central AI component that takes input from the [intellectual part](#intellectual-part), and then transforms it into structured and stylistically formatted text.

**Example:** "LLM transforms a set of facts about a location into a coherent description for the player."

**Linked:** [Agent](#agent), [Intellectual part](#intellectual-part).

----

### Agent
**Type:** Architecture (AI)

**Definition:** An AI component that performs a strictly defined intellectual task.

**Example:** "The Chronicler Agent analyzes events and adds them to the history of the world."

**Related to:** [LLM](#LLM), [Intellectual part](#intellectual-part).

----

## Game and logical terms

### Abstraction

**Type:** Game logic

**Definition:** A mechanism that allows you to extract parts of text (descriptions of objects, characters, locations, etc.), save them in a database, link them to other entities and call them when needed. It is used so that the AI can recognize recurring objects and use their previously defined descriptions, maintaining the integrity of the game world.

**Example:** "The text of the house description contains a phrase about a mug. Abstraction extracts the description of the mug, saves it in the database and links it to other objects. When the mug appears again, the AI uses the same description, rather than inventing a new one." **Linked:** [Agent](#agent), [Intellectual part](#intellectual-part)

----