---
title: "Duke"
template: page
slug: "/duke"
---
# User Guide

## Features 

### Feature 1 
Record Todos, Events and Deadlines.

## Usage
```
todo <desc>
event <desc> at <dd/mm/yy hhmm>
deadline <desc> by <dd/mm/yy hhmm>
```

### Example of usage: 

```
todo finish up 2103 ip duke
deadline submit post lecture quiz by 22/11/2019 2359
event prom at 11/11/2011 2000
```

Expected outcome:

A confirmation message about the item being recorded.

### Feature 2 
List all todos/events/deadlines

## Usage
```
ls|list
```

Expected outcome:

A list of recorded items, in ascending chronological order.

### Feature 3 
Mark an item as done, and remove it

## Usage
```
done <index>
delete|rm <index>
```

### Example of usage: 

```bash
list     # a list of items shown
done 2
rm 2     # an alias
remove 1 # even if not done
ls       # 1 and 2 gone.
```

Expected outcome:

Item is deleted from memory.

