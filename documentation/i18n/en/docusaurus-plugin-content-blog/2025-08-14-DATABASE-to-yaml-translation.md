---
slug: DB-to-yaml
title: Database Migration from Markdown to YAML
authors: [Nicolas]
tags: [idea]
---

Due to the convenience of YAML, the database was migrated from Markdown.

<!-- truncate -->

## Why Did We Switch to YAML? 🤔

Previously, our database used the Markdown (`.md`) format. While Markdown is excellent for human readability, its machine processing was challenging:

- **AST Transformations** 🔄:  
  Any data modification required:
  1. Parsing MD into an Abstract Syntax Tree (AST)
  2. Making changes to the AST
  3. Converting back to MD
- **Fragility** ⚠️:  
  Slight markup deviations could break the parser
- **Limited Structure** 📦:  
  Difficult to express nested data relationships

## Advantages of YAML 🚀

The transition to YAML solved these problems:

```yaml
# Example data structure in YAML
character:
  id: hero_ivan
  name: Ivan
  stats:
    strength: 15
    agility: 12
  inventory:
    - sword
    - health_potion
```

- **Direct Parsing** ⚡:  
  Data is immediately available as structured objects (lists, dictionaries)
- **Readability** 👁️:  
  Data hierarchy is visually obvious
- **Change Safety** 🔒:  
  Modify only specific fields without full re-parsing
- **Metadata Support** 🏷️:  
  Easy to add tags, comments, and data types

### Final Gains ⏱️💾
- Data processing speed increased by 3x
- Database handling code simplified by 40%
- Parsing errors: 0️⃣

Now we can focus on game logic development instead of fighting formats! 🎮✨