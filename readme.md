# Task Tracker

Another to-do list but in CLI. Not the first and not the last. Store the tasks with `id`, `createdAt`, `updatedAt`, `description`, `status` in tasks.json file. 

## Prerequisite

Python 3.10 or higher

## Usage

```bash
python task-cli.py <command> <arguments>
```

## Commands

### Add
Adds a task with the specified `description`. Outputs task's `ID`.
```bash
python task-cli.py add <task-description>
```

### Update
```bash
python task-cli.py update <ID> <task-description>
```
Changes the task's `description` with the specified `ID`.

### Delete
```bash
python task-cli.py delete <ID> 
```
Deletes the task with the specified `ID`.

### Mark-in-progress/Mark-done
```bash
python task-cli.py <mark-in-progress or mark-done> <ID> 
```
Changes the task's status with the specified `ID`.

### List
```bash
python task-cli.py list [status]
```
Lists all tasks with given `status`. If none given, list all.

## Related

Made for [roadmap.sh](https://roadmap.sh/projects/task-tracker) as training project.